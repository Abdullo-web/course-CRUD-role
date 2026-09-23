from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    ROLE = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('editor', 'Editor'),
        ('user', 'User'),
    ]
    
    role = models.CharField(max_length=50,choices=ROLE,default='user')
    
    
    def __str__(self):
        return self.username
    
    
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    cr_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    cr_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,related_name='comments')
    cr_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
