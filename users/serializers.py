from rest_framework import serializers

from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'birthday', 'is_organizer', 'organization_name', 'organization_description', 'organization_inn', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ('organizations',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password'))
        return super().update(instance, validated_data)

