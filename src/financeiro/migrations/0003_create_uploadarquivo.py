# Generated manually to recreate UploadArquivo model

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("financeiro", "0002_delete_uploadarquivo"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadArquivo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("titulo", models.CharField(max_length=255, help_text="Nome do arquivo enviado")),
                ("arquivo", models.FileField(upload_to="uploads/", help_text="O arquivo CSV em si")),
                ("data_upload", models.DateTimeField(auto_now_add=True, help_text="Data e hora do upload")),
            ],
            options={
                "app_label": "financeiro",
                "verbose_name": "Upload de Arquivo",
                "verbose_name_plural": "Uploads de Arquivos",
            },
        ),
    ]