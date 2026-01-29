from django.db import models


class UploadArquivo(models.Model):
    """
    Model for uploaded files.
    """

    titulo = models.CharField(max_length=255, help_text="Name of the uploaded file")
    arquivo = models.FileField(upload_to="uploads/", help_text="The CSV file itself")
    data_upload = models.DateTimeField(
        auto_now_add=True, help_text="Date and time of upload"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "financeiro"
        verbose_name = "File Upload"
        verbose_name_plural = "File Uploads"
