from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin)
from django.conf import settings
from django.db import models

class MainUserManager(BaseUserManager):
    """
    MainUser manager for MainUser model.
    """

    def create_user(self, login, password):
        if not login or not password:
            raise ValueError('User must have login and password.')
        user = self.model(login=login)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password):
        user = self.create_user(login, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_moderator = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def count_active(self):
        return MainUser.objects.filter(is_active=True).count()

    def get_staffs(self):
        return MainUser.objects.filter(is_staff=True)


class MainUser(AbstractBaseUser, PermissionsMixin):
    """
    MainUser model for user.
    """
    login = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = MainUserManager()
    USERNAME_FIELD = 'login'

    def __str__(self):
        return f'{self.name} {self.login}'


class Profile(models.Model):
    """
    Profile model for holding data about certain user.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="profile",
                                on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    web_site = models.URLField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'{self.user}: {self.bio}'
