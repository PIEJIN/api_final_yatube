from rest_framework import mixins, viewsets


class PostGetViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    pass
