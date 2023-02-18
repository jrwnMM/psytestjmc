# Generated by Django 3.2.7 on 2023-01-02 15:16

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('iqtest', '0006_alter_question_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', django_quill.fields.QuillField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', django_quill.fields.QuillField()),
                ('is_answer', models.CharField(choices=[('correct', 'Correct'), ('incorrect', 'Incorrect')], max_length=32)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='iqtest.question')),
            ],
        ),
    ]