# Generated by Django 4.2 on 2023-09-30 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoCompetencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUnidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadDidactica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
                ('horas', models.IntegerField()),
                ('ciclo', models.IntegerField()),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.modulo')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.plan')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.tipounidad')),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('capacidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.competencia')),
            ],
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.indicador')),
            ],
        ),
        migrations.AddField(
            model_name='competencia',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.tipocompetencia'),
        ),
        migrations.AddField(
            model_name='competencia',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.unidaddidactica'),
        ),
        migrations.CreateModel(
            name='Capacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.competencia')),
            ],
        ),
    ]
