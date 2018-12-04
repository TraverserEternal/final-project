from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from project.base.apps.calculations.models.data import Data
from project.api.sessions.serializers import SessionSerializer, CalculatedDataSerializer
from project.base.apps.trackers.models import Session

User = get_user_model()


class DataSend(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = SessionSerializer
    queryset = Session.objects.all()


class SessionListView(ListAPIView):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(team__user=self.request.user)


class ParticularSession(RetrieveAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        return Session.objects.filter(team__user=self.request.user)


class LoadSessionData(GenericAPIView):
    queryset = Session.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(team__user=self.request.user)

    def post(self, request, **kwargs):
        session = self.get_object()
        try:
            session.load_data()
        except Exception as e:
            return Response({
                'details': e.message,
            }, 400)
        return Response({
            'details': 'Loading in progress!',
        })


class CalculateSession(GenericAPIView):
    queryset = Session.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(team__user=self.request.user)

    def post(self, request, **kwargs):
        session = self.get_object()
        try:
            session.calculate_data()
        except Exception as e:
            return Response({
                'details': e.message,
            }, 400)
        return Response({
            'details': 'Calculation in progress!',
        })


class CalculatePowerCategoriesSession(GenericAPIView):
    queryset = Session.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(team__user=self.request.user)

    def post(self, request, **kwargs):
        session = self.get_object()
        try:
            session.calculate_power_categories()
        except Exception as e:
            return Response({
                'details': e.message,
            }, 400)
        return Response({
            'details': 'Calculation in progress!',
        })


class GetDataFromSession(GenericAPIView):
    serializer_class = CalculatedDataSerializer
    queryset = Data.objects.all()

    def get(self, request, **kwargs):
        qs = self.queryset.filter(session_id=self.kwargs.get('pk'))
        return Response(self.serializer_class(qs, many=True).data)
