from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializer import UserSerialzers, UserLoginSerializers
from app.models import User

from rest_framework.authtoken.models import Token

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzers

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializers(data = request.data)

        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data["email"])
                if user.password == serializer.validated_data["password"]:
                    token = Token.objects.get_or_create(user=user)
                    return Response({"success":True, "token":token[0].key})
                else:
                    return Response({"success": False,"message":"incorrect password"})

            except ObjectDoesNotExist:
                return Response({"success":False, "message":"user does not exist"})

class RetrieveUser(generics.RetrieveAPIView):
    pass
        
