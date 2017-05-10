from lib.base import AzureBaseAzureRM

class Main(AzureBaseAzureRM):
    def run(self, resource_group, scale_group, count):
        return self._set_scaleset(resource_group, scale_group, count)
