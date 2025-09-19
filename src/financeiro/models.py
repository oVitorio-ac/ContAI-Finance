from django.db import models


class UploadArquivo(models.Model):
    """
    Model for uploaded files.
    """

    titulo = models.CharField(max_length=255, help_text="Nome do arquivo enviado")
    arquivo = models.FileField(upload_to="uploads/", help_text="O arquivo CSV em si")
    data_upload = models.DateTimeField(
        auto_now_add=True, help_text="Data e hora do upload"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "financeiro"
        verbose_name = "Upload de Arquivo"
        verbose_name_plural = "Uploads de Arquivos"
