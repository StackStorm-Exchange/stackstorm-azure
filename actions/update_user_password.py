from azure.graphrbac.models import PasswordProfile

from lib.base import AzureBaseADUserPassAction


class AzureCreateVMAction(AzureBaseADUserPassAction):
    def run(self, user_object_id, password, force_password_change):
        self.graphrbac_client.users.update(
            user_object_id,
            {
                'passwordProfile': PasswordProfile(
                    password=password,
                    force_change_password_next_login=force_password_change
                )
            }
        )
        return {"updated": True}
