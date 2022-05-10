from src.service.postgresql import Postgresql
from src.model.dto.student_dto import StudentGetDto
from src.static.table_fields import fields_table_student

db = Postgresql()


class StudentModel:
    def union_fields_values(self, fields, values):
        dict_union = dict(zip(fields, list(values)))
        format_date_str = dict_union.get("created_at").strftime("%d/%m/%Y %H:%M:%S")
        dict_union["created_at"] = format_date_str
        format_date_str = dict_union.get("birth_date").strftime("%d/%m/%Y")
        dict_union["birth_date"] = format_date_str
        dto = StudentGetDto(**dict_union)
        return dto

    def get_all(self):
        sql_query = """SELECT * FROM public.student"""
        db_result = db.fetch_all(sql_query)
        if not db_result:
            return None

        payload_students = []
        for student in db_result:
            student_dto = self.union_fields_values(fields_table_student, student)
            payload_students.append(student_dto.dict())

        return payload_students

    def get_by_id(self, id):
        sql_query = """SELECT * FROM public.student WHERE student_id = %s"""
        id_to_fetch = (id,)
        db_result = db.fetch_one(sql_query, id_to_fetch)
        if not db_result:
            return None

        data_dto_result = self.union_fields_values(fields_table_student, db_result)
        return data_dto_result

    def add(self, payload):
        sql_query = """INSERT INTO public.student (name, birth_date, address, tutor_name, cpf_tutor, tutor_email) VALUES (%s,%s,%s,%s,%s,%s)"""
        data_to_insert = (
            payload.name,
            payload.birth_date,
            payload.address,
            payload.tutor_name,
            payload.cpf_tutor,
            payload.tutor_email,
        )
        data_result = db.execute_modify(sql_query, data_to_insert)
        return data_result

    def update(self, id, payload):
        sql_query = ("""UPDATE public.student SET {}=%s WHERE student_id=%s""").format(
            payload.field
        )
        data = (payload.value, id)

        db_result = db.execute_modify(sql_query, data)
        if db_result == []:
            return None
        return db_result

    def delete(self, id):
        sql_query = """DELETE FROM public.student WHERE student_id = %s"""
        id_to_delete = (id,)
        data_result = db.execute_modify(sql_query, id_to_delete)
        return data_result
