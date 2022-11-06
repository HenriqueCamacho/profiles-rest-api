from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response #When Django calls the api view, it expect a standard Response object


# Create your views here.

class HelloApiView(APIView):
    """Test Api View"""
     
    #Get Method
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function(get, post, patch, put, delete)',
        'Is similiar to a traditional Django View',
        'Gives tou the most control over your application logic',
        'Is mapped manually to URLs'
       ] 
        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
