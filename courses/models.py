from django.db import models
from django.contrib.auth.models import User

#class subject
class Subjects(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True)
    
    class Meta:
        ordering=['name']
    def __str__(self):
         return self.name
            
#class course      
class Course(models.Model):
    owner = models.ForeignKey(User,related_name='courses_created',on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects,related_name='courses',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    
#class Module    
class Module(models.Model):
    course= models.ForeignKey(Course,related_name='modules', on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    description=models.TextField(blank=True)
    
    def __str__(self):
        return self.title