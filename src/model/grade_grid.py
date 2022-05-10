from src.service.postgresql import Postgresql
from src.model.dto.grade_grid_dto import GradeGridGetDto
from src.static.table_fields import fields_table_grade_grid

db = Postgresql()


class GradeGridModel:
    def union_fields_values(self, fields, values):
        dict_union = dict(zip(fields, list(values)))
        format_date_str = dict_union.get("created_at").strftime("%d/%m/%Y %H:%M:%S")
        dict_union["created_at"] = format_date_str
        dto = GradeGridGetDto(**dict_union)
        return dto

    def get_all(self):
        sql_query = """SELECT * FROM public.grade_grid"""
        db_result = db.fetch_all(sql_query)
        if not db_result:
            return None

        payload_grade_grid = []
        for scored in db_result:
            scored_dto = self.union_fields_values(fields_table_grade_grid, scored)
            payload_grade_grid.append(scored_dto.dict())

        return payload_grade_grid

    def get_by_id(self, id):
        sql_query = """SELECT * FROM public.grade_grid WHERE scored_id = %s"""
        id_to_fetch = (id,)
        db_result = db.fetch_one(sql_query, id_to_fetch)
        if not db_result:
            return None

        data_dto_result = self.union_fields_values(fields_table_grade_grid, db_result)
        return data_dto_result

    def get_by_student_and_year(self, student_id, year):
        sql_query = (
            """SELECT * FROM public.grade_grid WHERE student_id = %s AND year = %s"""
        )
        data = (
            student_id,
            year,
        )
        db_result = db.fetch_one(sql_query, data)
        if not db_result:
            return None

        data_dto_result = self.union_fields_values(fields_table_grade_grid, db_result)
        return data_dto_result

    def find_student(self, id):
        sql_query = """SELECT * FROM public.student WHERE student_id = %s"""
        id_to_fetch = (id,)
        db_result = db.fetch_one(sql_query, id_to_fetch)
        if not db_result:
            return None
        return True

    def find_student_and_year(self, student_id, year):
        sql_query = (
            """SELECT * FROM public.grade_grid WHERE student_id = %s AND year = %s"""
        )
        data = (
            student_id,
            year,
        )
        db_result = db.fetch_one(sql_query, data)
        if not db_result:
            return None
        return True

    def add(self, payload):
        sql_query = """INSERT INTO public.grade_grid (student_id, year, "portuguese", "mathematics", "biology", "geography", "history") VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        data_to_insert = (
            payload.student_id,
            payload.year,
            payload.portuguese,
            payload.mathematics,
            payload.biology,
            payload.geography,
            payload.history,
        )
        data_result = db.execute_modify(sql_query, data_to_insert)
        return data_result

    def update(self, id, payload):
        sql_query = (
            """UPDATE public.grade_grid SET {}=%s WHERE scored_id=%s"""
        ).format(payload.subject)
        data_to_update = (
            payload.scored,
            id,
        )
        db_result = db.execute_modify(sql_query, data_to_update)
        if db_result == []:
            return None
        return db_result

    def update_by_student_year(self, payload):
        sql_query = (
            """UPDATE public.grade_grid SET {}=%s WHERE student_id=%s AND year=%s"""
        ).format(payload.subject)
        data_to_update = (
            payload.scored,
            payload.student_id,
            payload.year,
        )
        db_result = db.execute_modify(sql_query, data_to_update)
        if db_result == []:
            return None
        return db_result

    def delete(self, id):
        sql_query = """DELETE FROM public.grade_grid WHERE scored_id = %s"""
        id_to_delete = (id,)
        data_result = db.execute_modify(sql_query, id_to_delete)
        return data_result
