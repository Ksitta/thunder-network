from rest_framework import serializers
from . import models


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        read_only_fields = ['username']
        fields = ['contact_details', 'contact_email', 'contact_address'] + read_only_fields
