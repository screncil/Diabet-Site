from django.db import models
from django.contrib.auth.models import User


class Сarbohydrates(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cur_sugar = models.FloatField(max_length=33.0)
    carbohydrate = models.FloatField()
    cur_time = models.DateTimeField(auto_now_add=True, blank=True)
    
