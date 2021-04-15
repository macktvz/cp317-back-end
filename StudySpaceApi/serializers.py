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
        fields = ('id','user_id','group_id')
        depth = 2
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

class RF(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    group_id = RF(queryset=Group.objects.all(), serializer=GroupSerializer)
    author = RF(queryset=User.objects.all(), serializer=UserSerializer)

    class Meta:
        model = Posts
        fields = ('id','group_id','author','upvotes','title','time','body','slug')
        



