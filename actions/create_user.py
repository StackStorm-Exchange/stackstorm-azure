from azure.graphrbac.models import UserCreateParameters, PasswordProfile

from lib.base import AzureBaseADAction


class AzureCreateVMAction(AzureBaseADAction):
    def run(self, user_principal_name, account_enabled, display_name,
            mail_nickname, password, force_password_change):
        user = self.graphrbac_client.users.create(
            UserCreateParameters(
                user_principal_name=user_principal_name,
                account_enabled=account_enabled,
                display_name=display_name,
                mail_nickname=mail_nickname,
                password_profile=PasswordProfile(
                    password=password,
                    force_change_password_next_login=force_password_change
                )
            )
        )
        return {"user": user.__dict__}
