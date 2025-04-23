# VerifiedAccount

A verified account on a user's profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_type** | **str** | The type of the service. | 
**service_label** | **str** | The name of the service. | 
**service_icon** | **str** | The URL to the service&#39;s icon. | 
**url** | **str** | The URL to the user&#39;s profile on the service. | 
**is_hidden** | **bool** | Whether the verified account is hidden from the user&#39;s profile. | 

## Example

```python
from openapi_client.models.verified_account import VerifiedAccount

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedAccount from a JSON string
verified_account_instance = VerifiedAccount.from_json(json)
# print the JSON string representation of the object
print(VerifiedAccount.to_json())

# convert the object into a dict
verified_account_dict = verified_account_instance.to_dict()
# create an instance of VerifiedAccount from a dict
verified_account_from_dict = VerifiedAccount.from_dict(verified_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


