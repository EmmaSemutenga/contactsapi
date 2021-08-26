from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Contact
        fields = ['url','country_code', 'first_name', 'last_name', 'phone_number', 'contact_picture', 'is_favourited', 'owner']