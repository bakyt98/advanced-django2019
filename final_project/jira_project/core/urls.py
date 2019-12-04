from django.urls import path, include
from rest_framework import routers

from core.views import (TaskViewSet, ProjectViewSet, BlockAPIView, ProjectMemberAPIView,
                        TaskDocumentViewSet, TaskCommentViewSet, ProjectMemberViewSet)

router = routers.DefaultRouter()
router.register('task', TaskViewSet, base_name='core')
router.register('project', ProjectViewSet, base_name='core')
router.register('task_document', TaskDocumentViewSet, base_name='core')
router.register('task_comment', TaskCommentViewSet, base_name='core')
router.register('project_users', ProjectMemberViewSet, base_name="core")

urlpatterns = [
    path('', include(router.urls)),
    path('blocks/', BlockAPIView.as_view()),
    path('project_member/', ProjectMemberAPIView.as_view())
]
