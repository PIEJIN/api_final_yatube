from rest_framework import mixins, viewsets


class CreateListViewSetMixin(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass
