from rest_framework import serializers
from .models import Group, Group_User, User, Chats, Responses, Friends, Posts

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','firstName', 'lastName', 'email', 'password', 'registration_date', 'interest1','interest2','interest3','program','picture', 'online_status')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id','groupName','description','picture','tags','slug')

class GroupUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group_User
        fields = '__all__'

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['user_id'] = UserSerializer(instance.user_id).data
        response['group_id'] = GroupSerializer(instance.group_id).data
        return response
        
class ChatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chats
        fields = ('id','sender','recipient','message','timestamp')

class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Responses
        fields = ('id','post_id','response_id','time','upvotes','body')
        depth = 2

class FriendsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friends
        fields = ('id','user_id','friend_id','status')


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['author'] = UserSerializer(instance.author).data
        response['group_id'] = GroupSerializer(instance.group_id).data
        return response
        



