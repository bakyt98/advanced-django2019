from rest_framework import viewsets, status, generics, mixins
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Project, Block, Task, TaskComment, ProjectMember, TaskDocument
from core.serializers import (ProjectSerializer, BlockSerializer,
                              TaskSerializer, CreateBlockSerializer,
                              GetBlockSerializer, ProjectShortSerializer,
                              ProjectMemberSerializer, BlockShortSerializer,
                              TaskShortSerializer, TaskDocumentSerializer,
                              TaskCommentShortSerializer, TaskCommentSerializer)


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Project.own_projects(self.request.user.id)
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectShortSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ProjectMemberAPIView(APIView):
    http_method_names = ['post', 'get']
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProjectMemberSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        projects = self.request.user.projects.all()
        serializer = ProjectMemberSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectMemberViewSet(viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin,
                           viewsets.mixins.ListModelMixin):
    queryset = ProjectMember.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ProjectMemberSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskShortSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)

    def filter_queryset(self, queryset):
        if self.action == 'list':
            return queryset.filter(block_id=self.request.query_params['block_id'],
                                   creator=self.request.user)
        return queryset.filter(creator=self.request.user)


class BlockAPIView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = GetBlockSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        blocks = serializer.get()
        serializer_b = BlockShortSerializer(blocks, many=True)
        return Response(serializer_b.data)

    def post(self, request):
        serializer = CreateBlockSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        block = serializer.create()
        return Response(BlockSerializer(block).data)


class TaskDocumentViewSet(viewsets.ModelViewSet):
    queryset = TaskDocument.objects.all()
    serializer_class = TaskDocumentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)


class TaskCommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskCommentSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskCommentShortSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)
