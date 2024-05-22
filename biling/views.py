from rest_framework import permissions
# from rest_framework.viewsets import ModelViewSet


from biling.models import DataCenter, ServiceVPN, Tariff, VirtualMachine, Storage, Network, Orders

from biling.serializers import DataCenterSerializer, ServiceVPNSerializer
from biling.serializers import TariffSerializer, VirtualMachineSerializer
from biling.serializers import StorageSerializer, NetworkSerializer
from biling.serializers import OrdersSerializer
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
# from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from biling.filters import TariffFilterSet
from rest_framework.filters import OrderingFilter
# from django_filters import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

# Погода
import requests


class DataCenterViewSet(ReadOnlyModelViewSet):
    queryset = DataCenter.objects.all().order_by('-id')
    serializer_class = DataCenterSerializer

    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def Weather (self, request, pk):
        datacenter = DataCenter.objects.get(pk=pk)
        api_key = 'aab491a6ee1cff79655de09fbfad94fc'
        params = {'id': datacenter.city_id, 'units': 'metric', 'lang': 'ru', 'appid': api_key}
        res = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)
        # res = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+'Павлодар'+'&units=metric&lang=ru&appid=aab491a6ee1cff79655de09fbfad94fc')


        data = res.json()
        # print("conditions:", data['weather'][0]['description'])
        # print("temp:", data['main']['temp'])
        # print("temp_min:", data['main']['temp_min'])
        # print("temp_max:", data['main']['temp_max'])
        return Response(data)




class ServiceVPNViewSet(ReadOnlyModelViewSet):
    queryset = ServiceVPN.objects.all()
    serializer_class = ServiceVPNSerializer

    permission_classes = [permissions.IsAuthenticated]



class TariffViewSet(ReadOnlyModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer

    filterset_class = TariffFilterSet


    permission_classes = [permissions.IsAuthenticated]

class VirtualMachineViewSet(ReadOnlyModelViewSet):
    queryset = VirtualMachine.objects.all()
    serializer_class = VirtualMachineSerializer

    permission_classes = [permissions.IsAuthenticated]

class StorageViewSet(ReadOnlyModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

    permission_classes = [permissions.IsAuthenticated]


class NetworkViewSet(ReadOnlyModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

    permission_classes = [permissions.IsAuthenticated]

# class OrdersViewSet(CreateModelMixin, UpdateModelMixin, ReadOnlyModelViewSet):

class OrdersViewSet(ModelViewSet):  # Метод переопределен
    # для фильтрации запроса по текущему пользователю
    queryset = Orders.objects.all().order_by('-id')
    serializer_class = OrdersSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        print (self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.validated_data['user'] = (self.request.user)
        super().perform_create(serializer)





# class ProductViewSet(CreateModelMixin, UpdateModelMixin, ReadOnlyModelViewSet):
#     queryset = Product.objects.all().order_by('weight', '-id')
#     # serializer_class = ProductSerializer
#     filterset_class = filters.ProductFilterSet
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.select_related('category', 'registry', 'supplier')
#         qs = qs.filter(master=self.request.auth.get_master())
#         return qs
#
#     def get_serializer_class(self):
#         if getattr(self, 'action') in ['create', 'update', 'partial_update']:
#             return ProductSerializer
#         return ProductFullSerializer
#
#     def perform_create(self, serializer):
#         serializer.validated_data['master'] = self.request.auth.get_master()
#         super().perform_create(serializer)
#
#     def perform_update(self, serializer):
#         print(self.request.data)
#         # Обработка картинок
#         if self.request.data.get('images'):
#             # Сверяем мастера продукта и реестра
#             product = self.get_object()
#             if product.master == product.registry.master:
#                 # Добавляем их в реестр
#                 images = Image.objects.filter(id__in=self.request.data.get('images'))  # Объекты
#                 product.registry.images.add(*images)
#                 if not product.registry.image:
#                     product.registry.image = images.first()
#                     product.registry.save()
#         super().perform_update(serializer)






