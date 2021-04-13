from rest_framework import serializers 

class Person:
    def __init__(self,first_name,last_name,email):
        self.fname=first_name
        self.lname=last_name
        self.email=email

class Serializer(serializers.Serializer):
    fname=serializers.CharField()
    lname=serializers.CharField()
    email=serializers.CharField()

