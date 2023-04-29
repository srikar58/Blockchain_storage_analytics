import io
import requests
from azure.storage.blob import BlobServiceClient
from django.conf import settings

# Download from Azure Blob Storage
def download_from_azure_storage(file_name):
    connection_string = settings.AZURE_STORAGE_CONNECTION_STRING
    container_name = "your-container-name"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(file_name)
    
    stream = io.BytesIO()
    blob_data = blob_client.download_blob()
    blob_data.readinto(stream)
    stream.seek(0)

    return stream

# Download from IPFS using Pinata
def download_from_ipfs_storage(file_name):
    pinata_api_key = settings.PINATA_API_KEY
    pinata_secret_api_key = settings.PINATA_SECRET_API_KEY

    # Assuming the file_name is the IPFS hash
    ipfs_hash = file_name

    # Build the URL to download the file from the IPFS gateway
    url = f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}"

    headers = {
        "pinata_api_key": pinata_api_key,
        "pinata_secret_api_key": pinata_secret_api_key,
    }

    response = requests.get(url, stream=True, headers=headers)

    if response.status_code == 200:
        stream = io.BytesIO(response.content)
        stream.seek(0)
        return stream
    else:
        print("Failed to download file from IPFS:", response.text)
        return None
