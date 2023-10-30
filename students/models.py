from django.db import models

# Create your models here.
class Student(models.Model):
  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  field_of_study = models.CharField(max_length=50)
  gpa = models.IntegerField()

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'
