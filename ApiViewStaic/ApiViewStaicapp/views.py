from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
class Institute(APIView):
    def get(self,request):
        databases=[
            {
                'mysql':'free',
                'Oracle':1000,
                'MangoDb':2000,
            }
        ]
        languges=[
            {
                'python':2000,
                'java':1500,
                'c':500,
            }
        ]
        frameworks=[
            {
                'RestApi':2000,
                'django':1500,
                'springs':500,
            }
        ]
        return Response({
                       'databases':databases,
                       'languages':languges,
                        'frameworks':frameworks,
             })