from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Categories
from api.serializers import CategorySerializer


class HelloApiView(APIView):

    def get(self, request, format=None):
        """Returns a list of"""
        return Response(CategorySerializer(Categories.objects.all(), many=True).data)
