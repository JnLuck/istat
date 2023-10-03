# Generated by Django 4.2 on 2023-09-30 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion', '0001_initial'),
        ('unidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to='')),
                ('codigo', models.CharField(max_length=50)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.persona')),
            ],
        ),
        migrations.CreateModel(
            name='PlanEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.estudiante')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.IntegerField()),
                ('plan_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.planestudiante')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleMatricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('estado_curso', models.BooleanField(blank=True)),
                ('estado_modulo', models.BooleanField(blank=True)),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.matricula')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.unidaddidactica')),
            ],
        ),
    ]