from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    name = models.CharField(max_length=200)
    notes = models.TextField()
    category = models.ForeignKey(Category, 
        related_name='sauce', on_delete=models.CASCADE
        )