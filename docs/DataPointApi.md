# intrinio_sdk.DataPointApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_point_number**](DataPointApi.md#get_data_point_number) | **GET** /data_point/{identifier}/{tag}/number | Data Point (Number)
[**get_data_point_text**](DataPointApi.md#get_data_point_text) | **GET** /data_point/{identifier}/{tag}/text | Data Point (Text)



[//]: # (START_OPERTATION)

[//]: # (ENDPOINT:/data_point/{identifier}/{tag}/number)

[//]: # (DOC_LINK:DataPointApi.md#get_data_point_number)

# **get_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_data_point_number_v2)

> float get_data_point_number(identifier, tag)

Data Point (Number)

Returns a numeric value for the given `tag` and the entity with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

data_point_api = intrinio_sdk.DataPointApi()

identifier = 'AAPL' # str | An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)
tag = 'marketcap' # str | An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>)

try:
    api_response = data_point_api.get_data_point_number(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPointApi->get_data_point_number: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code (&lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags&#39;&gt;reference&lt;/a&gt;) | 

### Return type

**float**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERTATION)

[//]: # (ENDPOINT:/data_point/{identifier}/{tag}/text)

[//]: # (DOC_LINK:DataPointApi.md#get_data_point_text)

# **get_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_data_point_text_v2)

> str get_data_point_text(identifier, tag)

Data Point (Text)

Returns a text value for the given `tag` for the Security with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

data_point_api = intrinio_sdk.DataPointApi()

identifier = 'AAPL' # str | An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)
tag = 'ceo' # str | An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>)

try:
    api_response = data_point_api.get_data_point_text(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPointApi->get_data_point_text: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code (&lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags&#39;&gt;reference&lt;/a&gt;) | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

[//]: # (END_OPERATION)

