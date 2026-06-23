from rest_framework import serializers
from setup.models import MenuRole


class MenuRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuRole
        fields = "__all__"