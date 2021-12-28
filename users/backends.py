from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if "@" in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = get_user_model().objects.get(**kwargs)
        except get_user_model().DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None
