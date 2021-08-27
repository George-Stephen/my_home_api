from django.shortcuts import render
from django_filters.rest_framework.filterset import FilterSet
from .models import Apartment
from rest_framework.response import Response
from rest_framework import generics,filters, serializers,status
from rest_framework.views import APIView,Http404
from .serializers import ApartmentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class filter_apartments(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location','bedrooms','bathrooms','status']

class apartments_list(generics.ListAPIView):
    def post(self,request,format=None):
        serializers = ApartmentSerializer(data=request.data)
        if serializers.is_valid:
            serializers.save
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else :
            return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)

class single_apartment(APIView):
    def get_apartment(self,pk):
        try:
            return Apartment.objects.get(pk=pk)
        except Apartment.DoesNotExist:
            return Http404
    def get(self,request,pk,format=None):
        apartment = self.get_apartment(pk)
        serializers = ApartmentSerializer(apartment)
        return Response(serializers.data)

    def patch(self,request,pk,format=None):
        apartment = self.get_apartment(pk)
        serializers = ApartmentSerializer(apartment)
        if serializers.is_valid:
            serializers.save
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
