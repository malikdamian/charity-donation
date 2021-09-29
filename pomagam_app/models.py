from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


TYPES = (
    (1, "Fundacja"),
    (2, "Organizacja pozarządowa"),
    (3, "Zbiórka lokalna"),
    (4, "Domyślnie fundacja")

)


class Institution(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=12)
    pick_up_date = models.CharField(max_length=12)
    pick_up_time = models.CharField(max_length=6)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.address}, liczna worków: {self.quantity}"
