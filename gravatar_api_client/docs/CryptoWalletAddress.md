# CryptoWalletAddress

A crypto currency wallet address the user accepts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the crypto currency. | 
**address** | **str** | The wallet address for the crypto currency. | 

## Example

```python
from openapi_client.models.crypto_wallet_address import CryptoWalletAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoWalletAddress from a JSON string
crypto_wallet_address_instance = CryptoWalletAddress.from_json(json)
# print the JSON string representation of the object
print(CryptoWalletAddress.to_json())

# convert the object into a dict
crypto_wallet_address_dict = crypto_wallet_address_instance.to_dict()
# create an instance of CryptoWalletAddress from a dict
crypto_wallet_address_from_dict = CryptoWalletAddress.from_dict(crypto_wallet_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


