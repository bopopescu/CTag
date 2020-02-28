"""Generated message classes for cloudshell version v1.

Allows users to start, configure, and connect to interactive shell sessions
running in the cloud.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudshell'


class CancelOperationRequest(_messages.Message):
  r"""The request message for Operations.CancelOperation."""


class CloudshellOperationsCancelRequest(_messages.Message):
  r"""A CloudshellOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class CloudshellOperationsDeleteRequest(_messages.Message):
  r"""A CloudshellOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class CloudshellOperationsGetRequest(_messages.Message):
  r"""A CloudshellOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class CloudshellOperationsListRequest(_messages.Message):
  r"""A CloudshellOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class Environment(_messages.Message):
  r"""A Cloud Shell environment, which is defined as the combination of a
  Docker image specifying what is installed on the environment and a home
  directory containing the user's data that will remain across sessions. Each
  user has a single environment with the ID "default".

  Enums:
    SizeValueValuesEnum: Indicates the size of the backing VM running the
      environment.  If set to something other than DEFAULT, it will be
      reverted to the default VM size after vm_size_expire_time.
    StateValueValuesEnum: Output only. Current execution state of this
      environment.

  Fields:
    dockerImage: Required. Full path to the Docker image used to run this
      environment, e.g. "gcr.io/dev-con/cloud-devshell:latest".
    id: Output only. The environment's identifier, unique among the user's
      environments.
    name: Output only. Full name of this resource, in the format
      `users/{owner_email}/environments/{environment_id}`. `{owner_email}` is
      the email address of the user to whom this environment belongs, and
      `{environment_id}` is the identifier of this environment. For example,
      `users/someone@example.com/environments/default`.
    publicKeys: Output only. Public keys associated with the environment.
      Clients can connect to this environment via SSH only if they possess a
      private key corresponding to at least one of these public keys. Keys can
      be added to or removed from the environment using the CreatePublicKey
      and DeletePublicKey methods.
    size: Indicates the size of the backing VM running the environment.  If
      set to something other than DEFAULT, it will be reverted to the default
      VM size after vm_size_expire_time.
    sshHost: Output only. Host to which clients can connect to initiate SSH
      sessions with the environment.
    sshPort: Output only. Port to which clients can connect to initiate SSH
      sessions with the environment.
    sshUsername: Output only. Username that clients should use when initiating
      SSH sessions with the environment.
    state: Output only. Current execution state of this environment.
    vmSizeExpireTime: Output only. The time when the Environment will expire
      back to the default VM size.
    webHost: Output only. Host to which clients can connect to initiate HTTPS
      or WSS connections with the environment.
    webPorts: Output only. Ports to which clients can connect to initiate
      HTTPS or WSS connections with the environment.
  """

  class SizeValueValuesEnum(_messages.Enum):
    r"""Indicates the size of the backing VM running the environment.  If set
    to something other than DEFAULT, it will be reverted to the default VM
    size after vm_size_expire_time.

    Values:
      VM_SIZE_UNSPECIFIED: The VM size is unknown.
      DEFAULT: The default VM size.
      BOOSTED: The boosted VM size.
    """
    VM_SIZE_UNSPECIFIED = 0
    DEFAULT = 1
    BOOSTED = 2

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. Current execution state of this environment.

    Values:
      STATE_UNSPECIFIED: The environment's states is unknown.
      DISABLED: The environment is not running and can't be connected to.
        Starting the environment will transition it to the STARTING state.
      STARTING: The environment is being started but is not yet ready to
        accept connections.
      RUNNING: The environment is running and ready to accept connections. It
        will automatically transition back to DISABLED after a period of
        inactivity or if another environment is started.
    """
    STATE_UNSPECIFIED = 0
    DISABLED = 1
    STARTING = 2
    RUNNING = 3

  dockerImage = _messages.StringField(1)
  id = _messages.StringField(2)
  name = _messages.StringField(3)
  publicKeys = _messages.MessageField('PublicKey', 4, repeated=True)
  size = _messages.EnumField('SizeValueValuesEnum', 5)
  sshHost = _messages.StringField(6)
  sshPort = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  sshUsername = _messages.StringField(8)
  state = _messages.EnumField('StateValueValuesEnum', 9)
  vmSizeExpireTime = _messages.StringField(10)
  webHost = _messages.StringField(11)
  webPorts = _messages.IntegerField(12, repeated=True, variant=_messages.Variant.INT32)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class PublicKey(_messages.Message):
  r"""A public SSH key, corresponding to a private SSH key held by the client.

  Enums:
    FormatValueValuesEnum: Required. Format of this key's content.

  Fields:
    format: Required. Format of this key's content.
    key: Required. Content of this key.
    name: Output only. Full name of this resource, in the format
      `users/{owner_email}/environments/{environment_id}/publicKeys/{key_id}`.
      `{owner_email}` is the email address of the user to whom the key
      belongs. `{environment_id}` is the identifier of the environment to
      which the key grants access. `{key_id}` is the unique identifier of the
      key. For example,
      `users/someone@example.com/environments/default/publicKeys/myKey`.
  """

  class FormatValueValuesEnum(_messages.Enum):
    r"""Required. Format of this key's content.

    Values:
      FORMAT_UNSPECIFIED: Unknown format. Do not use.
      SSH_DSS: `ssh-dss` key format (see RFC4253).
      SSH_RSA: `ssh-rsa` key format (see RFC4253).
      ECDSA_SHA2_NISTP256: `ecdsa-sha2-nistp256` key format (see RFC5656).
      ECDSA_SHA2_NISTP384: `ecdsa-sha2-nistp384` key format (see RFC5656).
      ECDSA_SHA2_NISTP521: `ecdsa-sha2-nistp521` key format (see RFC5656).
    """
    FORMAT_UNSPECIFIED = 0
    SSH_DSS = 1
    SSH_RSA = 2
    ECDSA_SHA2_NISTP256 = 3
    ECDSA_SHA2_NISTP384 = 4
    ECDSA_SHA2_NISTP521 = 5

  format = _messages.EnumField('FormatValueValuesEnum', 1)
  key = _messages.BytesField(2)
  name = _messages.StringField(3)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class StartEnvironmentMetadata(_messages.Message):
  r"""Message included in the metadata field of operations returned from
  StartEnvironment.

  Enums:
    StateValueValuesEnum: Current state of the environment being started.

  Fields:
    state: Current state of the environment being started.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Current state of the environment being started.

    Values:
      STATE_UNSPECIFIED: The environment's start state is unknown.
      STARTING: The environment is in the process of being started, but no
        additional details are available.
      UNARCHIVING_DISK: Startup is waiting for the user's disk to be
        unarchived. This can happen when the user returns to Cloud Shell after
        not having used it for a while, and suggests that startup will take
        longer than normal.
      AWAITING_VM: Startup is waiting for a VM to be assigned to the
        environment. This should normally happen very quickly, but an
        environment might stay in this state for an extended period of time if
        the system is experiencing heavy load.
      FINISHED: Startup is complete and the user should be able to establish
        an SSH connection to their environment.
    """
    STATE_UNSPECIFIED = 0
    STARTING = 1
    UNARCHIVING_DISK = 2
    AWAITING_VM = 3
    FINISHED = 4

  state = _messages.EnumField('StateValueValuesEnum', 1)


class StartEnvironmentResponse(_messages.Message):
  r"""Message included in the response field of operations returned from
  StartEnvironment once the operation is complete.

  Fields:
    environment: Environment that was started.
  """

  environment = _messages.MessageField('Environment', 1)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
