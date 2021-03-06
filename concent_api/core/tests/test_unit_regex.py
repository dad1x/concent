from assertpy import assert_that

from core.constants import REGEX_FOR_VALID_UUID
from core.tests.utils import generate_uuid_for_tests


class TestRegexForValidUUID:
    def test_that_regex_matches_uuid(self):  # pylint: disable=no-self-use
        assert_that(generate_uuid_for_tests()).matches(REGEX_FOR_VALID_UUID)
