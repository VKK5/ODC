import rest_framework
from rest_framework import serializers
from signup.models import *

class LocationDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=200)
    geolocation = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Location(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.geolocation = validated_data.get('geolocation', instance.geolocation)
        instance.save()
        return instance 
