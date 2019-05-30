from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Advert (models.Model):
    name = models.CharField(
        max_length = 230
    )
    content = models.TextField()

    user = models.ForeignKey(to = User,on_delete = models.CASCADE)
    is_public = models.BooleanField(default = True)
    date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Advert "
        verbose_name_plural = "Advert "

