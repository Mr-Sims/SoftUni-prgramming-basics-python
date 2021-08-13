from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet

UserModel = get_user_model()


class ProfileDetailsTest(TestCase):
    def setUp(self) -> None:
        self.Client = Client
        self.user = UserModel.objects.create_user(email='pizza@abv.bg', password='mazen')

    def test_get_details__when_logged_in_user_should_get_details_with_no_pets(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        pets = list(response.context['pets'])
        profile = response.context['profile']

        self.assertEqual(200, response.status_code)
        self.assertListEqual(pets, [])
        self.assertEqual(self.user.id, profile.user_id)

    def test_get_details__when_logged_in_user_should_get_details_with_pets(self):
        pet = Pet.objects.create(
            name='Test Pet',
            description='Test pet description',
            type=Pet.TYPE_CHOICE_DOG,
            age=1,
            image='path/to/image.png',
            user=self.user,
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        pets = list(response.context['pets'])
        profile = response.context['profile']

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, profile.user_id)
        self.assertEqual([pet], pets)

#bellow tests not finnished
    def test_post_details__when_user_logged_in_without_image__should_change_image(self):
        path_to_image = 'path/to/image.png'
        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={'profile_image': path_to_image})
        self.assertEqual(302 , response.status_code)
        profile = Profile.objects.get(pk=self.user.id)

        # self.assertEqual(path_to_image, profile.profile_image.path)

    def test_post_details__when_user_logged_in_with_image__should_change_image(self):
        path_to_image = 'path/to/image.png'
        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()
        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={'profile_image': path_to_image})
        self.assertEqual(302 , response.status_code)
        profile = Profile.objects.get(pk=self.user.id)

        # self.assertEqual(path_to_image, profile.profile_image.path)