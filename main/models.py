from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users_link(models.Model):
    user = models.ForeignKey(User, db_column='username', verbose_name=("User"), on_delete=models.CASCADE)
    long_link = models.TextField('Long link')
    cut_link = models.TextField('Cut link', blank=True)

    def get_absolute_url(self):
        return self.long_link
    

    def __str__(self):
        return f'{self.user} {self.cut_link}'
