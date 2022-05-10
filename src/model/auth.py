from src.service.postgresql import Postgresql
from src.model.dto.auth_dto import AuthDtoGet
from src.static.table_fields import fields_table_user

db = Postgresql()

connection = Postgresql().postgresql_connect()


class AuthModel:
    def find_login(self, login):
        sql_query = """SELECT * FROM public.user WHERE login = %s"""
        login_to_fetch = (login,)

        db_result = db.fetch_one(sql_query, login_to_fetch)
        if db_result == None:
            return db_result

        dict_fields_and_db_result = dict(zip(fields_table_user, list(db_result)))
        data_result = AuthDtoGet(**dict_fields_and_db_result)
        return data_result

    def update_status(self, login, status):
        sql_query = """UPDATE public.user SET activated=%s WHERE login=%s"""
        data_update = (status, login)
        data_result = db.execute_modify(sql_query, data_update)
        return data_result
