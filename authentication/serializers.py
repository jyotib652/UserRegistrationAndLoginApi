from rest_framework import serializers
from .models import User
import re


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = '__all__'


    def validate(self, attrs):
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        address = attrs.get('address', '')

        if first_name.isalpha() is False:
            raise serializers.ValidationError("'First Name' should only contain characters")
        if last_name.isalpha() is False:
            raise serializers.ValidationError("'Last Name' should only contain characters")

        regex = re.compile("[@_!#$%^&*()<>?\|}{~]")
        if regex.search(address) is True:
            raise serializers.ValidationError("'Address' should not contain specaial cahracres other than .,/ and :")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        