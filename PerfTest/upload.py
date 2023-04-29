from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from django.conf import settings
import requests

def upload_azure_storage(file):
    # Replace with your Azure Storage account connection string
    connection_string = settings.AZURE_STORAGE_CONNECTION_STRING

    # Replace with your Azure Storage container name
    container_name = "your-container-name"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create a ContainerClient
    container_client = blob_service_client.get_container_client(container_name)

    # Upload the file to Azure Blob Storage
    blob_client = container_client.get_blob_client(file.name)
    blob_client.upload_blob(file)

def upload_ipfs_storage(file):
    # Replace with your Pinata API key and secret
    pinata_api_key = settings.PINATA_API_KEY
    pinata_secret_api_key = settings.PINATA_SECRET_API_KEY

    # Pinata API endpoint for pinning a file
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    # Read the file and create a multipart form request
    with open(file.path, 'rb') as f:
        files = {'file': (file.name, f)}
        headers = {
            "pinata_api_key": pinata_api_key,
            "pinata_secret_api_key": pinata_secret_api_key,
        }

        # Upload the file to IPFS via Pinata
        response = requests.post(url, files=files, headers=headers)

        if response.status_code == 200:
            print("File uploaded to IPFS:", response.json())
        else:
            print("Failed to upload file to IPFS:", response.text)

