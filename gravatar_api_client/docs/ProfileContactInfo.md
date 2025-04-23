# ProfileContactInfo

The user's contact information. This is only available if the user has chosen to make it public. This is only provided in authenticated API requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_phone** | **str** | The user&#39;s home phone number. | [optional] 
**work_phone** | **str** | The user&#39;s work phone number. | [optional] 
**cell_phone** | **str** | The user&#39;s cell phone number. | [optional] 
**email** | **str** | The user&#39;s email address as provided on the contact section of the profile. Might differ from their account emails. | [optional] 
**contact_form** | **str** | The URL to the user&#39;s contact form. | [optional] 
**calendar** | **str** | The URL to the user&#39;s calendar. | [optional] 

## Example

```python
from openapi_client.models.profile_contact_info import ProfileContactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileContactInfo from a JSON string
profile_contact_info_instance = ProfileContactInfo.from_json(json)
# print the JSON string representation of the object
print(ProfileContactInfo.to_json())

# convert the object into a dict
profile_contact_info_dict = profile_contact_info_instance.to_dict()
# create an instance of ProfileContactInfo from a dict
profile_contact_info_from_dict = ProfileContactInfo.from_dict(profile_contact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


