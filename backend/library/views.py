from rest_framework import mixins, viewsets

from rest_framework.pagination import LimitOffsetPagination

from .models import User
from .serializers import UserSerializer, UserSerializerV2


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    filterset_fields = ['username']
    pagination_class = UserLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserSerializerV2
        return UserSerializer
