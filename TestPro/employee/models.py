from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    desc=models.TextField()
    
    def __str__(self):
        return f"{self.email}"
