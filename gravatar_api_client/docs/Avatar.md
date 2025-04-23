# Avatar

An avatar that the user has already uploaded to their Gravatar account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | Unique identifier for the image. | 
**image_url** | **str** | Image URL | 
**rating** | **str** | Rating associated with the image. | 
**alt_text** | **str** | Alternative text description of the image. | 
**selected** | **bool** | Whether the image is currently selected as the provided selected email&#39;s avatar. | [optional] 
**updated_date** | **datetime** | Date and time when the image was last updated. | 

## Example

```python
from openapi_client.models.avatar import Avatar

# TODO update the JSON string below
json = "{}"
# create an instance of Avatar from a JSON string
avatar_instance = Avatar.from_json(json)
# print the JSON string representation of the object
print(Avatar.to_json())

# convert the object into a dict
avatar_dict = avatar_instance.to_dict()
# create an instance of Avatar from a dict
avatar_from_dict = Avatar.from_dict(avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


