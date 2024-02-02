from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
#created a model class to upload the filed in the specified formate
def validate_file_extension(value):
    allowed_extensions = ['.ppt', '.pptx', '.docx', '.xlsx']
    extension = str(value).lower().split('.')[-1]
    if extension not in allowed_extensions:
        raise ValidationError(_('Only .ppt, .pptx, .docx, and .xlsx files are allowed.'))

class File(models.Model):
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)