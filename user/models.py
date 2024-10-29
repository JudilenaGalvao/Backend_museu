from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30,default='')
    bith_date = models.FloatField(default='0')
    email = models.CharField(max_length=20,default='')
    username = models.CharField(max_length=20,default='')
    password = models.CharField(max_length=20,default='')
    role = models.CharField(max_length=20, default='user')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20,default='')
    
    def __str__(self):
        return self.name
