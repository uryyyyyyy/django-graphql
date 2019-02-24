import json

from django.http import HttpResponse, HttpRequest
from django.views import View

from apps.django_user.models import User


class LoginView(View):
    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")
        if not email or not password:
            return HttpResponse(status=400, content="you should set email, password")
        user = User.objects.get_by_natural_key(email)
        if not user or not user.check_password(password):
            return HttpResponse(status=400, content="email or password invalid")
        print("login success")
        return HttpResponse('login success')
