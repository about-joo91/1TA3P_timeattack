# Generated by Django 4.0.5 on 2022-06-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(choices=[('D', 'day'), ('S', 'sports')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tag_name',
            field=models.ManyToManyField(to='post.tagmodel'),
        ),
    ]
