from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import UserAccountSerializer
from .models import UserAccount


class UserAccountViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    def get_queryset(self):
        qs = UserAccount.objects.all()
        activity = self.request.query_params.get('activity', None)
        if activity is not None:
            qs = qs.filter(activities__name=activity)
        return qs
