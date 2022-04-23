# Generated by Django 4.0.2 on 2022-04-22 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0003_delete_sub_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, max_length=1500, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Categories.categories')),
            ],
        ),
    ]
