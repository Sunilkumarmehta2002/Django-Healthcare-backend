# mappings/urls.py
from django.urls import path
from .views import (
    PatientDoctorMappingListCreateView, 
    PatientDoctorMappingDetailView,
    PatientDoctorsListView
)

urlpatterns = [
    path('', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
    path('patient/<int:patient_id>/', PatientDoctorsListView.as_view(), name='patient-doctors'),
]