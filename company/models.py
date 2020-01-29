from django.db import models


class Company(models.Model):
    """There should be only one company element!"""
    title = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Company Settings'
        verbose_name_plural = 'Company Settings'
