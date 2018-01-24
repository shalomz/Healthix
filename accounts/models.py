from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



def user_directory_path(instance, filename):
    # image will be uploaded to MEDIA_ROOT/<username>/profile/<filename>
    return 'users/{0}/profile/{1}'.format(instance.user.username, filename)

DEPARTMENTS = (
    ('Reception', 'Reception'),
    ('Consultation', 'Consultation'),
    ('Triage', 'Triage'),
    ('Lab', 'Lab'),
    ('Theatre', 'Theatre'),
    ('Ward', 'Ward')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return 'Profile'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


    #  group = request.user.groups.get(user=request.user)