from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, password, role=3):
        user = self.model(username=username)
        user.set_password(password)
        user.role = role
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password, role=1)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

    # ниже код вставки посредством PyCharm
    # def delete_superuser(self, username, password):
    #     user = self.delete_user(username=username, password=password, role=1)
    #     user.is_superuser = True
    #     user.is_staff = True
    #
    #     user.save(using=self._db)
    #
    #     return user

    def update_user(self, username):
        user = self.retrieve_user(username)
        user.is_superuser = False
        user.is_staff = True
        user.update(using=self._db)
        return user


    def retrieve_user(self, username):
        user = self.retrieve_user(username)
        user.is_superuser = False
        user.is_staff = True
        user.retrieve(using=self._db)
        return user

    def delete_user(self, username, password):
        user = self.delete_user(username=username)
        user.is_superuser = False
        user.is_staff = True
        user.delete(using=self._db)
        return user