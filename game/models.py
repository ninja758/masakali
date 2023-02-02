from django.db import models
from accounts.models import User
import jsonfield

# Create your models here.
class event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    response = jsonfield.JSONField()
    investedChips = models.IntegerField()
    serverRandomizer = models.IntegerField
    result = models. BooleanField()


class transaction(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fromUser')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='toUser')
    timestamp = models.DateTimeField(auto_now_add=True)
    token = models.IntegerField

