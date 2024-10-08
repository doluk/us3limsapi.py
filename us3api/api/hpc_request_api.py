# coding: utf-8

"""
    UltraScan 3 LIMS Database Instance API

    A more machine-accessible version of the UltraScan 3 LIMS functionality. The authentication is done using the user's US3 LIMS credentials and sending them with every request as header `Us-Email` and `Us-Password`. Alternatively Basic Auth can be used.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from us3api.models.hpc_analysis_method import HPCAnalysisMethod
from us3api.models.hpc_analysis_queue_status import HPCAnalysisQueueStatus
from us3api.models.hpc_analysis_request import HPCAnalysisRequest
from us3api.models.hpc_analysis_request_body import HPCAnalysisRequestBody
from us3api.models.hpc_request_submission import HPCRequestSubmission

from us3api.api_client import ApiClient, RequestSerialized
from us3api.api_response import ApiResponse
from us3api.rest import RESTResponseType


class HPCRequestApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def hpcrequests_hpc_request_id_get(
        self,
        hpc_request_id: Annotated[StrictInt, Field(description="ID of HPC analysis request to return")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> HPCAnalysisRequest:
        """hpcrequests_hpc_request_id_get

        Get an HPC analysis request by ID

        :param hpc_request_id: ID of HPC analysis request to return (required)
        :type hpc_request_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._hpcrequests_hpc_request_id_get_serialize(
            hpc_request_id=hpc_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HPCAnalysisRequest",
            '404': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def hpcrequests_hpc_request_id_get_with_http_info(
        self,
        hpc_request_id: Annotated[StrictInt, Field(description="ID of HPC analysis request to return")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[HPCAnalysisRequest]:
        """hpcrequests_hpc_request_id_get

        Get an HPC analysis request by ID

        :param hpc_request_id: ID of HPC analysis request to return (required)
        :type hpc_request_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._hpcrequests_hpc_request_id_get_serialize(
            hpc_request_id=hpc_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HPCAnalysisRequest",
            '404': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def hpcrequests_hpc_request_id_get_without_preload_content(
        self,
        hpc_request_id: Annotated[StrictInt, Field(description="ID of HPC analysis request to return")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """hpcrequests_hpc_request_id_get

        Get an HPC analysis request by ID

        :param hpc_request_id: ID of HPC analysis request to return (required)
        :type hpc_request_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._hpcrequests_hpc_request_id_get_serialize(
            hpc_request_id=hpc_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HPCAnalysisRequest",
            '404': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _hpcrequests_hpc_request_id_get_serialize(
        self,
        hpc_request_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if hpc_request_id is not None:
            _path_params['hpcRequestID'] = hpc_request_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'LIMSLogin', 
            'USEmail', 
            'USPassword'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/hpcrequests/{hpcRequestID}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    async def hpcrequests_post(
        self,
        hpc_analysis_request_body: HPCAnalysisRequestBody,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> HPCRequestSubmission:
        """hpcrequests_post

        Create a new HPC analysis request

        :param hpc_analysis_request_body: (required)
        :type hpc_analysis_request_body: HPCAnalysisRequestBody
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._hpcrequests_post_serialize(
            hpc_analysis_request_body=hpc_analysis_request_body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HPCRequestSubmission",
            '400': None,
            '500': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def hpcrequests_post_with_http_info(
        self,
        hpc_analysis_request_body: HPCAnalysisRequestBody,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[HPCRequestSubmission]:
        """hpcrequests_post

        Create a new HPC analysis request

        :param hpc_analysis_request_body: (required)
        :type hpc_analysis_request_body: HPCAnalysisRequestBody
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._hpcrequests_post_serialize(
            hpc_analysis_request_body=hpc_analysis_request_body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HPCRequestSubmission",
            '400': None,
            '500': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def hpcrequests_post_without_preload_content(
        self,
        hpc_analysis_request_body: HPCAnalysisRequestBody,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """hpcrequests_post

        Create a new HPC analysis request

        :param hpc_analysis_request_body: (required)
        :type hpc_analysis_request_body: HPCAnalysisRequestBody
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._hpcrequests_post_serialize(
            hpc_analysis_request_body=hpc_analysis_request_body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HPCRequestSubmission",
            '400': None,
            '500': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _hpcrequests_post_serialize(
        self,
        hpc_analysis_request_body,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if hpc_analysis_request_body is not None:
            _body_params = hpc_analysis_request_body


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'LIMSLogin', 
            'USEmail', 
            'USPassword'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/hpcrequests',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    async def hpcrequests_search_get(
        self,
        experiment_id: Annotated[Optional[StrictInt], Field(description="ID of experiment to search for")] = None,
        submit_time: Annotated[Optional[datetime], Field(description="Time of submission to search for")] = None,
        cluster: Annotated[Optional[StrictStr], Field(description="Cluster to search for")] = None,
        method: Annotated[Optional[HPCAnalysisMethod], Field(description="Method to search for")] = None,
        anal_type: Annotated[Optional[StrictStr], Field(description="Type of analysis to search for")] = None,
        status: Annotated[Optional[HPCAnalysisQueueStatus], Field(description="Status of request to search for")] = None,
        edited_data_id: Annotated[Optional[StrictInt], Field(description="ID of edited data to search for")] = None,
        gfac_id: Annotated[Optional[StrictInt], Field(description="ID of gfac to search for")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[HPCAnalysisRequest]:
        """hpcrequests_search_get

        Search for HPC analysis requests

        :param experiment_id: ID of experiment to search for
        :type experiment_id: int
        :param submit_time: Time of submission to search for
        :type submit_time: datetime
        :param cluster: Cluster to search for
        :type cluster: str
        :param method: Method to search for
        :type method: HPCAnalysisMethod
        :param anal_type: Type of analysis to search for
        :type anal_type: str
        :param status: Status of request to search for
        :type status: HPCAnalysisQueueStatus
        :param edited_data_id: ID of edited data to search for
        :type edited_data_id: int
        :param gfac_id: ID of gfac to search for
        :type gfac_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._hpcrequests_search_get_serialize(
            experiment_id=experiment_id,
            submit_time=submit_time,
            cluster=cluster,
            method=method,
            anal_type=anal_type,
            status=status,
            edited_data_id=edited_data_id,
            gfac_id=gfac_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[HPCAnalysisRequest]",
            '500': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def hpcrequests_search_get_with_http_info(
        self,
        experiment_id: Annotated[Optional[StrictInt], Field(description="ID of experiment to search for")] = None,
        submit_time: Annotated[Optional[datetime], Field(description="Time of submission to search for")] = None,
        cluster: Annotated[Optional[StrictStr], Field(description="Cluster to search for")] = None,
        method: Annotated[Optional[HPCAnalysisMethod], Field(description="Method to search for")] = None,
        anal_type: Annotated[Optional[StrictStr], Field(description="Type of analysis to search for")] = None,
        status: Annotated[Optional[HPCAnalysisQueueStatus], Field(description="Status of request to search for")] = None,
        edited_data_id: Annotated[Optional[StrictInt], Field(description="ID of edited data to search for")] = None,
        gfac_id: Annotated[Optional[StrictInt], Field(description="ID of gfac to search for")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[HPCAnalysisRequest]]:
        """hpcrequests_search_get

        Search for HPC analysis requests

        :param experiment_id: ID of experiment to search for
        :type experiment_id: int
        :param submit_time: Time of submission to search for
        :type submit_time: datetime
        :param cluster: Cluster to search for
        :type cluster: str
        :param method: Method to search for
        :type method: HPCAnalysisMethod
        :param anal_type: Type of analysis to search for
        :type anal_type: str
        :param status: Status of request to search for
        :type status: HPCAnalysisQueueStatus
        :param edited_data_id: ID of edited data to search for
        :type edited_data_id: int
        :param gfac_id: ID of gfac to search for
        :type gfac_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._hpcrequests_search_get_serialize(
            experiment_id=experiment_id,
            submit_time=submit_time,
            cluster=cluster,
            method=method,
            anal_type=anal_type,
            status=status,
            edited_data_id=edited_data_id,
            gfac_id=gfac_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[HPCAnalysisRequest]",
            '500': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def hpcrequests_search_get_without_preload_content(
        self,
        experiment_id: Annotated[Optional[StrictInt], Field(description="ID of experiment to search for")] = None,
        submit_time: Annotated[Optional[datetime], Field(description="Time of submission to search for")] = None,
        cluster: Annotated[Optional[StrictStr], Field(description="Cluster to search for")] = None,
        method: Annotated[Optional[HPCAnalysisMethod], Field(description="Method to search for")] = None,
        anal_type: Annotated[Optional[StrictStr], Field(description="Type of analysis to search for")] = None,
        status: Annotated[Optional[HPCAnalysisQueueStatus], Field(description="Status of request to search for")] = None,
        edited_data_id: Annotated[Optional[StrictInt], Field(description="ID of edited data to search for")] = None,
        gfac_id: Annotated[Optional[StrictInt], Field(description="ID of gfac to search for")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """hpcrequests_search_get

        Search for HPC analysis requests

        :param experiment_id: ID of experiment to search for
        :type experiment_id: int
        :param submit_time: Time of submission to search for
        :type submit_time: datetime
        :param cluster: Cluster to search for
        :type cluster: str
        :param method: Method to search for
        :type method: HPCAnalysisMethod
        :param anal_type: Type of analysis to search for
        :type anal_type: str
        :param status: Status of request to search for
        :type status: HPCAnalysisQueueStatus
        :param edited_data_id: ID of edited data to search for
        :type edited_data_id: int
        :param gfac_id: ID of gfac to search for
        :type gfac_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._hpcrequests_search_get_serialize(
            experiment_id=experiment_id,
            submit_time=submit_time,
            cluster=cluster,
            method=method,
            anal_type=anal_type,
            status=status,
            edited_data_id=edited_data_id,
            gfac_id=gfac_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[HPCAnalysisRequest]",
            '500': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _hpcrequests_search_get_serialize(
        self,
        experiment_id,
        submit_time,
        cluster,
        method,
        anal_type,
        status,
        edited_data_id,
        gfac_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if experiment_id is not None:
            
            _query_params.append(('experimentID', experiment_id))
            
        if submit_time is not None:
            if isinstance(submit_time, datetime):
                _query_params.append(
                    (
                        'submitTime',
                        submit_time.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('submitTime', submit_time))
            
        if cluster is not None:
            
            _query_params.append(('cluster', cluster))
            
        if method is not None:
            
            _query_params.append(('method', method.value))
            
        if anal_type is not None:
            
            _query_params.append(('analType', anal_type))
            
        if status is not None:
            
            _query_params.append(('status', status.value))
            
        if edited_data_id is not None:
            
            _query_params.append(('editedDataID', edited_data_id))
            
        if gfac_id is not None:
            
            _query_params.append(('gfacID', gfac_id))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'LIMSLogin', 
            'USEmail', 
            'USPassword'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/hpcrequests/search',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


