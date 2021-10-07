from django.db import models


# Create your models here.
class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    headline = models.CharField(max_length=300)
    name = models.CharField(max_length=30)
    summary = models.CharField(max_length=400)
    author = models.CharField(max_length=400)
    pub_date = models.DateField()
    mod_date = models.DateField()
