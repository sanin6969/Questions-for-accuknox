from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


@receiver(post_save, sender=UserProfile)
def usr_profile_signal(sender, instance, created, **kwargs):
    if created:
        print(f'UserProfile created: {instance.name}, Email: {instance.email}')
    else:
        print(f'UserProfile updated: {instance.name}, Email: {instance.email}')


if __name__ == '__main__':
    user_profile = UserProfile(name='Alice', email='alice@example.com')
    user_profile.save() 
    user_profile.email = 'alice.new@example.com'
    user_profile.save() 
