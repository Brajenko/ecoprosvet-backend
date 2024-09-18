from django.urls import path, include

from .views import CreateUserView, RetrieveUpdateDeleteUserView

urlpatterns = [
    path('', CreateUserView.as_view(), name='register'),
    path('me/', RetrieveUpdateDeleteUserView.as_view(), name='me'),
]
