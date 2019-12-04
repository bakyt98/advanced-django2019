from django.conf import settings
from django.db import models
from utils.constants import (PRIORITY, MEDIUM, PROJECT_TYPES, SOFTWARE,
                            BLOCK_TYPES, NEW)
from utils.file_utils import validate_image_size


class ProjectManager(models.Manager):
    def get_projects(self, project_type):
        return Project.objects.filter(project_type=project_type)

    def get_null_descriptions(self):
        return Project.objects.filter(description__isnull=True)

    def get_users_projects(self, users):
        return Project.objects.filter(creator__in=users)

    def get_type_projects(self, types):
        return Project.objects.filter(project_type__in=types)


class Project(models.Model):
    """
    Project model keeps info about each project.
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    project_type = models.CharField(max_length=100, choices=PROJECT_TYPES,
                                    default=SOFTWARE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    objects = ProjectManager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f'{self.name} {self.creator}'

    @classmethod
    def own_projects(cls, user_id):
        return cls.objects.filter(creator_id=user_id)

    @property
    def get_short_desc(self):
        return self.description[:200]


class ProjectMember(models.Model):
    """
    ManyToMany relationship between user and project models.
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return f'{self.project} {self.user}'


class Block(models.Model):
    """
    Black model for project.
    """
    name = models.CharField(max_length=100)
    block_type = models.IntegerField(choices=BLOCK_TYPES, default=NEW)
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
                                 on_delete=models.SET_NULL,
                                 related_name='executor',
                                 blank=True, null=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    priority = models.CharField(max_length=100, choices=PRIORITY, default=MEDIUM)
    order = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.executor}'

    @classmethod
    def get_task_by_block(cls, block_id):
        return cls.objects.filter(block_id=block_id)


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.task} {self.body}'


class TaskDocument(models.Model):
    document = models.FileField(upload_to='files/', validators=[validate_image_size])
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.document.path} {self.creator}'
