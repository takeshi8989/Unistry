from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(default='default_school.png', upload_to='static/school_images')

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default_profile.png', upload_to='static/user_images')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Event(models.Model):
    title = models.CharField(max_length=100)
    organizers = models.ManyToManyField(Profile, related_name='event_organizers')
    members = models.ManyToManyField(Profile, related_name='event_members', blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # min, max

class Team(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    members = models.ManyToManyField(Profile, blank=True)
    # link

class Chat(models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE, null=True, blank=True)
    event = models.OneToOneField(Event, on_delete=models.CASCADE, null=True, blank=True)
    team = models.OneToOneField(Team, on_delete=models.CASCADE, null=True, blank=True)
    is_public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(Profile, blank=True)
    # image

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    content = models.TextField()
    sent_time = models.DateField(auto_now_add=True)