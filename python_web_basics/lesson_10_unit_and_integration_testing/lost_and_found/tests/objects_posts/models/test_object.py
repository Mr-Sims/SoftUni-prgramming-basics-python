from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.lost_and_found_app.models import Object


class ObjectTests(TestCase):
    valid_name = 'object1'
    valid_image = 'http://image.com'
    valid_width = 2
    valid_height = 1
    valid_weight = 1.2

    def test__when_width_is_less_than_3__expect_raise(self):
        width = 2
        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )
        with self.assertRaises(ValidationError) as context:
            obj.full_clean()
            obj.save()
        self.assertIsNotNone(context.exception)

    def test__when_width_is_equal_to_3__expect_success(self):
        width = 3
        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )
        obj.full_clean()
        obj.save()

    def test__when_width_is_greater_than_600__expect_raise(self):
        width = 601
        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )
        with self.assertRaises(ValidationError) as context:
            obj.full_clean()
            obj.save()
        self.assertIsNotNone(context.exception)

    def test__when_width_is_equal_to_600_expect_success(self):
        width = 600
        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )

        obj.full_clean()
        obj.save()

    def test__when_width_is_between_3_and_600_expect_success(self):
        width = 20
        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )

        obj.full_clean()
        obj.save()

