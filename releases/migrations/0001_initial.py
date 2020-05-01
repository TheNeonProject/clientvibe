# Generated by Django 3.0.5 on 2020-04-30 20:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('tag', models.CharField(max_length=100)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=2000)),
                ('attachment', models.FileField(upload_to='')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReleaseObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('stakeholder_email', models.EmailField(max_length=254)),
                ('score', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.CharField(blank=True, max_length=2000, null=True)),
                ('email_status', models.CharField(blank=True, max_length=2000, null=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='releases.Release')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]