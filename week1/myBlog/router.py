from article.views import ArticleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('article', ArticleViewSet)
