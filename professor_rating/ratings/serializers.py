from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Professor, Module, ModuleInstance,Rating

# --- Serializes to convery Django models  to json for API responses ---

#Reference: https://www.django-rest-framework.org/tutorial/1-serialization/

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'password'] #fields to be serialized
        extra_kwargs = {
            'password': {'write_only':True}, #password is write-only
            'email': {'required': True}  # email is required
        } 
    
    #Validates email to ensure it is unique
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

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
    professors = serializers.SerializerMethodField()  

    class Meta:
        model = ModuleInstance
        fields = ['id','module', 'year', 'semester','professors']

    def get_professors(self, obj):
        return [prof.professor.name for prof in obj.professormodule_set.all()]
 

class RatingSerializer(serializers.ModelSerializer):
    #Takes the following models as a string instead of ID
    user= serializers.StringRelatedField()
    professor = ProfessorSerializer()
    module_instance =ModuleInstanceSerializer()

    class Meta:
        model = Rating
        fields = ['id', 'user', 'professor','module_instance', 'rating']

