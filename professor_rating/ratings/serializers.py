from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Professor, Module, ModuleInstance,Rating

# --- Serializes to convery Django models  to json for API responses ---

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'password'] #fields to be serialized
        extra_kwargs = {'password': {'write_only':True}} #password is write only
  
    def create(self, validated_data): 
        return User.objects.create_user(**validated_data) 

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Professor
        fields =['id','name']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module 
        fields =['id','name']  

class ModuleInstanceSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()

    class Meta:
        model = ModuleInstance
        fields = ['id','module', 'year', 'semester'] 
 

class RatingSerializer(serializers.ModelSerializer):
    #Takes the following models as a string instead of ID
    user= serializers.StringRelatedField()
    professor = ProfessorSerializer()
    module_instance =ModuleInstanceSerializer()

    class Meta:
        model = Rating
        fields = ['id', 'user', 'professor','module_instance', 'rating']

