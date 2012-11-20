from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models


class UserProfile(models.Model):
    '''
    User profile for users.
    '''
    user = models.OneToOneField('auth.User')

    def __unicode__(self):
        return '%s\'s profile.' % self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
