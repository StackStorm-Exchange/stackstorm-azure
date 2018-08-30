# Microsoft Azure Integration Pack

Pack which contains integrations for different Microsoft Azure services.

## Configuration

Copy the example configuration in [azure.yaml.example](./azure.yaml.example)
to `/opt/stackstorm/configs/azure.yaml` and edit as required.

* ``compute.subscription_id`` - Your Azure subscription ID.
* ``compute.cert_file`` - Path to the certificate file used for authentication.

For information on how to obtain your subscription ID and generate and upload a
certificate file, see the following page [Generating and uploading a
certificate file and obtaining subscription ID](https://libcloud.readthedocs.org/en/latest/compute/drivers/azure.html#generating-and-uploading-a-certificate-file-and-obtaining-subscription-id).

* ``storage.name`` - Your storage account name.
* ``storage.access_key`` - Your storage account access key.

For information on how to obtain those credentials, see the following page
[Connecting to Azure Blobs](https://libcloud.readthedocs.org/en/latest/storage/drivers/azure_blobs.html#connecting-to-azure-blobs).

* ``resource_manager.client_id`` Resource manager client ID
* ``resource_manager.secret`` Resource manager token
* ``resource_manager.tenant`` Resource manager tenant identifier
* ``default_resource_group`` - Default resource group

For usage of the Resource Manager actions you will need to create a [Service Principal](https://azure.microsoft.com/en-us/documentation/articles/resource-group-create-service-principal-portal/)

* ``username`` Username of administrator for modifying Azure AD users
* ``password`` Password of administrator for modifying Azure AD users

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

### Virtual Machines / Servers

* ``list_vms`` - List available VMs.
* ``create_vm`` - Create a new VM.
* ``reboot_vm`` - Reboot a VM.
* ``destroy_vm`` - Destroy a VM.

### Object Storage

* ``list_containers`` - List containers.
* ``list_container_objects`` - List container objects.
* ``upload_file`` - Upload local file to the provided container.
* ``delete_object`` - Delete the provided object.

### Resource Management

* ``create_resource`` - Create a generic ARM resource
* ``create_linked_resource_url`` - Create a linked (template and parameter) resource from a URI
* ``list_resource_groups`` - List the names of the resource groups

## Actions

* ``create_ticket`` - Creates a new ticket with the given subject and description.
* ``search_tickets`` - Searches all tickets for the given phrase.
* ``update_ticket`` - Updates the ticket with the given ID with a new comment.
* ``update_ticket_status`` - Updates the status of the ticket with the given ID.
