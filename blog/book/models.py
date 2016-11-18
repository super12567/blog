from django.db import models


class Book(models.Model):
    titles = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=128,)
    publisher = models.CharField(max_length=128)
    publicationdate = models.DateField()
    printversion = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.titles