from src.service.postgresql import Postgresql
from src.model.dto.student_dto import StudentGetDto
from src.static.table_fields import fields_table_student

db = Postgresql()

connection = Postgresql().postgresql_connect()


class FiltersModel:
    def union_fields_values(self, fields, values):
        dict_union = dict(zip(fields, list(values)))
        format_date_str = dict_union.get("created_at").strftime("%d/%m/%Y %H:%M:%S")
        dict_union["created_at"] = format_date_str

        format_date_str = dict_union.get("birth_date").strftime("%d/%m/%Y")
        dict_union["birth_date"] = format_date_str
        dto = StudentGetDto(**dict_union)
        return dto

    def find_field_word(self, data):
        word_query = "%" + data.word + "%"
        sql_query = ("""SELECT * FROM public.student WHERE {} ILIKE %s""").format(
            data.field
        )
        data = (word_query,)

        db_result = db.fetch_all(sql_query, data)
        if db_result == []:
            return None

        payload_students = []
        for student in db_result:
            student_dto = self.union_fields_values(fields_table_student, student)
            payload_students.append(student_dto.dict())

        return payload_students
