from rest_framework import serializers
from setup.models import Role


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = [
            "id",
            "role_name",
            "status"
        ]