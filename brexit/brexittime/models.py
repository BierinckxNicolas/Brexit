from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Clock(models.Model):    
    clock_time = models.DateTimeField(auto_now_add= True)
    timediff = models.DateTimeField()
    def __str__(self):
        return self.timediff
    def time_left_till_brexit(self):
        if self.clock_time:
         brexit_time = datetime.datetime(2019, 3, 29, 23, 0, 0)
         timediff = brexit_time - self.clock_time
        return timediff