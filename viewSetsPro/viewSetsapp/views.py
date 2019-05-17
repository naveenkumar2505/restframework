from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework import status


class Viewset_Feedback(viewsets.ViewSet):

    def list(self,request):

       #getting data from Database
        queryset=Feedback.objects.all()

       #converting Database data into Json Formate
        serializer=FeedbackSerializer(queryset,many=True)
        return Response(serializer.data)


    def create(self,request):
        serializer=FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def retieve(self,request,pk):
        #grtting specific data from DB
        queryset=Feedback.objects.get(pk=pk)
        serializer=FeedbackSerializer(queryset)
        return Response(serializer.data)


    def update(self,request,pk):
        queryset=Feedback.objects.get(pk=pk)
        serializer=FeedbackSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.error,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


    def destroy(self,request,pk):
        queryset=Feedback.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)