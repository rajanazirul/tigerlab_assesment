from django.db import models


# Create your models here.
class FileUpload(models.Model):
    file = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "file_upload"
        verbose_name_plural = "files_upload"
        db_table = "file_upload"
