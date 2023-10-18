from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)


    #special method
    def __str__(self):
        return self.name

class  Student(models.Model):
    name =models.CharField(max_length=256)
    age= models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='student', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
