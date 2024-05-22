from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework import generics, views, status
from rest_framework.response import Response

from authorization.models import User
from authorization.serializers import LoginSerializer, RegistrationSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework.mixins import CreateModelMixin, UpdateModelMixin

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from rest_framework import permissions
from authorization.permissions import CustomUpdatePermission

# registration
class RegistrationView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    # def create(self, request, *args, **kwargs):
    #     request.data['password'] = make_password(request.data['password'])
        # return super().create(request, *args, **kwargs)

    # def perform_create(self, request, *args, **kwargs):
    #     request.data['password'] = make_password(request.data['password'])
    #     return super().create(request, *args, **kwargs)


    def perform_create(self, serializer):
        serializer.validated_data['password'] = make_password(self.request.data['password'])
        super().perform_create(serializer)


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)







# login
class LoginView(generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"detail": "Logged in!"})
        return Response({"detail": "Неверный логин и пароль"})


# logout
class LogoutView(generics.GenericAPIView):

    def get(self, request):
        logout(request)
        return Response({"detail": "Logged out!"})


# Нужна проверка кода ниже

class UserViewSet(UpdateModelMixin, ReadOnlyModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [CustomUpdatePermission, permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated,CustomUpdatePermission]
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(id=self.request.user.id)
        print (self.request.user)
        return qs




# class UpdateView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UpdateSerializer
#     def get(self, request):
#         user = User._do_update(request.user)
#         return Response({"detail": "Юзер обновлен"})
