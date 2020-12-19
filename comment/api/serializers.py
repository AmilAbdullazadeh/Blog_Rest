from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from posts.models import Post
from ..models import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created']

    def validate(self, attrs):
        if (attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("Valdation error buddy !")
        return attrs


# class CommenyChildSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug',)


class CommentListSerializer(serializers.ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = "__all__"
        # depth = 1

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'description'
        ]
