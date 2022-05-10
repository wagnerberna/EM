from src.utils.normalize import NormalizeFields
from src.model.dto.student_dto import (
    StudentAddDto,
    StudentUpdateBirthDateDto,
    StudentDtoUpdateEmail,
)

normalize_fields = NormalizeFields()


class StudentCore:
    def payload_new_student(self, new_student):

        payload_add_student = StudentAddDto(
            name=normalize_fields.string(new_student.name),
            birth_date=new_student.birth_date,
            address=normalize_fields.string(new_student.address),
            tutor_name=normalize_fields.string(new_student.tutor_name),
            cpf_tutor=normalize_fields.cpf(new_student.cpf_tutor),
            tutor_email=normalize_fields.string(new_student.tutor_email),
        )
        return payload_add_student

    def payload_update_student(self, update_student):
        if update_student.field == "birth_date":
            update_student_birth_date = StudentUpdateBirthDateDto(
                field=update_student.field, value=update_student.value
            )
            return update_student_birth_date

        if update_student.field == "tutor_email":
            update_student_email = StudentDtoUpdateEmail(
                field=update_student.field, value=update_student.value
            )
            return update_student_email

        if update_student.field == "cpf_tutor":
            update_student.value = normalize_fields.cpf(update_student.value)
            return update_student

        update_student.value = normalize_fields.string(update_student.value)
        return update_student
