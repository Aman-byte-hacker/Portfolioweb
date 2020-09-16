from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=20)
    subject=models.TextField(max_length=2000)

    def __str__(self):
        return self.firstname
    