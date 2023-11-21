from django.urls import path
from .views import CreateGoogleDriveDocument

urlpatterns = [
    path('create-document/', CreateGoogleDriveDocument.as_view(), name='create-google-drive-document'),
]
