from st2common.runners.base_action import Action

from libcloud.compute.providers import Provider as ComputeProvider
from libcloud.compute.providers import get_driver as get_compute_driver
from libcloud.storage.providers import Provider as StorageProvider
from libcloud.storage.providers import get_driver as get_storage_driver

from msrestazure.azure_active_directory import ServicePrincipalCredentials, UserPassCredentials
from azure.graphrbac import GraphRbacManagementClient

import azurerm

__all__ = [
    'AzureBaseComputeAction',
    'AzureBaseStorageAction',
    'AzureBaseResourceManagerAction',
    'AzureBaseAzureRM'
]


class AzureBaseAzureRM(Action):
    def __init__(self, config):
        super(AzureBaseAzureRM, self).__init__(config=config)
        resource_manager = config['resource_manager']
        tenant_id = resource_manager['tenant']
        app_id = resource_manager['client_id']
        app_secret = resource_manager['secret']
        self.subscription_id = config['compute']['subscription_id']
        self.access_token = azurerm.get_access_token(tenant_id, app_id, app_secret)
        self.default_resource_group = self._get_default_resource_group_from_cfg(resource_manager)

    @staticmethod
    def _get_default_resource_group_from_cfg(config):
        return config.get('default_resource_group')

    def _get_resource_group(self, resource_group):
        if resource_group:
            return resource_group
        elif self.default_resource_group:
            return str(self.default_resource_group)
        else:
            raise Exception("Missing resource group")

    def _get_scaleset(self, resource_group=None, scale_group=None):
        output = azurerm.get_vmss(self.access_token,
                                  self.subscription_id,
                                  self._get_resource_group(resource_group),
                                  scale_group)

        return {'resource_group': self._get_resource_group(resource_group),
                'scale_group_name': output['name'],
                'tier': output['sku']['tier'],
                'capacity': output['sku']['capacity'],
                'machine_type': output['sku']['name']}

    def _set_scaleset(self, resource_group=None, scale_group=None, count=1):
        get_current = self._get_scaleset(self._get_resource_group(resource_group), scale_group)
        return azurerm.scale_vmss(self.access_token,
                                  self.subscription_id,
                                  self._get_resource_group(resource_group),
                                  scale_group,
                                  get_current['machine_type'],
                                  get_current['tier'],
                                  count)

    def _get_public_ips(self, resource_group=None):
        result = azurerm.list_public_ips(self.access_token,
                                         self.subscription_id,
                                         resource_group=resource_group)

        if 'error' not in result and 'value' in result:
            return [str(i['properties']['ipAddress']) for i in result['value']]


class AzureBaseComputeAction(Action):
    def __init__(self, config):
        super(AzureBaseComputeAction, self).__init__(config=config)

        config = self.config['compute']
        subscription_id = config['subscription_id']
        key_file = config['cert_file']
        self._driver = self._get_driver(subscription_id=subscription_id,
                                        key_file=key_file)

    def _get_driver(self, subscription_id, key_file):
        cls = get_compute_driver(ComputeProvider.AZURE)
        driver = cls(subscription_id=subscription_id, key_file=key_file)
        return driver


class AzureBaseStorageAction(Action):
    def __init__(self, config):
        super(AzureBaseStorageAction, self).__init__(config=config)

        config = self.config['storage']
        name = config['name']
        access_key = config['access_key']
        self._driver = self._get_driver(name=name, access_key=access_key)

    def _get_driver(self, name, access_key):
        cls = get_storage_driver(StorageProvider.AZURE_BLOBS)
        driver = cls(key=name, secret=access_key)
        return driver


class AzureBaseResourceManagerAction(Action):
    def __init__(self, config):
        super(AzureBaseResourceManagerAction, self).__init__(config=config)

        resource_config = self.config['resource_manager']
        self.credentials = ServicePrincipalCredentials(
            client_id=resource_config['client_id'],
            secret=resource_config['secret'],
            tenant=resource_config['tenant']
        )


class AzureBaseADAction(Action):
    def __init__(self, config):
        super(AzureBaseADAction, self).__init__(config=config)
        resource_config = self.config['resource_manager']
        self.credentials = ServicePrincipalCredentials(
            client_id=resource_config['client_id'],
            secret=resource_config['secret'],
            tenant=resource_config['tenant'],
            resource='https://graph.windows.net'
        )

        self.graphrbac_client = GraphRbacManagementClient(
            self.credentials,
            resource_config['tenant']
        )


class AzureBaseADUserPassAction(Action):
    def __init__(self, config):
        super(AzureBaseADUserPassAction, self).__init__(config=config)
        user_config = self.config['user']
        resource_config = self.config['resource_manager']
        self.credentials = UserPassCredentials(
            user_config['username'],
            user_config['password'],
            resource='https://graph.windows.net'
        )

        self.graphrbac_client = GraphRbacManagementClient(
            self.credentials,
            resource_config['tenant']
        )
