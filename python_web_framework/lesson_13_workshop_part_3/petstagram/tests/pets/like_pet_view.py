from django.urls import reverse

from petstagram.pets.models import Pet, Like
from tests.base.mixins import PetTestUtils, UserTestUtils
from tests.base.tests import PetstagramTestCase


class LikePetViewTest(PetTestUtils, UserTestUtils, PetstagramTestCase):

    def test_likePet__whenPetNotLiked_shouldCreateLike(self):
        self.client.force_login(self.user)
        pet_user = self.create_user(
            email='pet@abv.bg',
            password='mazen',
        )
        pet = self.create_pet(
            name='Test Pet',
            description='Test pet description',
            type=Pet.TYPE_CHOICE_DOG,
            age=1,
            image='path/to/image.png',
            user=pet_user,
        )

        response = self.client.post(reverse('like pet', kwargs={
            'pk': pet.id,
        }))
        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            pet_id=pet.id,
        ).exists()

        self.assertTrue(like_exists)


    def test_likePet_whenPetAlreadyLiked_shouldDeleteTheLike(self):
        self.client.force_login(self.user)
        pet_user = self.create_user(
            email='pet@abv.bg',
            password='mazen',
        )
        pet = self.create_pet_with_like(
            like_user=self.user,
            name='Test Pet',
            description='Test pet description',
            type=Pet.TYPE_CHOICE_DOG,
            age=1,
            image='path/to/image.png',
            user=pet_user,
        )

        response = self.client.post(reverse('like pet', kwargs={
            'pk': pet.id,
        }))
        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            pet_id=pet.id,
        ).exists()

        self.assertFalse(like_exists)
