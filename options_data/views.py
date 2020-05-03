from .serializers import OptionRawDataSerializer
from .models import OptionRawDataModel
from rest_framework import viewsets
from rest_framework import permissions


class OptionRawDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OptionRawDataModel.objects.all()
    serializer_class = OptionRawDataSerializer
    permission_classes = [permissions.IsAuthenticated]


class CMEOptionRawDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OptionRawDataModel.objects.filter(
        exchange__exact='CME'
    )
    serializer_class = OptionRawDataSerializer
    permission_classes = [permissions.IsAuthenticated]


class EUREXOptionRawDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OptionRawDataModel.objects.filter(
        exchange__exact='EUREX'
    )
    serializer_class = OptionRawDataSerializer
    permission_classes = [permissions.IsAuthenticated]


class ICEOptionRawDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OptionRawDataModel.objects.filter(
        exchange__exact='ICE'
    )
    serializer_class = OptionRawDataSerializer
    permission_classes = [permissions.IsAuthenticated]


class USETFOptionRawDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OptionRawDataModel.objects.filter(
        exchange__exact='USETF'
    )
    serializer_class = OptionRawDataSerializer
    permission_classes = [permissions.IsAuthenticated]

