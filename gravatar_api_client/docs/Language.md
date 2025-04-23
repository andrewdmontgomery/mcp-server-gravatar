# Language

The languages the user knows. This is only provided in authenticated API requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The language code. | 
**name** | **str** | The language name. | 
**is_primary** | **bool** | Whether the language is the user&#39;s primary language. | 
**order** | **int** | The order of the language in the user&#39;s profile. | 

## Example

```python
from openapi_client.models.language import Language

# TODO update the JSON string below
json = "{}"
# create an instance of Language from a JSON string
language_instance = Language.from_json(json)
# print the JSON string representation of the object
print(Language.to_json())

# convert the object into a dict
language_dict = language_instance.to_dict()
# create an instance of Language from a dict
language_from_dict = Language.from_dict(language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


