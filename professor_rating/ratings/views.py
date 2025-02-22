from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserSerializer, ModuleInstanceSerializer, ProfessorSerializer

from .models import ModuleInstance, Professor, Rating


from django.db.models import Avg

#Reference: https://www.django-rest-framework.org/tutorial/3-class-based-views/
class RegisterView(APIView):
    def post(self, request):   #handles POST request
        serializer = UserSerializer(data=request.data) #serializes data into Django User data model
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Reference: https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
#Reference: https://www.youtube.com/watch?v=bLGAKqn_stA
class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']

            #Prevent double login:
            Token.objects.filter(user=user).delete() #delete our old token (if exists) before creating a new one
            token, _ = Token.objects.get_or_create(user=user) #issue new token

            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView (APIView):
    permission_classes = [IsAuthenticated] #must be auth to be able to logout 
    
    def post(self, request):
        try:  
            Token.objects.get(user=request.user).delete() #invalidate the token on logout
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK) 
            
        except Token.DoesNotExist:
            return Response({"error": "Invalid request"},status=status.HTTP_400_BAD_REQUEST) 

class ModuleInstanceListView(ListAPIView):
    permission_classes = [AllowAny]

    queryset = ModuleInstance.objects.all()
    serializer_class = ModuleInstanceSerializer

#Reference: https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#generating-aggregates
class ProfessorRatingsView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request): 
        professors = Professor.objects.all()

        data = [] 
        for professor in professors: 
            avg_rating =Rating.objects.filter(professor=professor).aggregate(Avg("rating"))["rating__avg"] 
            if avg_rating is not None:
                avg_rating = round(avg_rating)
            else:
                avg_rating = "No ratings yet"

            data.append({
                "id": professor.id,
                "name": professor.name,
                "average_rating":avg_rating
            })

        return Response(data) 
    