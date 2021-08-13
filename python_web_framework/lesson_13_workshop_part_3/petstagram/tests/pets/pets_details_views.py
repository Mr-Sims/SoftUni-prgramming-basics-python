from django.urls import reverse

from petstagram.pets.models import Pet, Like
from tests.base.mixins import PetTestUtils, UserTestUtils
from tests.base.tests import PetstagramTestCase


class PetDetailsTest(PetTestUtils, UserTestUtils, PetstagramTestCase):
    def test_getPetDetails_whenPetDoesNotExistAndIsOwner_shouldReturnDetailsForOwner(self):
        pass

    def test_getPetDetails_whenPetExistsAndIsOwner_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        pet = self.create_pet(
            name='Test Pet',
            description='Test pet description',
            type=Pet.TYPE_CHOICE_DOG,
            age=1,
            image='path/to/image.png',
            user=self.user,
        )
        response = self.client.get(reverse('pet details', kwargs={
            'pk': pet.id
        }))
        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_getPetDetails_whenPetExistsAndIsNotOwnerAndNotLiked_shouldReturnDetailsForOwner(self):
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

        response = self.client.get(reverse('pet details', kwargs={
            'pk': pet.id
        }))
        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_getPetDetails_whenPetExistsAndIsNotOwnerAndLiked_shouldReturnDetailsForOwner(self):
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

        response = self.client.get(reverse('pet details', kwargs={
            'pk': pet.id
        }))
        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])
