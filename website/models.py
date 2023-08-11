from django.db import models

# Create your models here.


class Record (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    industry = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
