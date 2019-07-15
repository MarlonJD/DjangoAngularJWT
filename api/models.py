from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class BlogPost(models.Model):
    """
    The "BlogPost" model for the micro blog app
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(
        default=timezone.now
    )
    body = models.CharField(default='', max_length=200)

    def __str__(self):
        return self.body
