from src.utils.normalize import NormalizeFields
from src.model.dto.grade_grid_dto import (
    GradeGridAddDto,
    GradeGridUpdateDto,
    GradeGridUpdateByStudentYearDto,
)

normalize_fields = NormalizeFields()


class GradeGridCore:
    def payload_add(self, data):
        payload = GradeGridAddDto(
            student_id=data.student_id,
            year=data.year,
            portuguese=round(data.portuguese, 1),
            mathematics=round(data.mathematics, 1),
            biology=round(data.biology, 1),
            geography=round(data.geography, 1),
            history=round(data.history, 1),
        )
        return payload

    def payload_update(self, data):
        payload = GradeGridUpdateDto(
            subject=data.subject,
            scored=round(data.scored, 1),
        )
        return payload

    def payload_update_by_student_year(self, data):
        payload = GradeGridUpdateByStudentYearDto(
            student_id=data.student_id,
            year=data.year,
            subject=data.subject,
            scored=round(data.scored, 1),
        )
        return payload
