import requests
from azure.storage.blob import BlobServiceClient
from django.conf import settings

# Delete from Azure Blob Storage
def delete_from_azure_storage(file_identifier):
    connection_string = settings.AZURE_STORAGE_CONNECTION_STRING
    container_name = "your-container-name"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(file_identifier)

    blob_client.delete_blob()

# Delete from IPFS using Pinata
def delete_from_ipfs_storage(file_identifier):
    pinata_api_key = settings.PINATA_API_KEY
    pinata_secret_api_key = settings.PINATA_SECRET_API_KEY

    # Assuming the file_identifier is the IPFS hash
    ipfs_hash = file_identifier

    # Build the URL to unpin the file from Pinata
    url = "https://api.pinata.cloud/pinning/unpin/"

    headers = {
        "pinata_api_key": pinata_api_key,
        "pinata_secret_api_key": pinata_secret_api_key,
    }

    response = requests.delete(url + ipfs_hash, headers=headers)

    if response.status_code != 200:
        print("Failed to unpin file from IPFS:", response.text)
