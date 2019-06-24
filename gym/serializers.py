from rest_framework import serializers
from .models import *

class MemberRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberInfo
        fields = "__all__"

class MemberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberInfo
        fields = ["username", "phone", "sex", "portrait"]

class MemberCardSerializer(serializers.ModelSerializer):
    member = MemberInfoSerializer()
    class Meta:
        model = MemberCard
        fields = ["member", "card_type", "end_time", "create_time", "use_time"]