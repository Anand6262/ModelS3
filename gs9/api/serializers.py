from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    #3)Validators
    def start_with_r(value):
        if value[0].lower() !='r':
            raise serializers.ValidationError('Name must be start with R!!')
    name=serializers.CharField(validators=[start_with_r])


    class Meta:
        model=Student
        fields=['id','name', 'roll', 'city']


    #1)Field Level Validation
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('Seat Full!!')
        return value


    #2)Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'raju' and ct.lower() !='mp':
            raise serializers.ValidationError('City of Raju must be mp!!')
        return data




# class StudentSerializer(serializers.ModelSerializer):
#     # name=serializers.CharField(read_only=True)  #THIS LINE IS WRITTEN TO PUT READ ONLY IN SINGLE FIELDS
#     class Meta:
#         model=Student
#         fields=['id','name', 'roll', 'city']
#         read_only_fields=['name', 'roll']  #THIS LINE IS WRITTEN TO PUT READ ONLY IN MULTIPLE FIELDS (Here we are applying read_only in 2 fields i.e name and roll)
#         # extra_kwargs={'name' : {'read_only' : True}}  #THIS LINE IS WRITTEN TO PUT READ ONLY IN SINGLE FIELDS