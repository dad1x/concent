# pylint: disable=unused-wildcard-import
from .base import *  # NOQA  # pylint: disable=wildcard-import
from .development import *  # NOQA  # pylint: disable=wildcard-import


# To use this settings uncomment environment that You would like to test.
# For example testing staging cluster require only STAGING settings, while LOCAL and DEV remains commented.

# LOCAL SETTINGS

# STORAGE_CLUSTER_ADDRESS = 'http://localhost:8001/'
#
# CONCENT_MESSAGING_TIME = 5
# FORCE_ACCEPTANCE_TIME = 15
# MINIMUM_UPLOAD_RATE = 48
# PAYMENT_DUE_TIME = 40
# DOWNLOAD_LEADIN_TIME = 3
# SUBTASK_VERIFICATION_TIME = 10
# BLENDER_MAX_RENDERING_TIME = 10
# ADDITIONAL_VERIFICATION_CALL_TIME = 30
# CUSTOM_PROTOCOL_TIMES = True
# STORAGE_SERVER_INTERNAL_ADDRESS = 'http://localhost:8001/'


# DEV SETTINGS

# STORAGE_CLUSTER_ADDRESS = 'http://devel.concent.golem.network/'
#
# CONCENT_MESSAGING_TIME = 5
# FORCE_ACCEPTANCE_TIME = 15
# MINIMUM_UPLOAD_RATE = 48
# PAYMENT_DUE_TIME = 40
# DOWNLOAD_LEADIN_TIME = 3
# SUBTASK_VERIFICATION_TIME = 10
# BLENDER_MAX_RENDERING_TIME = 10
# ADDITIONAL_VERIFICATION_CALL_TIME = 30
# CUSTOM_PROTOCOL_TIMES = True


# STAGING SETTINGS
STORAGE_CLUSTER_ADDRESS = 'https://staging.concent.golem.network/'
CONCENT_PUBLIC_KEY = b'b\x9b>\xf3\xb3\xefW\x92\x93\xfeIW\xd1\n\xf0j\x91\t\xdf\x95\x84\x81b6C\xe8\xe0\xdb\\.P\x00;rZM\xafQI\xf7G\x95\xe3\xe3.h\x19\xf1\x0f\xfa\x8c\xed\x12:\x88\x8aK\x00C9 \xf0~P'
