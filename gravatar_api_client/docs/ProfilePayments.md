# ProfilePayments

The user's public payment information. This is only provided in authenticated API requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Link]**](Link.md) | A list of payment URLs the user has added to their profile. | 
**crypto_wallets** | [**List[CryptoWalletAddress]**](CryptoWalletAddress.md) | A list of crypto currencies the user accepts. | 

## Example

```python
from openapi_client.models.profile_payments import ProfilePayments

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePayments from a JSON string
profile_payments_instance = ProfilePayments.from_json(json)
# print the JSON string representation of the object
print(ProfilePayments.to_json())

# convert the object into a dict
profile_payments_dict = profile_payments_instance.to_dict()
# create an instance of ProfilePayments from a dict
profile_payments_from_dict = ProfilePayments.from_dict(profile_payments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


