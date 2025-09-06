# mappings/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Only show mappings where the patient or doctor belongs to the current user
        return PatientDoctorMapping.objects.filter(
            patient__user=self.request.user
        ) | PatientDoctorMapping.objects.filter(
            doctor__user=self.request.user
        )
    
    def create(self, request, *args, **kwargs):
        # Check if patient and doctor exist and belong to the user
        patient_id = request.data.get('patient')
        doctor_id = request.data.get('doctor')
        
        try:
            patient = Patient.objects.get(id=patient_id, user=request.user)
        except Patient.DoesNotExist:
            return Response(
                {'error': 'Patient not found or does not belong to you.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            doctor = Doctor.objects.get(id=doctor_id, user=request.user)
        except Doctor.DoesNotExist:
            return Response(
                {'error': 'Doctor not found or does not belong to you.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if mapping already exists
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            return Response(
                {'error': 'This doctor is already assigned to this patient.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PatientDoctorMappingDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Only show mappings where the patient or doctor belongs to the current user
        return PatientDoctorMapping.objects.filter(
            patient__user=self.request.user
        ) | PatientDoctorMapping.objects.filter(
            doctor__user=self.request.user
        )

class PatientDoctorsListView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(
            patient__id=patient_id, 
            patient__user=self.request.user
        )