from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    from HyperlinkedModelSerializer:

        * A 'url' field is included instead of the 'id' field.
        * Relationships to other instances are hyperlinks, instead of primary keys.

    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
