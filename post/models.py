from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    file = models.FileField(upload_to='uploads/')
    user_id = models.ForeignKey('user.User',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20,default='')
    
    
    def __str__(self):
        return self.title
