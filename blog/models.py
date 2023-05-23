from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone

from blog.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    SUPERADMIN, EDITOR, READER = range(1, 4)
    ROLE_TYPES = (
        (SUPERADMIN, 'Суперпользователь'),
        (EDITOR, 'Новостной редактор'),
        (READER, 'Читатель')
    )

    objects = UserManager()

    id = models.AutoField(primary_key=True)
    username = models.CharField('Логин', max_length=50, default='', unique=True)
    first_name = models.CharField("ФИО", max_length=100, default='', blank=True, null=True)
    email = models.EmailField("Почта", default="email@mail.com", blank=True, null=True)
    date_joined = models.DateTimeField("Дата присоединения", blank=True, null=True, default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Статус доступа',
    )
    role = models.IntegerField('Роль', default=READER, choices=ROLE_TYPES)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

# Create your models here.
