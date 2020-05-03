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

    def get_queryset(self):
        """
        instead of defining a queryset which may or may not implement
        filtering it is possible to use dynamic filtering by overwriting the
        `get_queryset` method.

        Access query parameters:

            from rest_framework import generics
            class SomeView(generics.ListAPIView):
                def get_queryset(self)
                    username = self.request.query_params.get('username', None)
                    queryset = ModelOfSomeView.filter(username__exact=username)
                    return queryset

        Access via URL element:
            # urls.py
            url('^purchases/(?P<username>.+)/$', SomeView),

            # views.py
            from rest_framework import generics
            class SomeView(generics.ListAPIView):
                def get_queryset(self)
                    username = self.kwarg['username']
                    return ModelOfSomeView.filter(username__exact=username)

        query parameter is designed to be optional (hence the .get() method)
        Whereas the URL segment is expected to be certainly present (hence the ['key'] access)

        also: django_filters package
        """
        queryset = OptionRawDataModel.objects.filter(
            exchange__exact='USETF'
        )
        return queryset
