from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UploadFileSerializer
import upload
import download
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from django.conf import settings
import delete
from django.http import FileResponse

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES['file']
            storage_type = serializer.validated_data['storage_type']

            if storage_type == 'azure':
                upload.upload_azure_storage(file)
            elif storage_type == 'ipfs':
                upload.upload_ipfs_storage(file)
            else:
                return Response({"error": "Invalid storage type"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def download_file(request):
    storage_type = request.POST.get('storage_type')
    file_name = request.POST.get('file_name')

    if storage_type is None or file_name is None:
        return Response({"error": "storage_type and file_name are required"}, status=status.HTTP_400_BAD_REQUEST)

    if storage_type == 'azure':
        file = download.download_from_azure_storage(file_name)
    elif storage_type == 'ipfs':
        file = download.download_from_ipfs_storage(file_name)
    else:
        return Response({"error": "Invalid storage type"}, status=status.HTTP_400_BAD_REQUEST)

    return FileResponse(file, as_attachment=True, filename=file_name)

@api_view(['POST'])
def delete_file(request):
    storage_type = request.POST.get('storage_type')
    file_name = request.POST.get('file_name')

    if storage_type is None or file_name is None:
        return Response({"error": "storage_type and file_name are required"}, status=status.HTTP_400_BAD_REQUEST)

    if storage_type == 'azure':
        delete.delete_from_azure_storage(file_name)
    elif storage_type == 'ipfs':
        delete.delete_from_ipfs_storage(file_name)
    else:
        return Response({"error": "Invalid storage type"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "File deleted successfully"})

