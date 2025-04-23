# GalleryImage

A gallery image a user has uploaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to the image. | 
**alt_text** | **str** | The image alt text. | [optional] 

## Example

```python
from openapi_client.models.gallery_image import GalleryImage

# TODO update the JSON string below
json = "{}"
# create an instance of GalleryImage from a JSON string
gallery_image_instance = GalleryImage.from_json(json)
# print the JSON string representation of the object
print(GalleryImage.to_json())

# convert the object into a dict
gallery_image_dict = gallery_image_instance.to_dict()
# create an instance of GalleryImage from a dict
gallery_image_from_dict = GalleryImage.from_dict(gallery_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


