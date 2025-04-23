# SetEmailAvatarRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_hash** | **str** | The email SHA256 hash to set the avatar for. | 

## Example

```python
from openapi_client.models.set_email_avatar_request import SetEmailAvatarRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetEmailAvatarRequest from a JSON string
set_email_avatar_request_instance = SetEmailAvatarRequest.from_json(json)
# print the JSON string representation of the object
print(SetEmailAvatarRequest.to_json())

# convert the object into a dict
set_email_avatar_request_dict = set_email_avatar_request_instance.to_dict()
# create an instance of SetEmailAvatarRequest from a dict
set_email_avatar_request_from_dict = SetEmailAvatarRequest.from_dict(set_email_avatar_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


