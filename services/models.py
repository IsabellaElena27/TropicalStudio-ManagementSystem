from django.db import models
from employee.models import Employee
from django.contrib.auth.models import User


class Service(models.Model):
    name_of_service = models.TextField(max_length=200)
    price = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_of_service


STATUS = (
    ('draft', 'draft'),
    ('completed', 'completed')
)


class RezervareServicii(models.Model):
    id_service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    id_user = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=9, default='draft')
    date = models.DateTimeField(null=True)
