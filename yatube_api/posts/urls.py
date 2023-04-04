from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet
from rest_framework import routers


router = routers.DefaultRouter()


router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comment')
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet)

urlpatterns = [
]