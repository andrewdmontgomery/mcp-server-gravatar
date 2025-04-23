# Profile

A user's profile information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | The SHA256 hash of the user&#39;s primary email address. | 
**display_name** | **str** | The user&#39;s display name. This is the name that is displayed on their profile. | 
**profile_url** | **str** | The full URL for the user&#39;s profile. | 
**avatar_url** | **str** | The URL for the user&#39;s avatar image if it has been set. | 
**avatar_alt_text** | **str** | The alt text for the user&#39;s avatar image if it has been set. | 
**location** | **str** | The user&#39;s location. | 
**description** | **str** | The about section on a user&#39;s profile. | 
**job_title** | **str** | The user&#39;s job title. | 
**company** | **str** | The user&#39;s current company&#39;s name. | 
**verified_accounts** | [**List[VerifiedAccount]**](VerifiedAccount.md) | A list of verified accounts the user has added to their profile. This is limited to a max of 4 in unauthenticated requests. | 
**pronunciation** | **str** | The phonetic pronunciation of the user&#39;s name. | 
**pronouns** | **str** | The pronouns the user uses. | 
**timezone** | **str** | The timezone the user has. This is only provided in authenticated API requests. | [optional] 
**languages** | [**List[Language]**](Language.md) | The languages the user knows. This is only provided in authenticated API requests. | [optional] 
**first_name** | **str** | User&#39;s first name. This is only provided in authenticated API requests. | [optional] 
**last_name** | **str** | User&#39;s last name. This is only provided in authenticated API requests. | [optional] 
**is_organization** | **bool** | Whether user is an organization. This is only provided in authenticated API requests. | [optional] 
**header_image** | **str** | The header image used in the main profile card. | [optional] 
**background_color** | **str** | The profile background color. | [optional] 
**links** | [**List[Link]**](Link.md) | A list of links the user has added to their profile. This is only provided in authenticated API requests. | [optional] 
**interests** | [**List[Interest]**](Interest.md) | A list of interests the user has added to their profile. This is only provided in authenticated API requests. | [optional] 
**payments** | [**ProfilePayments**](ProfilePayments.md) |  | [optional] 
**contact_info** | [**ProfileContactInfo**](ProfileContactInfo.md) |  | [optional] 
**gallery** | [**List[GalleryImage]**](GalleryImage.md) | Additional images a user has uploaded. This is only provided in authenticated API requests. | [optional] 
**number_verified_accounts** | **int** | The number of verified accounts the user has added to their profile. This count includes verified accounts the user is hiding from their profile. This is only provided in authenticated API requests. | [optional] 
**last_profile_edit** | **datetime** | The date and time (UTC) the user last edited their profile. This is only provided in authenticated API requests. | [optional] 
**registration_date** | **datetime** | The date the user registered their account. This is only provided in authenticated API requests. | [optional] 

## Example

```python
from openapi_client.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


