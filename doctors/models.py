# doctors/models.py
from django.db import models
from accounts.models import CustomUser

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('CARDIOLOGY', 'Cardiology'),
        ('DERMATOLOGY', 'Dermatology'),
        ('NEUROLOGY', 'Neurology'),
        ('ONCOLOGY', 'Oncology'),
        ('PEDIATRICS', 'Pediatrics'),
        ('PSYCHIATRY', 'Psychiatry'),
        ('SURGERY', 'Surgery'),
        ('RADIOLOGY', 'Radiology'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctors')
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    qualifications = models.TextField()
    experience = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name