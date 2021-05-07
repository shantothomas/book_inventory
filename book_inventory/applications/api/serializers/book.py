from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from rest_framework import serializers
from uuid import uuid4

from bookapp.models import Books


class RegitrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    email = serializers.CharField(required=False, allow_blank=True, max_length=100)
    password = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        # email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        rand_token = uuid4()
        user = User.objects.create(password=make_password(password), username=username,email=email)
        return validated_data

class EmlployeeLoginSerializer(serializers.Serializer):
    id = serializers.CharField(required=False, allow_blank=True, max_length=100)
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    email = serializers.CharField(required=False, allow_blank=True, max_length=100)
    password = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        rand_token = uuid4()
        print(make_password(password))
        userlogin = User.objects.filter(email=email)
        if userlogin:
            for user in userlogin:
                validated_data['id'] = user.id
                validated_data['password'] = user.password
                validated_data['username'] = user.username
                validated_data['email'] = user.email
                if check_password(password, user.password):
                    print("Login successful")

                    return validated_data
        else:
            print("lll")
            raise serializers.ValidationError({"message": "Username and password is mismatch"})

class AddingBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
