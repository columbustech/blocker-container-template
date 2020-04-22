from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .block import *
import requests

class BlockView(APIView):
    parser_class = (JSONParser,)

    @csrf_exempt
    def post(self, request):
        left = request.data['leftTuples']
        right = request.data['rightTuples']
        df = block(left, right)
        return Response({"output": df.to_json(orient='records')}, status=status.HTTP_200_OK)
