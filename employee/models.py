from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    description = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
