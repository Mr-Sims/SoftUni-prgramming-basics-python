from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.lost_and_found_app.validators import validate_max_value


class ValidateMaxValueTests(TestCase):

    def test_when_value_is_greater_than_max__expect_to_raise(self):
        value = 5
        validate_func = validate_max_value(value-1)
        with self.assertRaises(ValidationError) as context:
            validate_func(value)

        self.assertIsNotNone(context.exception)

    def test_when_value_is_lesser_than_max__expect_nothing(self):
        value = 5
        validate_func = validate_max_value(value + 1)
        validate_func(value)

    def test_when_value_is_equal_than_max__expect_nothing(self):
        value = 5
        validate_func = validate_max_value(value)
        validate_func(value)


# tests.object_posts.validators.test_validate_max_value