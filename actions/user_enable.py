from lib.base import AzureBaseADUserPassAction


class AzureCreateVMAction(AzureBaseADUserPassAction):
    def run(self, user_object_id, enable):
        self.graphrbac_client.users.update(user_object_id, {'accountEnabled': enable})
        return {"updated": True}
