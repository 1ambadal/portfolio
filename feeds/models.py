from django.db import models

from django.db import models
from ckeditor.fields import RichTextField

class PersonalInformation(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/', null=True)
    mini_about = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    # Social Network
    mycv = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_complete


class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)
    description2 = models.TextField(blank=False, null=True)
    about_avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    skill = models.TextField(max_length=230, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image  = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    medium = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(upload_to= 'images/',null = True)

    def __str__(self):
        return self.skill


class Blogs(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to= 'images/',null = True)
    url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title