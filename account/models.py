from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def does_exits(self):
        return Customer.objects.filter(email=self.email)    