from django.urls import path
from .views import my_functional_view, confirm_needed, Logout

urlpatterns = [
    path("signup/",my_functional_view,name="signup"),
    path('confirm/<int:id>/',confirm_needed,name="confirm_needed"),
    path('logout/',Logout,name="logout")
]