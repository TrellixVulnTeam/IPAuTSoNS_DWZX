from rest_framework import serializers
from .models import Job, User


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'job_id',
            'user_id',
            'app_id',
            'path',
            'num_img',
            'img_selected',
            'persent',
            'job_status',
            'create_time'
        )
        model = Job


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user_id',
            'password',
            'email',
            'is_vip',
            'first_name',
            'last_name',
        )
        model = User

        extra_kwargs ={
            'password' : {'write_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
