import os
from googleapiclient.http import MediaIoBaseUpload
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import io


class CreateGoogleDriveDocument(APIView):
    """
    API View for creating a document in Google Drive.

    Methods:
    - post(self, request, *args, **kwargs): Handles POST requests to create a document in Google Drive.
    - get_folder_id(cls, service, folder_name): Retrieves the folder ID by name from Google Drive.

    Example:
    ```
    POST /api/v1/test_API/create-document/
    {
        "data": "Lorem ipsum...",
        "name": "example.txt"
    }
    ```
    """

    @classmethod
    def get_folder_id(cls, service, folder_name):
        """
        Retrieves the Google Drive folder ID based on the folder name.

        Args:
        - service: The authenticated Google Drive API service.
        - folder_name: The name of the folder.

        Returns:
        - str: The folder ID if found.

        Raises:
        - ValueError: If the folder with the specified name is not found.
        """

        # Получаем идентификатор папки по ее имени
        results = service.files().list(
            q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'").execute()
        items = results.get('files', [])
        if items:
            return items[0]['id']
        else:
            raise ValueError(f"Папка '{folder_name}' не найдена на Google Drive.")

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a document in Google Drive.

        Args:
        - request: The HTTP request object.
        - args: Additional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: The HTTP response indicating the success or failure of the request.
        """

        # Получаем имя и контент файла из запроса
        data = request.data.get('data')
        name = request.data.get('name')

        # Получаем свои credentials
        if os.path.exists('credentials.json'):
            credentials = Credentials.from_authorized_user_file('credentials.json')
        else:
            return Response({'error': "Credentials are not valid or does not exist"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Авторизация
        service = build('drive', 'v3', credentials=credentials)

        # Используем MediaIoBaseUpload для загрузки данных
        media = MediaIoBaseUpload(io.BytesIO(data.encode()), mimetype='text/plain', resumable=True)

        # Получаем идентификатор папки "Test_API"
        folder_id = self.get_folder_id(service, 'Test_API')

        # Создаем файл в Google Drive
        file_metadata = {'name': name, 'mimeType': 'text/plain', 'parents': [folder_id]}
        media = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        return Response({'file_id': media.get('id')}, status=status.HTTP_201_CREATED)
