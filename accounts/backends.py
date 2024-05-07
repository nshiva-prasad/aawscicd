from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class EmailOrPhoneBackend(BaseBackend):
    def authenticate(self, request, email_or_phone=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(
                Q(email=email_or_phone) | Q(phone=email_or_phone))
        except user_model.DoesNotExist:
            return None
        if not user.check_password(password):
            return None
        return user
