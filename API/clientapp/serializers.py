from rest_framework import serializers
from . models import CCTV_Img

class CCTVSerializer(serializers.ModelSerializer):

    class Meta:
        model = CCTV_Img
        fields = "__all__"