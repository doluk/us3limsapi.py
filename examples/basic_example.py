import asyncio
import os
import dotenv
from pprint import pprint

import us3api
from us3api import HPCAnalysisMethod
from us3api.rest import ApiException

dotenv.load_dotenv()

# See configuration.py for a list of all supported configuration parameters.
configuration = us3api.Configuration(
        host=os.environ.get('US3_LIMS_API_URL'),
        username=os.environ.get('US3_USERNAME'),
        password=os.environ.get('US3_PASSWORD')
)


async def main():
    # Enter a context with an instance of the API client
    async with us3api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = us3api.PersonApi(api_client)
        
        try:
            api_response = await api_instance.persons_me_get()
            print("The response of PersonApi->persons_me_get:\n")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonApi->persons_me_get: %s\n" % e)


if __name__ == '__main__':
    
    asyncio.run(main())
