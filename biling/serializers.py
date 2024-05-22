
from rest_framework import serializers
from biling.models import DataCenter, ServiceVPN, Tariff, VirtualMachine, Storage, Network, Orders


class DataCenterSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataCenter
        fields = "__all__"

class ServiceVPNSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceVPN
        fields = "__all__"



class VirtualMachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualMachine
        fields = "__all__"


class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = "__all__"

class NetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Network
        fields = "__all__"

class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = "__all__"

class TariffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tariff
        fields = "__all__"
    data_center = DataCenterSerializer()
    service_vpn = ServiceVPNSerializer()
    virtual_machine = VirtualMachineSerializer()
    storage = StorageSerializer()
    network = NetworkSerializer()