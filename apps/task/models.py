from django.db import models
from apps.users.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField('Новое задания', max_length=555)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
