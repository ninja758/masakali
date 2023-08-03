from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class event(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField
    end_time = models.DateTimeField
    result = models.IntegerField(default=0)

class event_participation_record(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invested_money = models.JSONField
    user_benefit = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

class user_transaction(models.Model):
    id = models.AutoField(primary_key=True)
    from_user = models.ForeignKey(User,related_name='transaction_from', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='transaction_to',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)

