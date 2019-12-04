from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Project, Block, TaskDocument
from utils import constants
import logging
import os

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Project)
def project_post_save(sender, instance, created, **kwargs):
    if created:
        logger.info('create blocks to project')
        Block.objects.create(
            name="TO DO", block_type=constants.TODO, project=instance
        )
        Block.objects.create(
            name="In progress", block_type=constants.INPROGRESS, project=instance
        )
        Block.objects.create(
            name="Done", block_type=constants.DONE, project=instance
        )
        logger.info('end creation of blocks')


@receiver(post_delete, sender=TaskDocument)
def tas_post_del(sender, instance, **kwargs):
    try:
        if instance.document:
             if os.path.isfile(instance.document.path):
                os.remove(instance.document.path)
    except Exception as e:
        logger.error(e)
