# GoogleDrive-Document-Creation


# Create Google Drive Document API

This repository contains a Django REST framework (DRF) API view for creating a document in Google Drive. The API allows you to submit text data and a filename, and it will create a corresponding file in a specified folder on Google Drive.

## Usage

### Prerequisites

Make sure you have Docker and Docker Compose installed on your system.

### Run with Docker

1. Clone the repository:

   ```bash
   git clone [https://github.com/VadimPoliakov/Create-GoogleDrive-Document](https://github.com/VadimPoliakov/GoogleDrive-Document-Creation).git
   cd GoogleDrive-Document-Creation


2. Build the Docker image:

   ```bash
   docker build -t create-google-drive-doc .
   ```

3. Run the Docker container:

   ```bash
   docker run -p 8000:8000 create-google-drive-doc
   ```

4. Access the API at [http://localhost:8000/api/v1/test_API/create-document/](http://localhost:8000/api/v1/test_API/create-document/).

## API Documentation

### `POST /api/v1/test_API/create-document/`

Create a document in Google Drive.

**Request Body:**

```json
{
    "data": "Lorem ipsum...",
    "name": "example.txt"
}
```

**Response:**

```json
{
    "file_id": "your_generated_file_id"
}
```

## Additional Commands

### Database Migrations

```bash
docker run create-google-drive-doc python manage.py migrate
```
