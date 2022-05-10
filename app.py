from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from src.service.create_db import CreateDb
from src.resources.auth_ns_payload import auth_ns
from src.resources.student_ns_payload import students_ns, student_ns
from src.resources.user_ns_payload import users_ns, user_ns
from src.resources.filters_ns_payload import filters_ns
from src.resources.grade_grid_ns_payload import grade_grid_all_ns, grade_grid_ns
from src.controller.auth import (
    AuthLoginController,
    AuthLogoutController,
)
from src.controller.student import (
    StudentsController,
    StudentController,
    StudentAddController,
)
from src.controller.user import (
    UsersController,
    UserController,
    UserAddController,
    UserControllerStatus,
)
from src.controller.grade_grid import (
    GradeGridAllController,
    GradeGridController,
    GradeGridAddController,
    GradeGridAdvancedController,
)
from src.controller.filters import FilterFieldWordCotroller
from blacklist import BLACKLIST
import os
from dotenv import load_dotenv

load_dotenv()
APP_PORT = os.getenv("APP_PORT")
APP_DEV_CONFIG = os.getenv("APP_DEV")
APP_PROD_CONFIG = os.getenv("APP_PROD")

app = Flask(__name__)
app.config.from_object(APP_DEV_CONFIG)
api = Api(app)
jwt = JWTManager(app)

CreateDb.create_db()
CreateDb.create_table()


@jwt.token_in_blocklist_loader
def verifify_blacklist(self, token):
    return token["jti"] in BLACKLIST


api.add_namespace(students_ns)
api.add_namespace(student_ns)
api.add_namespace(auth_ns)
api.add_namespace(users_ns)
api.add_namespace(user_ns)
api.add_namespace(filters_ns)
api.add_namespace(grade_grid_all_ns)
api.add_namespace(grade_grid_ns)

auth_ns.add_resource(AuthLoginController, "/login")
auth_ns.add_resource(AuthLogoutController, "/logout")

users_ns.add_resource(UsersController, "")
user_ns.add_resource(UserController, "/<id>")
user_ns.add_resource(UserAddController, "")
user_ns.add_resource(UserControllerStatus, "")

students_ns.add_resource(StudentsController, "")
student_ns.add_resource(StudentController, "/<id>")
student_ns.add_resource(StudentAddController, "")

grade_grid_all_ns.add_resource(GradeGridAllController, "")
grade_grid_ns.add_resource(GradeGridController, "/<id>")
grade_grid_ns.add_resource(GradeGridAddController, "")
grade_grid_ns.add_resource(GradeGridAdvancedController, "")


filters_ns.add_resource(FilterFieldWordCotroller, "")

if __name__ == "__main__":
    app.run(port=APP_PORT or 5000)
