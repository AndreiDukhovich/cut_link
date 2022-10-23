from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users_link(models.Model):
    user = models.ForeignKey(User, db_column='username', verbose_name=("User"), on_delete=models.CASCADE)
    name = models.CharField('Site name', max_length=50)
    long_link = models.URLField('Long link')
    cut_link = models.URLField('Cut link', blank=True)
    qr = models.ImageField()

    def get_absolute_url(self):
        return self.long_link
    

    def __str__(self):
        return f'{self.user} {self.cut_link}'
