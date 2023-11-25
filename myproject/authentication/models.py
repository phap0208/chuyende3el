
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)  # Define the ImageField

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Lesson'
class Test(models.Model):
    Lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255)
    description = RichTextUploadingField(null=True, blank=True)
    # start_time = models.DateTimeField(null=True, blank=True)
    # end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    choice_1 = models.CharField(max_length=255, default='')
    choice_2 = models.CharField(max_length=255, default='')
    choice_3 = models.CharField(max_length=255, default='')
    choice_4 = models.CharField(max_length=255, default='')
    correct_choice = models.CharField(max_length=1, null=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])

    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # Add other fields as needed for your user profiles

    def __str__(self):
        return self.user.username + "'s Profile"



# @receiver(post_save, sender=get_user_model())
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=get_user_model())
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

# @receiver(post_save, sender=get_user_model())
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         profile = Profile.objects.create(user=instance)
#         # Add additional information to the profile
#         profile.bio = "here"
#         profile.profile_picture = "1.jpg"
#         profile.save()
#

