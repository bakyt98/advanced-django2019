from rest_framework import serializers

from auth_.models import MainUser
from auth_.serializers import MainUserSerializer
from core.models import (Project, Block, Task, TaskComment, ProjectMember,
                         TaskDocument)
from utils.constants import BLOCK_TYPES, PRIORITY
import logging

logger = logging.getLogger(__name__)


class ProjectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'project_type')


class ProjectSerializer(ProjectShortSerializer):
    creator = MainUserSerializer(read_only=True)
    class Meta(ProjectShortSerializer.Meta):
        fields = ProjectShortSerializer.Meta.fields + ('description', 'creator')

    def create(self, validated_data):
        logger.info('start creation of project')
        project = Project.objects.create(**validated_data)
        logger.info('end of project creation ')
        return project


class BlockShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('id', 'name', 'block_type')

    def validate_block_type(self, value):
        if value not in BLOCK_TYPES:
            raise serializers.ValidationError('block_type is not correct')
        return value


class BlockSerializer(BlockShortSerializer):
    class Meta(BlockShortSerializer.Meta):
        fields = BlockShortSerializer.Meta.fields + ('project',)
        depth = 2


class TaskShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'block', 'order')

    def validate_order(self, value):
        if value > 0:
            raise serializers.ValidationError('order cannot be less than 0')
        return value


class TaskSerializer(TaskShortSerializer):
    creator = MainUserSerializer(read_only=True)
    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('description', 'creator', 'executor', 'priority')

    def validate_priority(self, value):
        if value not in PRIORITY:
            raise serializers.ValidationError('there is no such priority')
        return value


class GetBlockSerializer(serializers.Serializer):
    prj_id = serializers.IntegerField()

    def get(self):
        blocks = Block.objects.filter(project_id=self.validated_data['prj_id'])
        return blocks


class CreateBlockSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    block_type = serializers.IntegerField()
    project_id = serializers.IntegerField()

    def create(self):
        block = Block.objects.create(
            name=self.validated_data['name'],
            block_type=self.validated_data['block_type'],
            project_id=self.validated_data['project_id'])
        return block


class ProjectMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectMember
        fields = '__all__'

    def create(self, validated_data):
        return ProjectMember.objects.create(**validated_data)


class TaskDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDocument
        fields = '__all__'
        read_only_fields = ('creator', )


class TaskCommentShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('id', 'task', 'body')

    def validate_body(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('body should not be more than 200 symbols')
        return value


class TaskCommentSerializer(TaskCommentShortSerializer):
    creator = MainUserSerializer(read_only=True)

    class Meta(TaskCommentShortSerializer.Meta):
        fields = TaskCommentShortSerializer.Meta.fields + ('creator', 'created_at')
