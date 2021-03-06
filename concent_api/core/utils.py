import datetime
import math
import random
import uuid
from logging import getLogger
from typing import Optional

from django.conf import settings
from django.http import HttpRequest
from golem_messages import message
from golem_messages.helpers import maximum_download_time
from golem_messages.helpers import subtask_verification_time
from golem_messages.utils import decode_hex

from common.constants import ErrorCode
from common.helpers import get_current_utc_timestamp
from common.helpers import parse_timestamp_to_utc_datetime
from core.exceptions import Http400
from core.exceptions import SceneFilePathError
from .constants import GOLEM_PUBLIC_KEY_HEX_LENGTH
from .constants import GOLEM_PUBLIC_KEY_LENGTH
from .constants import VALID_SCENE_FILE_PREFIXES

logger = getLogger(__name__)


def calculate_maximum_download_time(size: int, rate: int) -> int:
    """
    This function calls `maximum_download_time` helper function from golem messages or Concent custom implementation
    of it, depending on CUSTOM_PROTOCOL_TIMES setting value.
    The reason for using custom implementation is because it has hard-coded values and we cannot make it use values
    from our settings.
    """
    assert isinstance(size, int)
    assert isinstance(rate, int)
    assert size > 0
    assert rate > 0
    assert settings.DOWNLOAD_LEADIN_TIME > 0

    if settings.CUSTOM_PROTOCOL_TIMES:
        bytes_per_sec = rate << 10
        download_time = int(
            datetime.timedelta(
                seconds=int(math.ceil(size / bytes_per_sec))
            ).total_seconds()
        )

        return settings.DOWNLOAD_LEADIN_TIME + download_time
    else:
        return int(maximum_download_time(size, rate).total_seconds())


def calculate_subtask_verification_time(report_computed_task: message.ReportComputedTask) -> int:
    """
    This function calls `subtask_verification_time` helper function from golem messages or Concent custom implementation
    of it, depending on CUSTOM_PROTOCOL_TIMES setting value.
    The reason for using custom implementation is because it has hard-coded values and we cannot make it use values
    from our settings.
    """
    assert isinstance(report_computed_task, message.ReportComputedTask)

    if settings.CUSTOM_PROTOCOL_TIMES:
        mdt = calculate_maximum_download_time(
            size=report_computed_task.size,
            rate=settings.MINIMUM_UPLOAD_RATE
        )
        ttc_dt = parse_timestamp_to_utc_datetime(
            report_computed_task.task_to_compute.timestamp,
        )
        subtask_dt = parse_timestamp_to_utc_datetime(
            report_computed_task.task_to_compute.compute_task_def['deadline'],
        )
        subtask_timeout = subtask_dt - ttc_dt

        return int(
            (4 * settings.CONCENT_MESSAGING_TIME) +
            (3 * mdt) +
            (0.5 * subtask_timeout.total_seconds())
        )
    else:
        return int(subtask_verification_time(report_computed_task).total_seconds())


def calculate_concent_verification_time(task_to_compute: message.TaskToCompute) -> int:
    """ This function calculates a value referenced in documentation as CONCENT VERIFICATION TIME. """
    assert isinstance(task_to_compute, message.TaskToCompute)

    return int(
        (task_to_compute.compute_task_def['deadline'] - task_to_compute.timestamp) *
        settings.ADDITIONAL_VERIFICATION_TIME_MULTIPLIER /
        settings.BLENDER_THREADS
    )


def hex_to_bytes_convert(client_public_key: str) -> bytes:
    if not isinstance(client_public_key, str):
        raise Http400(
            "Client public key must be string",
            error_code=ErrorCode.MESSAGE_VALUE_NOT_STRING
        )
    if not len(client_public_key) == GOLEM_PUBLIC_KEY_HEX_LENGTH:
        raise Http400(
            "Client public key must be length of 128 characters",
            error_code=ErrorCode.MESSAGE_VALUE_WRONG_LENGTH
        )
    key_bytes = decode_hex(client_public_key)
    assert len(key_bytes) == GOLEM_PUBLIC_KEY_LENGTH
    return key_bytes


def extract_name_from_scene_file_path(absoulte_scene_file_path_in_docker: str) -> str:
    for golem_resources_path in VALID_SCENE_FILE_PREFIXES:
        if absoulte_scene_file_path_in_docker.startswith(golem_resources_path):
            relative_scene_file_path_in_archive = absoulte_scene_file_path_in_docker[len(golem_resources_path):]
            break
    else:
        raise SceneFilePathError(
            f'Scene file should starts with one of available scene file paths: {VALID_SCENE_FILE_PREFIXES}',
            ErrorCode.MESSAGE_INVALID
        )
    return relative_scene_file_path_in_archive


def is_protocol_version_compatible(protocol_version: str) -> bool:
    """
    Versions are considered compatible if they share the minor and major version number. E.g 2.18.5 is compatible with
    2.18.1 but not with 2.17.5 or 3.0.0. This supports semver version style https://semver.org/
    """
    major, minor, _ = protocol_version.split('.')
    concent_major, concent_minor, _ = settings.GOLEM_MESSAGES_VERSION.split('.')
    return major == concent_major and minor == concent_minor


def is_given_golem_messages_version_supported_by_concent(
    request: HttpRequest,
) -> bool:
    """
    If header is missing version is not checked and Concent assumes that client uses compatible version.
    """
    if 'HTTP_X_Golem_Messages' not in request.META:
        return True
    else:
        golem_message_version = request.META['HTTP_X_Golem_Messages']
        if not is_protocol_version_compatible(golem_message_version):
            return False
        return True


def generate_uuid(seed: Optional[int] = None) -> str:
    if seed is None:
        seed = get_current_utc_timestamp()
    random.seed(seed)
    random_bits = "%32x" % random.getrandbits(128)
    # for UUID4 not all bits are random, see: en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_.28random.29
    string_for_uuid = random_bits[:12] + '4' + random_bits[13:16] + 'a' + random_bits[17:]
    generated = str(uuid.UUID(string_for_uuid))
    return generated


def adjust_transaction_hash(tx_hash: str) -> str:
    if tx_hash.startswith('0x'):
        return tx_hash[2:]
    return tx_hash
