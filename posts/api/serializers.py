from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="post:detail",
        lookup_field='slug'
    )
    username = serializers.SerializerMethodField(method_name='username_new')

    class Meta:
        model = Post
        fields = [
            'username',
            'title',
            'description',
            'image',
            'url',
            'created',
            'modified',
            'modified_by'
        ]

    def username_new(self, obj):
        return str(obj.user.username)


class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'image'
        ]

    # def validate_title(self, value):
    #     if value == "amil":
    #         raise serializers.ValidationError("Bu deyer qadagan edilmishdir")
    #     return value

    # def validate(self, attrs):
    #     if attrs["title"] == 'amil':
    #         raise serializers.ValidationError("Bu deyer qadagan edilmishdir")
    #     return attrs
