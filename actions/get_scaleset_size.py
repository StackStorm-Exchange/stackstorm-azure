from lib.base import AzureBaseAzureRM


class Get_Scaleset_Size(AzureBaseAzureRM):
    def run(self, resource_group=None, scale_group=None):
        return self._get_scaleset(resource_group, scale_group)
