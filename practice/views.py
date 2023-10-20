from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import studentDetails
from .serializers import QueryPracticeViewSerializers
import json
# Create your views here.

class QueryPracticeView(APIView):
    def post(self,request):
        # stu_name = request.data.get('name','')
        # stu_standard = request.data.get('standard','')
        # stu_phone_number = request.data.get('phone_number','')
        seriliazer = QueryPracticeViewSerializers(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response({"message":"Post request created succesfully"})
        return Response({'Error':seriliazer.errors},status=status.HTTP_400_BAD_REQUEST)

        
        
    
    def get(self,request):
        model_get = studentDetails.objects.all().values()
        print("this is the model i get",model_get)
        try:
            serilizer = QueryPracticeViewSerializers(model_get,many = True)
            return Response(serilizer.data)
        except studentDetails.DoesNotExist:
            return Response({"message":"No data is present in get request"})
        
    def put(self,request):
        id = request.data.get('id')
        # data_fetch = studentDetails.objects.get(id = id)
        try:
            data_fetch = studentDetails.objects.get(id = id)
        except:
            return Response({"message":"Invalid id to update"},status=status.HTTP_400_BAD_REQUEST)
        serilizer = QueryPracticeViewSerializers(data_fetch,request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"Updated Data",json.dumps(serilizer.data)},status=status.HTTP_200_OK)
        return Response(serilizer.errors)
    def delete(self,request):
        id = request.data.get('id')
        try:
            del_data = studentDetails.objects.get(id= id)
        except:
            return Response({"message":"You entered wrong id"})
        
        if del_data:
            del_data.delete()
            return Response({"message":"Data deleted Successfully"})
        return Response({"message":"Unable to delete data"})
    


        
        return Response({'response':model_get})
        
    

    




