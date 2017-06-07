from lib.base import AzureBaseAzureRM


class Get_Scaleset_Size(AzureBaseAzureRM):
    def run(self, resource_group, scale_group, count):
        return self._set_scaleset(resource_group, scale_group, count)
