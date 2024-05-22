import django_filters
from django.db.models import Q
from django_filters.rest_framework import FilterSet

from biling.models import Tariff
from django_filters.filters import OrderingFilter

# from biling.models import DataCenter, ServiceVPN, Tariff, VirtualMachine, Storage, Network, Orders


class TariffFilterSet(FilterSet):
    class Meta:
        model = Tariff
        fields = ('id','name','description','price',
                  'data_center', 'service_vpn', 'virtual_machine',
                  'storage', 'network')

    search = django_filters.CharFilter(method='search_by')


    ordering = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('price', 'price'),
            ('name', 'name'),
            ('id', 'id'),
        ),

    )

    def search_by(self, queryset, name, value):
        values = value.split(' ')
        for value in values:
            queryset = queryset.filter(Q(name__icontains=value) |
                                       Q(description__icontains=value) |
                                       Q(service_vpn__name__icontains=value)) # глубина поиска второго уровня
        return queryset

