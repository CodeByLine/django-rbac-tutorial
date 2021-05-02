# rbac/core/auth.py
import typing

from rbac.core.models import User
from rbac.core import services


class CheckPasswordBackend:
    def authenticate(
        self, request=None, email=None, password=None
    ) -> typing.Optional[User]:
        user = services.find_user_by_email(email=email)

        if user is None:
            return None

        return user if user.check_password(password) else None

    def get_user(self, user_id) -> typing.Optional[User]:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
