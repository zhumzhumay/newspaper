from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone

from blog.managers import UserManager
from django.utils.translation import gettext as _


class User(AbstractBaseUser, PermissionsMixin):
    SUPERADMIN, EDITOR, READER = range(1, 4)
    ROLE_TYPES = (
        (SUPERADMIN, _('Суперпользователь')),
        (EDITOR, _('Новостной редактор')),
        (READER, _('Читатель'))
    )

    objects = UserManager()

    id = models.AutoField(primary_key=True)
    username = models.CharField(_('Логин'), max_length=50, default='', unique=True)
    first_name = models.CharField(_("ФИО"), max_length=100, default='', blank=True, null=True)
    email = models.EmailField(_("Почта"), default="email@mail.com", blank=True, null=True)
    date_joined = models.DateTimeField(_("Дата присоединения"), blank=True, null=True, default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Статус доступа'),
    )
    role = models.IntegerField(_('Роль'), default=READER, choices=ROLE_TYPES)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


class Post(models.Model):
    URGENT, BESTOFTHEDAY, REGULAR= range(1, 4)
    NEWS_TYPES = (
        (URGENT, _('СРОЧНАЯ НОВОСТЬ')),
        (BESTOFTHEDAY, _('НОВОСТЬ ДНЯ')),
        (REGULAR, _('ОБЫЧНАЯ'))
    )

    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, verbose_name=_('Пользователь'), related_name='posts', default=0)
    image = models.ImageField(_('Изображение'), default='service-6.jpg')
    title = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name=_('Заголовок'))
    text = models.TextField(verbose_name=_("Текст"))
    text_author = models.CharField(_('Автор статьи'), max_length=255, default="")
    date_post = models.DateTimeField(default=timezone.now, verbose_name=_("дата"))

    type = models.IntegerField(_('Тип новости'), default=REGULAR, choices=NEWS_TYPES)
    

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')
        
    def __str__(self):
        return self.title

    def get_absolute_image_url(self):
        if self.image:
            return self.image.url
        else:
            return ''
    
    
# class Sessions(models.Model):
#         user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'), related_name='sessions', default=0)
#         tokenaccess = models.TextField(verbose_name="токен доступа")
#         tokenrefresh = models.TextField('Токен рефреш')
#         date = models.DateTimeField(default=timezone.now, verbose_name="дата")

