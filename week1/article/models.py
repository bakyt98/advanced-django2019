from django.contrib import auth
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=64)
    rating = models.fields.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True)
    summary = models.CharField(max_length=10000, null=True, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    submission_date = models.DateField(null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE,
                                null=True, blank=True)
    reviewer = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                                 null=True, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.id, self.title)
