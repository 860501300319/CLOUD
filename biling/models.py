# Облачные услуги
from django.db import models
# from datetime, django.utils import timezone.now as value

class DataCenter(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    city_id = models.IntegerField(default=701)
    def __str__(self):
        return self.name

# class Service(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     # price = models.DecimalField(max_digits=10, decimal_places=2)
#     data_center = models.ForeignKey(DataCenter, on_delete=models.CASCADE)
#     def __str__(self):
#         return f'{self.name} - {self.data_center}'

class Tariff(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    data_center = models.ForeignKey('biling.DataCenter', on_delete=models.CASCADE,default=1)
    service_vpn = models.ForeignKey('biling.ServiceVPN', on_delete=models.CASCADE,null=True,default=None)
    virtual_machine = models.ForeignKey('biling.VirtualMachine', on_delete=models.CASCADE,default=1)
    storage = models.ForeignKey('biling.Storage', on_delete=models.CASCADE,default=1)
    network = models.ForeignKey('biling.Network', on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f'{self.name} - {self.data_center_id}'

class ServiceVPN(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # service_tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'{self.name}'

class VirtualMachine(models.Model):
    name = models.CharField(max_length=255)
    cpu_cores = models.IntegerField()
    ram_gb = models.IntegerField()
    storage_gb = models.IntegerField()
    # virtual_machine_tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'

class Storage(models.Model):
    name = models.CharField(max_length=255)
    capacity_gb = models.IntegerField()
    # storage_tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'

class Network(models.Model):
    name = models.CharField(max_length=255)
    speed_mbps = models.IntegerField()
    # network_tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'


from django.utils import timezone

# from datetime import datetime
import datetime
class Orders(models.Model):
    start_date = models.DateField(blank=True, null=True, default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True, default=datetime.date.today)
    tariff = models.ForeignKey('biling.Tariff', on_delete=models.CASCADE)
    user = models.ForeignKey('authorization.User', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f'{self.id}'




