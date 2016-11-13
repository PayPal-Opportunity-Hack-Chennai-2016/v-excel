from rest_framework import viewsets, routers

from service_and_process.models import MasterService
from service_and_process.models import MasterProduct
from service_and_process.models import MasterProcess
from service_and_process.models import MappingProductServicesProcess
from service_and_process.models import MasterWorkable

from service_and_process.serializers import MasterProcessSerializer
from service_and_process.serializers import MasterProductSerializer
from service_and_process.serializers import MasterServiceSerializer
from service_and_process.serializers import MappingProductServicesProcessSerializer
from service_and_process.serializers import MasterWorkableSerializer


class MasterWorkableViewset(viewsets.ModelViewSet):
    queryset = MasterWorkable.objects.all()
    serializer_class = MasterWorkableSerializer
    filter_fields = ('category', 'label')


class MasterServiceViewset(viewsets.ModelViewSet):
    queryset = MasterService.objects.all()
    serializer_class = MasterServiceSerializer
    filter_fields = ('workable__id', 'workable__category', 'workable__label', 'label', 'price', 'tax')


class MasterProductViewset(viewsets.ModelViewSet):
    queryset = MasterProduct.objects.all()
    serializer_class = MasterProductSerializer


class MasterProcessViewset(viewsets.ModelViewSet):
    queryset = MasterProcess.objects.all()
    serializer_class = MasterProcessSerializer


class MappingProductServicesProcessViewset(viewsets.ModelViewSet):
    queryset = MappingProductServicesProcess.objects.all()
    serializer_class = MappingProductServicesProcessSerializer
