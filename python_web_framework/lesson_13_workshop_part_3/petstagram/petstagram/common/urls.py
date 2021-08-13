# common.urls.py

from django.urls import path

from petstagram.common.views import landing_page, LandingPage


urlpatterns = [
    path('', LandingPage.as_view(), name='landing page')
]
