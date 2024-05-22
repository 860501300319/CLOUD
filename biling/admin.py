from django.contrib import admin
from biling.models import DataCenter, Tariff, ServiceVPN,  VirtualMachine, Storage, Network, Orders


@admin.register(DataCenter)
class DataCenterAdmin(admin.ModelAdmin):
    # fields = ("name", "location")
    list_display = ("name", "location")


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    # fields = ("name", "description", "price", "data_center", "service_vpn", "virtual_machine",  "storage", "network")
    list_display = ("name", "description", "price", "data_center", "service_vpn", "virtual_machine",  "storage", "network")

@admin.register(ServiceVPN)
class ServiceVPNAdmin(admin.ModelAdmin):
    # fields = ("name", "description")
    list_display = ("name", "description")

@admin.register(VirtualMachine)
class VirtualAdmin(admin.ModelAdmin):
    # fields = ("name", "cpu_cores", "ram_gb", "storage_gb")
    list_display = ("name", "cpu_cores", "ram_gb", "storage_gb")


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    # fields = ("name", "capacity_gb")
    list_display = ("name", "capacity_gb")

@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    # fields = ("name", "speed_mbps")
    list_display = ("name", "speed_mbps")


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    # list_display = ("user", "tariff", "start_date", "end_date")
    list_display = ("user", "tariff", "start_date", "end_date")



# Register your models here.
