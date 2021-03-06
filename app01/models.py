from django.db import models

class Classes(models.Model):
    '''
    班级表
    '''
    title = models.CharField(max_length=32)
    t = models.ManyToManyField("Teachers")

class Teachers(models.Model):
    '''
    教师表
    '''
    name = models.CharField(max_length=32)

class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes, on_delete=models.CASCADE)
