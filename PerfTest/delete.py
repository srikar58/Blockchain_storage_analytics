import requests
from azure.storage.blob import BlobServiceClient
from django.conf import settings

# Delete from Azure Blob Storage
def delete_from_azure_storage(file_name):
    connection_string = settings.AZURE_STORAGE_CONNECTION_STRING
    container_name = "your-container-name"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(file_name)

    blob_client.delete_blob()

# Delete from IPFS using Pinata
def delete_from_ipfs_storage(file_name):
    pinata_api_key = settings.PINATA_API_KEY
    pinata_secret_api_key = settings.PINATA_SECRET_API_KEY

    # Assuming the file_name is the IPFS hash
    ipfs_hash = file_name

    # Build the URL to unpin the file from Pinata
    url = "https://api.pinata.cloud/pinning/unpin/"

    headers = {
        "pinata_api_key": pinata_api_key,
        "pinata_secret_api_key": pinata_secret_api_key,
    }

    response = requests.delete(url + ipfs_hash, headers=headers)

    if response.status_code != 200:
        print("Failed to unpin file from IPFS:", response.text)
