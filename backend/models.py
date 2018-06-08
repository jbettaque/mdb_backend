from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    friends = models.ManyToManyField("User")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __unicode__(self):
        return self.username



class Room(models.Model):
    name = models.CharField(max_length=50)
    join_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField("User", related_name="all_users")
    active_user = models.ManyToManyField("User", related_name="active_users")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class MenuEntry(models.Model):
    text = models.CharField(max_length=50)
    link = models.URLField
    target = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text
