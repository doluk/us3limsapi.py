# us3api.PersonApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**persons_get**](PersonApi.md#persons_get) | **GET** /persons | 
[**persons_me_get**](PersonApi.md#persons_me_get) | **GET** /persons/me | 
[**persons_person_id_get**](PersonApi.md#persons_person_id_get) | **GET** /persons/{personID} | 
[**persons_search_get**](PersonApi.md#persons_search_get) | **GET** /persons/search | 


# **persons_get**
> List[Person] persons_get()



Get a list of all persons

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.person import Person
from us3api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = us3api.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: LIMSLogin
configuration = us3api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: USEmail
configuration.api_key['USEmail'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USEmail'] = 'Bearer'

# Configure API key authorization: USPassword
configuration.api_key['USPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USPassword'] = 'Bearer'

# Enter a context with an instance of the API client
async with us3api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = us3api.PersonApi(api_client)

    try:
        api_response = await api_instance.persons_get()
        print("The response of PersonApi->persons_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->persons_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Person]**](Person.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of persons |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persons_me_get**
> Person persons_me_get()



Get the current person

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.person import Person
from us3api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = us3api.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: LIMSLogin
configuration = us3api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: USEmail
configuration.api_key['USEmail'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USEmail'] = 'Bearer'

# Configure API key authorization: USPassword
configuration.api_key['USPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USPassword'] = 'Bearer'

# Enter a context with an instance of the API client
async with us3api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = us3api.PersonApi(api_client)

    try:
        api_response = await api_instance.persons_me_get()
        print("The response of PersonApi->persons_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->persons_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Person**](Person.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current person |  -  |
**404** | Person not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persons_person_id_get**
> Person persons_person_id_get(person_id)



Get a person by ID

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.person import Person
from us3api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = us3api.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: LIMSLogin
configuration = us3api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: USEmail
configuration.api_key['USEmail'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USEmail'] = 'Bearer'

# Configure API key authorization: USPassword
configuration.api_key['USPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USPassword'] = 'Bearer'

# Enter a context with an instance of the API client
async with us3api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = us3api.PersonApi(api_client)
    person_id = 56 # int | ID of person to return

    try:
        api_response = await api_instance.persons_person_id_get(person_id)
        print("The response of PersonApi->persons_person_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->persons_person_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| ID of person to return | 

### Return type

[**Person**](Person.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A person |  -  |
**404** | Person not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persons_search_get**
> List[Person] persons_search_get(email=email, first_name=first_name, last_name=last_name, username=username, person_id=person_id, person_guid=person_guid)



Search for persons

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.person import Person
from us3api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = us3api.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: LIMSLogin
configuration = us3api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: USEmail
configuration.api_key['USEmail'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USEmail'] = 'Bearer'

# Configure API key authorization: USPassword
configuration.api_key['USPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USPassword'] = 'Bearer'

# Enter a context with an instance of the API client
async with us3api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = us3api.PersonApi(api_client)
    email = 'email_example' # str | Email of person to search for (optional)
    first_name = 'first_name_example' # str | First name of person to search for (optional)
    last_name = 'last_name_example' # str | Last name of person to search for (optional)
    username = 'username_example' # str | Username of person to search for (optional)
    person_id = 56 # int | personID of person to search for (optional)
    person_guid = 'person_guid_example' # str | personGUID of person to search for (optional)

    try:
        api_response = await api_instance.persons_search_get(email=email, first_name=first_name, last_name=last_name, username=username, person_id=person_id, person_guid=person_guid)
        print("The response of PersonApi->persons_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->persons_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of person to search for | [optional] 
 **first_name** | **str**| First name of person to search for | [optional] 
 **last_name** | **str**| Last name of person to search for | [optional] 
 **username** | **str**| Username of person to search for | [optional] 
 **person_id** | **int**| personID of person to search for | [optional] 
 **person_guid** | **str**| personGUID of person to search for | [optional] 

### Return type

[**List[Person]**](Person.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of persons |  -  |
**404** | No persons found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

