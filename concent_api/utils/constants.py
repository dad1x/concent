import enum


class ErrorCode(enum.Enum):
    REQUEST_BODY_NOT_EMPTY                                              = 'request_body.not_empty'
    AUTH_CLIENT_AUTH_MESSAGE_MISSING                                    = 'header.client_public_key.missing'
    AUTH_CLIENT_AUTH_MESSAGE_INVALID                                    = 'header.client_public_key.invalid'
    CONCENT_APPLICATION_CRASH                                           = 'concent.application_crash'
    HEADER_AUTHORIZATION_MISSING                                        = 'header.authorization.missing'
    HEADER_AUTHORIZATION_MISSING_TOKEN                                  = 'header.authorization.missing_token'
    HEADER_AUTHORIZATION_TOKEN_INVALID_MESSAGE                          = 'header.authorization.token_not_valid_message'
    HEADER_AUTHORIZATION_UNRECOGNIZED_SCHEME                            = 'header.authorization.unrecognized_scheme'
    HEADER_AUTHORIZATION_NOT_BASE64_ENCODED_VALUE                       = 'header.authorization.not_base64_encoded_value'
    HEADER_CONTENT_TYPE_NOT_SUPPORTED                                   = 'header.content_type.not_supported'
    MESSAGE_AUTHORIZED_CLIENT_PUBLIC_KEY_UNAUTHORIZED_CLIENT            = 'message.authorized_client_public_key_unauthorized_client'
    MESSAGE_AUTHORIZED_CLIENT_PUBLIC_KEY_WRONG_TYPE                     = 'message.authorized_client_public_key_wrong_type'
    MESSAGE_FILES_CHECKSUM_EMPTY                                        = 'message.files.checksum.empty'
    MESSAGE_FILES_CHECKSUM_INVALID_SHA1_HASH                            = 'message.files.checksum.invalid_sha1_hash'
    MESSAGE_FILES_CHECKSUM_INVALID_ALGORITHM                            = 'message.files.checksum.invalid_algorithm'
    MESSAGE_FILES_CHECKSUM_WRONG_FORMAT                                 = 'message.files.checksum.wrong_format'
    MESSAGE_FILES_CHECKSUM_WRONG_TYPE                                   = 'message.files.checksum.wrong_type'
    MESSAGE_FILES_PATH_NOT_LISTED_IN_FILES                              = 'message.files.path.not_listed_in_files'
    MESSAGE_FILES_PATHS_NOT_UNIQUE                                      = 'message.files.paths.not_unique'
    MESSAGE_FILES_SIZE_EMPTY                                            = 'message.files.size.empty'
    MESSAGE_FILES_SIZE_NEGATIVE                                         = 'message.files.size.negative'
    MESSAGE_FILES_SIZE_WRONG_TYPE                                       = 'message.files.size.wrong_type'
    MESSAGE_FILES_WRONG_TYPE                                            = 'message.files.wrong_type'
    MESSAGE_OPERATION_INVALID                                           = 'message.operation.invalid'
    MESSAGE_SIGNATURE_MISSING                                           = 'message.signature.missing'
    MESSAGE_STORAGE_CLUSTER_INVALID_URL                                 = 'message.storage_cluster_invalid_url'
    MESSAGE_STORAGE_CLUSTER_WRONG_CLUSTER                               = 'message.storage_cluster_wrong_cluster'
    MESSAGE_STORAGE_CLUSTER_WRONG_TYPE                                  = 'message.storage_cluster_wrong_type'
    MESSAGE_TOKEN_EXPIRATION_DEADLINE_PASSED                            = 'message.token_expiration_deadline_passed'
    MESSAGE_TOKEN_EXPIRATION_DEADLINE_WRONG_TYPE                        = 'message.token_expiration_deadline_wrong_type'
    MESSAGE_UNABLE_TO_DESERIALIZE                                       = 'message.unable_to_deserialize'
