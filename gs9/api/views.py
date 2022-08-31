#CRUD OPERATION (CREATE,READ, UPDATE, DELETE)
from functools import partial
import json
from django.shortcuts import render
import io
from django.urls import is_valid_path
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    #THIS IS FOR C(CREATE DATAS)
    def post(self, request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg' : 'Data Inserted Successfully!!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    #THIS IS FOR R(READ DATA)
    def get(self, request,*args, **kwargs):
        stu=Student.objects.all()
        # def get(self, req, pk):
        # get(id=pk)
        serializer=StudentSerializer(stu, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    #THIS IS FOR U(UPDATE DATA)
    def put(self, request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id= pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg' : 'Data Updated Successfully!!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    #THIS IS FOR U(UPDATE DATA)-->(Partially)
    def patch(self, request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id= pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg' : 'Data Updated(Partially) Successfully!!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    #THIS IS FOR D(DELETE DATA)
    def delete(self, request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id= pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg' : 'Data Deleted Successfully!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')