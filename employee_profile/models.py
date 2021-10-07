from django.db import models

# Create your models here.
class Users(models.Model):
    full_name = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    dob = models.DateField()
    email = models.EmailField(default=None)
    password = models.CharField(max_length=300)
    status = models.BooleanField(default=True, help_text="True: Active, False: Inactive")

    def __str__(self):
        return f"{self.username} ({self.full_name}), dob {self.dob}"

