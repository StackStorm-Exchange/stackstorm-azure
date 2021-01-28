# Change Log

## 0.4.3

- Pin azure to <5.0 so we don't have to refactor to use the azure-mgmt-compute,
  azure-mgmt-storage, azure-mgmt-resource, azure-keyvault-secrets, and
  azure-storage-blob packages separately - see
  https://github.com/Azure/azure-sdk-for-python/issues/10646 for more

## 0.4.2

- Pin libcloud to <3.0.0 to maintain Python 2 support

## 0.4.1

- Version bump to fix tagging issue, no code changes

## 0.4.0

- Added new actions for working with Azure AD

## 0.3.1

- Changed st2actions import path
- Pinned azurerm version to avoid breaking changes in v0.8.28 and later

## 0.3.0

- Updated action `runner_type` from `run-python` to `python-script`

## 0.2.1

- Adding azurerm package
- Adding actions
  - Get/put scaleset size 
  - Get public address from resouce group

## 0.2.0

- Rename `config.yaml` to `config.schema.yaml` and update to use schema.

## 0.1.0

- First release 
