from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class Index(APIView):
    def get(self,request):
        data = {
            'name' : 'Subham',
            'age' : 21
        }
        return Response(data)


# def index(request):
#     return JsonResponse({'message' : 'tihis is home page'})