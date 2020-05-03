from .serializers import OptionRawDataSerializer
from .models import OptionRawDataModel
from rest_framework import viewsets
from rest_framework import permissions


class OptionRawDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OptionRawDataModel.objects.all()
    serializer_class = OptionRawDataSerializer
    permission_classes = [permissions.IsAuthenticated]


class CMEOptionRawDataViewSet(OptionRawDataViewSet):
    queryset = OptionRawDataModel.objects.filter(
        exchange__exact='CME'
    )


class EUREXOptionRawDataViewSet(OptionRawDataViewSet):
    queryset = OptionRawDataModel.objects.filter(
        exchange__exact='EUREX'
    )


class ICEOptionRawDataViewSet(OptionRawDataViewSet):
    queryset = OptionRawDataModel.objects.filter(
        exchange__exact='ICE'
    )


class USETFOptionRawDataViewSet(OptionRawDataViewSet):
    queryset = OptionRawDataModel.objects.filter(
        exchange__exact='USETF'
    )

