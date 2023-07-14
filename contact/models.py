from django.db import models


class Contact(models.Model):
    full_name = models.TextField(max_length=40)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15)
    message = models.TextField(max_length=300)


    def __str__(self):
        return self.full_name