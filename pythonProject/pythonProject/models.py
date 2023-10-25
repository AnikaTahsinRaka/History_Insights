from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
class Review(models.Model):
    Task_id = models.AutoField
    Rating = models.CharField(max_length=200)
    Msg = models.CharField(max_length=200)
    Created = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(
        HeritageDetails, on_delete=models.CASCADE, null=True, blank=True)
class SignUp(models.Model):
    User_id = models.AutoField
    FullName = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class Signin(models.Model):
    User_id = models.AutoField
    UserName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
class Contact(models.Model):
    User_id = models.AutoField
    UserName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Message = models.TextField()


class UserProfile(models.Model):
    GENRE_CHOICES = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    full_name = models.CharField(max_length=50)
    # Email = models.CharField(max_length=100)
    image = models.ImageField()



class Task(models.Model):
    Task_id = models.AutoField
    Title = models.CharField(max_length=200, null=True)
    Complete = models.BooleanField(null=True, blank=True)
    Created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'

