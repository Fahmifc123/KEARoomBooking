from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Campus
from .serializer import CampusSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class AllCampus(ListAPIView):

    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('campusName', )

    def post(self, request, format=None):
        serializer = CampusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampusView(APIView):

    def get(self, request, pk, format=None):
        try:
            campus = Campus.objects.get(pk=pk)
            serializer = CampusSerializer(campus)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        campus = Campus.objects.get(pk=pk)
        campus.delete()
        return Response(status=status.HTTP_200_OK)



