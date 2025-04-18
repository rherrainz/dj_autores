# Generated by Django 5.2 on 2025-04-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(choices=[('ARG', 'Argentina'), ('ESP', 'España'), ('USA', 'Estados Unidos'), ('MEX', 'México'), ('COL', 'Colombia'), ('PER', 'Perú'), ('CHL', 'Chile'), ('VEN', 'Venezuela'), ('ECU', 'Ecuador'), ('BOL', 'Bolivia'), ('PAR', 'Paraguay'), ('URY', 'Uruguay'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('DOM', 'República Dominicana'), ('NIC', 'Nicaragua'), ('HND', 'Honduras'), ('GTM', 'Guatemala'), ('SLV', 'El Salvador'), ('PAN', 'Panamá'), ('PRY', 'Paraguay'), ('BRA', 'Brasil'), ('CHL', 'Chile'), ('URY', 'Uruguay'), ('BOL', 'Bolivia'), ('PAR', 'Paraguay'), ('VEN', 'Venezuela'), ('COL', 'Colombia'), ('PER', 'Perú'), ('ECU', 'Ecuador'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('DOM', 'República Dominicana'), ('NIC', 'Nicaragua'), ('HND', 'Honduras'), ('GTM', 'Guatemala'), ('SLV', 'El Salvador'), ('PAN', 'Panamá')], max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_muerte', models.DateField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
