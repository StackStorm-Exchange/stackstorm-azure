from lib.base import AzureBaseADUserPassAction


class AzureCreateVMAction(AzureBaseADUserPassAction):
    def run(self, user_object_id):
        self.graphrbac_client.users.delete(user_object_id)
        return {"deleted": True}
