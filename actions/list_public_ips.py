from lib.base import AzureBaseAzureRM


class AzurePublicIpAction(AzureBaseAzureRM):
    def run(self, resource_group=None):
        return self._get_public_ips(resource_group)
