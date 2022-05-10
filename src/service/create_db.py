from src.service.postgresql import Postgresql

db = Postgresql()


class CreateDb:
    def create_db():
        sql_query_check_db = (
            "SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'school_test'"
        )
        db_exists = db.fetch_one(sql_query_check_db)
        if not db_exists:
            sql_query_db = "CREATE DATABASE school_test;"
            db.create_db(sql_query_db)

    def create_table():
        sql_query_tables = """
            CREATE TABLE IF NOT EXISTS public.student (
                student_id serial NOT NULL,
                name varchar NOT NULL,
                birth_date date NOT Null,
                address varchar NOT NULL,
                tutor_name varchar NOT NULL,
                cpf_tutor varchar NOT NULL,
                tutor_email varchar NOT NULL,
                created_at TIMESTAMP DEFAULT now(),
                PRIMARY KEY (student_id)
            );
            CREATE TABLE IF NOT EXISTS public.grade_grid (
                scored_id serial NOT NULL,
                student_id int NOT NULL,
                year int NOT NULL,
                portuguese float,
                mathematics float,
                biology float,
                geography float,
                history float,
                created_at TIMESTAMP DEFAULT now(),
                PRIMARY KEY (scored_id),
                FOREIGN KEY(student_id) REFERENCES public.student (student_id)
            );
            CREATE TABLE IF NOT EXISTS public.user (
                user_id serial NOT NULL,
                name varchar NOT NULL,
                login varchar NOT NULL,
                password varchar NOT NULL,
                activated bool NOT NULL,
                created_at TIMESTAMP DEFAULT now()
            );
            """
        result_db = db.execute_modify(sql_query_tables)
        print(result_db)

    def drop_db():
        sql_query_drop_db = "DROP DATABASE school_test;"
        db.create_db(sql_query_drop_db)
