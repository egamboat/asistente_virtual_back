# Generated by Django 4.2.16 on 2024-11-21 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('modalidad', models.CharField(max_length=50)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='asistente.agenda')),
                ('tipo_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='asistente.tipoevento')),
            ],
        ),
    ]
