from django.urls import path

from .views import StudentAutocomplete

urlpatterns = [
    path('ac/student/', StudentAutocomplete.as_view(), name='ac_student'),
]
