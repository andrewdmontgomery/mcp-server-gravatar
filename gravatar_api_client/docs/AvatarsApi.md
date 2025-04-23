# openapi_client.AvatarsApi

All URIs are relative to *https://api.gravatar.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_avatar**](AvatarsApi.md#delete_avatar) | **DELETE** /me/avatars/{imageId} | Delete avatar
[**get_avatars**](AvatarsApi.md#get_avatars) | **GET** /me/avatars | List avatars
[**set_email_avatar**](AvatarsApi.md#set_email_avatar) | **POST** /me/avatars/{imageId}/email | Set avatar for the hashed email
[**update_avatar**](AvatarsApi.md#update_avatar) | **PATCH** /me/avatars/{imageId} | Update avatar data
[**upload_avatar**](AvatarsApi.md#upload_avatar) | **POST** /me/avatars | Upload new avatar image


# **delete_avatar**
> delete_avatar(image_id)

Delete avatar

Deletes a specific avatar for the authenticated user.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gravatar.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.gravatar.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AvatarsApi(api_client)
    image_id = 'image_id_example' # str | The ID of the avatar to delete.

    try:
        # Delete avatar
        api_instance.delete_avatar(image_id)
    except Exception as e:
        print("Exception when calling AvatarsApi->delete_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The ID of the avatar to delete. | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Avatar deleted successfully |  -  |
**401** | Not Authorized |  -  |
**403** | Insufficient Scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatars**
> List[Avatar] get_avatars(selected_email_hash=selected_email_hash)

List avatars

Retrieves a list of available avatars for the authenticated user.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.avatar import Avatar
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gravatar.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.gravatar.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AvatarsApi(api_client)
    selected_email_hash = '' # str | The SHA256 hash of the email address used to determine which avatar is selected. The 'selected' attribute in the avatar list will be set to 'true' for the avatar associated with this email. (optional) (default to '')

    try:
        # List avatars
        api_response = api_instance.get_avatars(selected_email_hash=selected_email_hash)
        print("The response of AvatarsApi->get_avatars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->get_avatars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selected_email_hash** | **str**| The SHA256 hash of the email address used to determine which avatar is selected. The &#39;selected&#39; attribute in the avatar list will be set to &#39;true&#39; for the avatar associated with this email. | [optional] [default to &#39;&#39;]

### Return type

[**List[Avatar]**](Avatar.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of avatars |  -  |
**401** | Not Authorized |  -  |
**403** | Insufficient Scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_email_avatar**
> set_email_avatar(image_id, set_email_avatar_request)

Set avatar for the hashed email

Sets the avatar for the provided email hash.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.set_email_avatar_request import SetEmailAvatarRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gravatar.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.gravatar.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AvatarsApi(api_client)
    image_id = 'image_id_example' # str | Image ID of the avatar to set as the provided hashed email avatar.
    set_email_avatar_request = openapi_client.SetEmailAvatarRequest() # SetEmailAvatarRequest | Avatar selection details

    try:
        # Set avatar for the hashed email
        api_instance.set_email_avatar(image_id, set_email_avatar_request)
    except Exception as e:
        print("Exception when calling AvatarsApi->set_email_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Image ID of the avatar to set as the provided hashed email avatar. | 
 **set_email_avatar_request** | [**SetEmailAvatarRequest**](SetEmailAvatarRequest.md)| Avatar selection details | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Avatar successfully set |  -  |
**401** | Not Authorized |  -  |
**403** | Insufficient Scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avatar**
> Avatar update_avatar(image_id, update_avatar_request)

Update avatar data

Updates the avatar data for a given avatar for the authenticated user.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.avatar import Avatar
from openapi_client.models.update_avatar_request import UpdateAvatarRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gravatar.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.gravatar.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AvatarsApi(api_client)
    image_id = 'image_id_example' # str | The ID of the avatar to update.
    update_avatar_request = openapi_client.UpdateAvatarRequest() # UpdateAvatarRequest | 

    try:
        # Update avatar data
        api_response = api_instance.update_avatar(image_id, update_avatar_request)
        print("The response of AvatarsApi->update_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->update_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The ID of the avatar to update. | 
 **update_avatar_request** | [**UpdateAvatarRequest**](UpdateAvatarRequest.md)|  | 

### Return type

[**Avatar**](Avatar.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Avatar updated successfully |  -  |
**401** | Not Authorized |  -  |
**403** | Insufficient Scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_avatar**
> Avatar upload_avatar(data, selected_email_hash=selected_email_hash, select_avatar=select_avatar)

Upload new avatar image

Uploads a new avatar image for the authenticated user.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.avatar import Avatar
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gravatar.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.gravatar.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AvatarsApi(api_client)
    data = None # bytearray | The avatar image file
    selected_email_hash = 'selected_email_hash_example' # str | The SHA256 hash of email. If provided, the uploaded image will be selected as the avatar for this email. (optional)
    select_avatar = False # bool | Determines if the uploaded image should be set as the avatar for the email. If not passed, the image is only selected as the email's avatar if no previous avatar has been set. Accepts '1'/'true' to always set the avatar or '0'/'false' to never set the avatar. (optional) (default to False)

    try:
        # Upload new avatar image
        api_response = api_instance.upload_avatar(data, selected_email_hash=selected_email_hash, select_avatar=select_avatar)
        print("The response of AvatarsApi->upload_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->upload_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **bytearray**| The avatar image file | 
 **selected_email_hash** | **str**| The SHA256 hash of email. If provided, the uploaded image will be selected as the avatar for this email. | [optional] 
 **select_avatar** | **bool**| Determines if the uploaded image should be set as the avatar for the email. If not passed, the image is only selected as the email&#39;s avatar if no previous avatar has been set. Accepts &#39;1&#39;/&#39;true&#39; to always set the avatar or &#39;0&#39;/&#39;false&#39; to never set the avatar. | [optional] [default to False]

### Return type

[**Avatar**](Avatar.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Avatar uploaded successfully |  -  |
**400** | Invalid request |  -  |
**401** | Not Authorized |  -  |
**403** | Insufficient Scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

