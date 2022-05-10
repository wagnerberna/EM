from src.service.postgresql import Postgresql
from src.model.dto.user_dto import UserGetDto
from src.static.table_fields import fields_table_user

db = Postgresql()


class UserModel:
    def union_fields_values(self, fields, values):
        dict_union = dict(zip(fields, list(values)))
        format_date_str = dict_union.get("created_at").strftime("%d/%m/%Y %H:%M:%S")
        dict_union["created_at"] = format_date_str
        dto = UserGetDto(**dict_union)
        return dto

    def get_all(self):
        sql_query = """SELECT * FROM public.user"""
        db_result = db.fetch_all(sql_query)
        if not db_result:
            return None

        payload_users = []
        for user in db_result:
            user_dto = self.union_fields_values(fields_table_user, user)
            payload_users.append(user_dto.dict())

        return payload_users

    def find_login(self, login):
        sql_query = """SELECT * FROM public.user WHERE login = %s"""
        login_to_fetch = (login,)

        db_result = db.fetch_one(sql_query, login_to_fetch)
        if db_result == None:
            return False
        return True

    def get_by_id(self, id):
        sql_query = """SELECT * FROM public.user WHERE user_id = %s"""
        id_to_fetch = (id,)
        db_result = db.fetch_one(sql_query, id_to_fetch)
        if not db_result:
            return None

        data_dto_result = self.union_fields_values(fields_table_user, db_result)
        return data_dto_result

    def add(self, payload):
        sql_query = """INSERT INTO public.user (name, login, password, activated) VALUES (%s,%s,%s, %s)"""
        data_to_insert = (
            payload.name,
            payload.login,
            payload.password,
            payload.activated,
        )
        data_result = db.execute_modify(sql_query, data_to_insert)
        return data_result

    def update(self, id, payload):
        sql_query = ("""UPDATE public.user SET {}=%s WHERE user_id=%s""").format(
            payload.field
        )
        data = (payload.value, id)
        db_result = db.execute_modify(sql_query, data)
        if db_result == []:
            return None
        return db_result

    def update_status(self, payload):
        sql_query = ("""UPDATE public.user SET activated=%s WHERE login=%s""").format(
            payload.status
        )
        data = (payload.status, payload.login)
        db_result = db.execute_modify(sql_query, data)
        return db_result

    def delete(self, id):
        sql_query = """DELETE FROM public.user WHERE user_id = %s"""
        id_to_delete = (id,)
        data_result = db.execute_modify(sql_query, id_to_delete)
        return data_result
