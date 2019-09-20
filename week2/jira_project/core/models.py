from django.conf import settings
from django.db import models
from utils.constants import PRIORITY, MEDIUM


class Project(models.Model):
    """
    Project model keeps info about each project.
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    project_type = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.creator}'


class ProjectMember(models.Model):
    """
    ManyToMany relationship between user and project models.
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project} {self.user}'


class Block(models.Model):
    """
    Black model for project.
    """
    name = models.CharField(max_length=100)
    block_type = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.project}'


class Task(models.Model):
    """
    Task model which holds tasks of each block.
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='creator')
    executor = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='executor')
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    priority = models.CharField(max_length=100, choices=PRIORITY, default=MEDIUM)
    order = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.executor}'


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.task} {self.body}'


class TaskDocument(models.Model):
    document = models.FileField(upload_to='files/')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.document.path} {self.creator}'
