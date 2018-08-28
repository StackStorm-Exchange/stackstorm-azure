from lib.base import AzureBaseADAction


class AzureCreateVMAction(AzureBaseADAction):
    def run(self, user_object_id, display_name):
        self.graphrbac_client.users.update(user_object_id, {'displayName': display_name})
        return {"updated": True}
