from rest_framework import serializers
from .models import Group, Group_User, User, Chats, Responses, Friends, Posts

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','firstName', 'lastName', 'email', 'password', 'registration_date', 'interest1','interest2','interest3','program','picture', 'online_status')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id','groupName','description','picture','tags')

class GroupUserSerializer(serializers.ModelSerializer):
    user_id = serializers.HyperlinkedRelatedField(
    read_only=True, view_name='user-detail')
    group_id = serializers.HyperlinkedRelatedField(
    read_only=True, view_name='group-detail')
    class Meta:
        model = Group_User
        fields = ('id','user_id','group_id')

class ChatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chats
        fields = ('id','sender','recipient','message','timestamp')

class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Responses
        fields = ('id','post_id','response_id','time','upvotes','body')

class FriendsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friends
        fields = ('id','user_id','friend_id','status')

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('id','group_id','author','upvotes','title','time','body')

