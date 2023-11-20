from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyCustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('is_staff must be True')
        if not extra_fields.get('is_superuser'):
            raise ValueError('is_superuser must be True')

        if not extra_fields.get('is_active'):
            raise ValueError('is_active must be True')
        return self.create_user(email, password, **extra_fields)


class MyCustomUserModel(AbstractBaseUser):
    GENDER = (
        (1, 'male'),
        (2, 'female')
    )
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=150, null=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.IntegerField(choices=GENDER)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender']

    objects = MyCustomUserManager()

    def str(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
