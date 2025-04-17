# openapi_client.ProfilesApi

All URIs are relative to *https://api.gravatar.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associated_email**](ProfilesApi.md#associated_email) | **GET** /me/associated-email | Check if the email is associated with the authenticated user
[**get_profile_by_id**](ProfilesApi.md#get_profile_by_id) | **GET** /profiles/{profileIdentifier} | Get profile by identifier


# **associated_email**
> AssociatedResponse associated_email(email_hash)

Check if the email is associated with the authenticated user

Checks if the provided email address is associated with the authenticated user.

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
    api_instance = openapi_client.ProfilesApi(api_client)
    email_hash = 'email_hash_example' # str | The hash of the email address to check.

    try:
        # Check if the email is associated with the authenticated user
        api_response = api_instance.associated_email(email_hash)
        print("The response of ProfilesApi->associated_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->associated_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_hash** | **str**| The hash of the email address to check. | 

### Return type

[**AssociatedResponse**](AssociatedResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The email is associated with the authenticated user |  -  |
**401** | Not Authorized |  -  |
**403** | Insufficient Scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_by_id**
> Profile get_profile_by_id(profile_identifier)

Get profile by identifier

Returns a profile by the given identifier.

### Example

* Bearer Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.profile import Profile
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

# Configure Bearer authorization: apiKey
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProfilesApi(api_client)
    profile_identifier = 'profile_identifier_example' # str | This can either be an SHA256 hash of an email address or profile URL slug.

    try:
        # Get profile by identifier
        api_response = api_instance.get_profile_by_id(profile_identifier)
        print("The response of ProfilesApi->get_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_identifier** | **str**| This can either be an SHA256 hash of an email address or profile URL slug. | 

### Return type

[**Profile**](Profile.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | Profile not found |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Rate Limit Exceeded |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

