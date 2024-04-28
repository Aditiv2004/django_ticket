from django.db import models

# Create your models here.

from django.contrib.auth.models import User
class Ticket(models.Model):  
  title = models.CharField(max_length=255)
  document_upload = models.FileField(blank=True, default="", upload_to="complaint") 
  description = models.TextField(max_length=255)
  solution=models.TextField(max_length=255, default="", blank=True)
  complaint_type=models.CharField(max_length=255, blank=True, choices=[("2","HARDWARE"),("1","SOFTWARE")],default="")
  created_date=models.DateTimeField(auto_now_add=True)
  resolve_date=models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, related_name="employee",on_delete=models.CASCADE,null=True, blank=True)
  priority=models.CharField(max_length=255, choices=[("3","HIGH"),("2","MEDIUM"),("1","LOW")],default="1")
  technician=models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
  status=models.CharField(max_length=255, choices=[("created","created"),("assigned","assigned"),("resolved","resolved")],default="created")
  rating=models.CharField(max_length=255, choices=[("poor","poor"),("average","average"),("good","good"),("excellent","excellent")],default="poor")
  

  

  

 
