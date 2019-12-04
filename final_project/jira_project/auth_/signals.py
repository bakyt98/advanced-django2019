from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import MainUser, Profile
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=MainUser)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_id=instance.id)


@receiver(post_delete, sender=Profile)
def deleted_profile(sender, instance, **kwargs):
    try:
        MainUser.objects.get(id=instance.user.id).delete()
    except Exception as e:
        logger.error('errrrroooorrr!!!')
