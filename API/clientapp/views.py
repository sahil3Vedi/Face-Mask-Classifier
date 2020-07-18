from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from . serializers import CCTVSerializer

from . forms import *

# Create your views here.

class CCTVList(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        CCTV_serializer = CCTVSerializer(data=request.data)

        if CCTV_serializer.is_valid():
            cctv_img = CCTV_serializer.save()
            json_response = cctv_img.processImage()
            return Response(json_response, status=status.HTTP_201_CREATED)
        else:
            return Response(CCTV_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

