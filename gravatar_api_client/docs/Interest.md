# Interest

An interest the user has added to their profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the interest. | 
**name** | **str** | The name of the interest. | 

## Example

```python
from openapi_client.models.interest import Interest

# TODO update the JSON string below
json = "{}"
# create an instance of Interest from a JSON string
interest_instance = Interest.from_json(json)
# print the JSON string representation of the object
print(Interest.to_json())

# convert the object into a dict
interest_dict = interest_instance.to_dict()
# create an instance of Interest from a dict
interest_from_dict = Interest.from_dict(interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


