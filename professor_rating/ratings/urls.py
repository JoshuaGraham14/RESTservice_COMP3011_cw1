from django.urls import path
from .views import RegisterView, LoginView, LogoutView,ModuleInstanceListView, ProfessorRatingsView, ProfessorModuleRatingView, RateProfessorView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('modules/', ModuleInstanceListView.as_view(), name='modules'),
    path('professors/ratings/', ProfessorRatingsView.as_view(), name='professor_ratings'),

    path('professors/<str:professor_id>/module/<str:module_code>/rating/', 
         ProfessorModuleRatingView.as_view(), name='professor_module_rating'),
         
    path('professors/<str:professor_id>/module/<str:module_code>/<int:year>/<int:semester>/rate/',
         RateProfessorView.as_view(), name='rate_professor'),
]