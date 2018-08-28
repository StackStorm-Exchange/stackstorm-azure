from lib.base import AzureBaseADAction


class AzureCreateVMAction(AzureBaseADAction):
    def run(self, user_object_id, first_name, last_name):
        if not last_name and not first_name:
            return {"updated": False}

        update = {}

        if first_name:
            update['givenName'] = first_name

        if last_name:
            update['surName'] = last_name

        self.graphrbac_client.users.update(user_object_id, update)
        return {"updated": True}
