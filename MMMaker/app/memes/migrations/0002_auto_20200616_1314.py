# Generated by Django 2.2.12 on 2020-06-16 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AddField(
            model_name='task',
            name='result_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(10, '서버 작업 대기중'), (20, '서버 작업 시작'), (30, '서버 리소스 다운로드'), (0, '작업 실패')], default=10),
        ),
        migrations.AlterField(
            model_name='taskresource',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_resources', to='memes.Task'),
        ),
    ]
