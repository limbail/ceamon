from rest_framework import serializers
from ceamon.models import sapnode, StatusModel
from django.contrib.auth.models import User, Group

class sapnodeSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(many=True, required=False)
    class Meta:
        model = sapnode
        fields = ('pk', 'active_moni', 'product', 'project', 'client_role', 'status', 'product_v', 'product_def', 'sap_kernel', 'database', 'database_v', 'os', 'os_v', 'ip', 'cpu', 'asi_disk', 'asi_ram', 'sid', 'hostname', 'url', 'sap_clnt', 'sap_sysn',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class StatusSerializer(serializers.ModelSerializer):
    #comment = serializers.StringRelatedField(required=False)
    system = serializers.StringRelatedField()
    class Meta:
        model = StatusModel
        fields = ('system', 'status_id', 'status', 'comment',)

