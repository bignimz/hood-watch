from unicodedata import category, name
from django.contrib.auth.models import AbstractUser
from django.db import models


# EXtending the default Django User attributes
class User(AbstractUser):
    is_controller = models.BooleanField(default=False)
    is_elder = models.BooleanField(default=False)
    is_resident = models.BooleanField(default=False)


class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='neighborhoods/', default="/default.jpg")
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Elder(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    bio = models.TextField()
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, blank=True)


class Resident(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='profiles/', default="/default.jpg")
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    bio = models.TextField()
    neighbourhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)


class Controller(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    bio = models.TextField()
    neighbourhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)


class Post(models.Model):
    image = models.ImageField(upload_to='posts/', default="/default.jpg")
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='business/', default="/default.jpg")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
