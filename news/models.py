from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}"


class NewCategory(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=10000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.category_name + ' ' + str(self.created)


class Source(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class New(models.Model):
    category = models.ForeignKey(NewCategory, on_delete=models.CASCADE, null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=10000, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    recommendation = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title + ' ' + str(self.created)



