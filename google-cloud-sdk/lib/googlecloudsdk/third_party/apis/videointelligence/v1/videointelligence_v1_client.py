"""Generated client library for videointelligence version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.videointelligence.v1 import videointelligence_v1_messages as messages


class VideointelligenceV1(base_api.BaseApiClient):
  """Generated client library for service videointelligence version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://videointelligence.googleapis.com/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'videointelligence'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'VideointelligenceV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new videointelligence handle."""
    url = url or self.BASE_URL
    super(VideointelligenceV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations_projects_locations_operations = self.OperationsProjectsLocationsOperationsService(self)
    self.operations_projects_locations = self.OperationsProjectsLocationsService(self)
    self.operations_projects = self.OperationsProjectsService(self)
    self.operations = self.OperationsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)
    self.videos = self.VideosService(self)

  class OperationsProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the operations_projects_locations_operations resource."""

    _NAME = u'operations_projects_locations_operations'

    def __init__(self, client):
      super(VideointelligenceV1.OperationsProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (VideointelligenceOperationsProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'videointelligence.operations.projects.locations.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/operations/{+name}:cancel',
        request_field='',
        request_type_name=u'VideointelligenceOperationsProjectsLocationsOperationsCancelRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (VideointelligenceOperationsProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'videointelligence.operations.projects.locations.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/operations/{+name}',
        request_field='',
        request_type_name=u'VideointelligenceOperationsProjectsLocationsOperationsDeleteRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (VideointelligenceOperationsProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'videointelligence.operations.projects.locations.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/operations/{+name}',
        request_field='',
        request_type_name=u'VideointelligenceOperationsProjectsLocationsOperationsGetRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

  class OperationsProjectsLocationsService(base_api.BaseApiService):
    """Service class for the operations_projects_locations resource."""

    _NAME = u'operations_projects_locations'

    def __init__(self, client):
      super(VideointelligenceV1.OperationsProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class OperationsProjectsService(base_api.BaseApiService):
    """Service class for the operations_projects resource."""

    _NAME = u'operations_projects'

    def __init__(self, client):
      super(VideointelligenceV1.OperationsProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(VideointelligenceV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = u'projects_locations_operations'

    def __init__(self, client):
      super(VideointelligenceV1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (VideointelligenceProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'videointelligence.projects.locations.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field=u'googleLongrunningCancelOperationRequest',
        request_type_name=u'VideointelligenceProjectsLocationsOperationsCancelRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (VideointelligenceProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'videointelligence.projects.locations.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'VideointelligenceProjectsLocationsOperationsDeleteRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (VideointelligenceProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'videointelligence.projects.locations.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'VideointelligenceProjectsLocationsOperationsGetRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (VideointelligenceProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method=u'GET',
        method_id=u'videointelligence.projects.locations.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}/operations',
        request_field='',
        request_type_name=u'VideointelligenceProjectsLocationsOperationsListRequest',
        response_type_name=u'GoogleLongrunningListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(VideointelligenceV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(VideointelligenceV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class VideosService(base_api.BaseApiService):
    """Service class for the videos resource."""

    _NAME = u'videos'

    def __init__(self, client):
      super(VideointelligenceV1.VideosService, self).__init__(client)
      self._upload_configs = {
          }

    def Annotate(self, request, global_params=None):
      r"""Performs asynchronous video annotation. Progress and results can be.
retrieved through the `google.longrunning.Operations` interface.
`Operation.metadata` contains `AnnotateVideoProgress` (progress).
`Operation.response` contains `AnnotateVideoResponse` (results).

      Args:
        request: (GoogleCloudVideointelligenceV1AnnotateVideoRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Annotate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Annotate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'videointelligence.videos.annotate',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/videos:annotate',
        request_field='<request>',
        request_type_name=u'GoogleCloudVideointelligenceV1AnnotateVideoRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )
