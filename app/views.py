# import io
# from django.http import JsonResponse
# from django.shortcuts import render
# from rest_framework.decorators import api_view
from .models import Student
# from django.views.decorators.csrf import csrf_exempt 
from .serializer import StudentSerializer
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

from app import serializer
# Create your views here.


class StudentListCreate(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class StudentRUDAPI(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# @api_view(['GET','POST','PUT','DELETE'])
# def student(request,pk=None):
#     if request.method == "GET":
#         # json_data = request.body
#         # stream =io.BytesIO(json_data)
#         # python_data= JSONParser().parse(stream)
#         id= pk
#         # data = Student.objects.all()
#         # id = data.id
#         # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",id)

#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         # elif id :


      
#         stu = Student.objects.all()
#         serializer= StudentSerializer(stu , many=True)
#         return Response(serializer.data)
    

   
#     if request.method == 'POST':
#         # json_data = request.body
#         # stream = io.BytesIO(json_data)
#         # python_data= JSONParser().parse(stream)
#         serializer= StudentSerializer(data= request.data)
#         if serializer.is_valid(): 
#             serializer.save()
            
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     if request.method == 'PUT':
#         # json_data = request.body
#         # stream = io.BytesIO(json_data)
#         # python_data= JSONParser().parse(stream)
#         id = pk
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             response_msg = {'msg': 'data updated successfully!!!!!'}
#             return Response(response_msg)
#         return Response(serializer.errors)

#     if request.method == 'DELETE':
#         # json_data=request.body
#         # stream= io.BytesIO(json_data)
#         # python_data= JSONParser().parse(stream)
#         id = pk
#         if id is not None:
            
#             stu= Student.objects.get(id=id)
#             stu.delete()
#             response_msg= {'msg':'Data deleted !!!!!!'}
#             return Response(response_msg)
#         response_msg= {'msg':'Please enter id !!!!!!'}
#         return Response(response_msg)