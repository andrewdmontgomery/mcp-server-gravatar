# UpdateAvatarRequest

The avatar data to update. Partial updates are supported, so only the provided fields will be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | [**AvatarRating**](AvatarRating.md) | Rating associated with the image. | [optional] 
**alt_text** | **str** | Alternative text description of the image. | [optional] 

## Example

```python
from openapi_client.models.update_avatar_request import UpdateAvatarRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAvatarRequest from a JSON string
update_avatar_request_instance = UpdateAvatarRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAvatarRequest.to_json())

# convert the object into a dict
update_avatar_request_dict = update_avatar_request_instance.to_dict()
# create an instance of UpdateAvatarRequest from a dict
update_avatar_request_from_dict = UpdateAvatarRequest.from_dict(update_avatar_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


