from rest_framework import serializers

class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    storage_type = serializers.CharField()
