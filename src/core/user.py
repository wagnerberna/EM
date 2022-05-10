from src.utils.normalize import NormalizeFields
from src.utils.passwords import crypt_password
from src.model.dto.user_dto import UserAddDto

normalize_fields = NormalizeFields()


class UserCore:
    def payload_new_user(self, user):

        payload = UserAddDto(
            name=normalize_fields.string(user.name),
            login=normalize_fields.string(user.login),
            password=crypt_password(user.password),
        )
        return payload

    def payload_update_user(self, update_user):
        if update_user.field == "password":
            update_user.value = crypt_password(update_user.value)
            return update_user

        update_user.value = normalize_fields.string(update_user.value)
        return update_user
