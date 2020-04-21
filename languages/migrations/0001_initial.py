# Generated by Django 3.0.5 on 2020-04-21 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('language', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='language', to='categorys.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language_note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.TextField()),
                ('language_note', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='language_note', to='languages.Language')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language_notes_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('text', models.TextField()),
                ('title_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Language_notes_text', to='languages.Language_note')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
