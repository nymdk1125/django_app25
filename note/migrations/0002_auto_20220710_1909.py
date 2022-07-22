# Generated by Django 3.0.4 on 2022-07-10 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(choices=[('Pathology', '病態'), ('Symptoms', '症状'), ('Clinical_examination', '検査'), ('Image_inspection', '画像'), ('Diagnose', '診断'), ('Treatment', '治療'), ('Nurse', '看護'), ('Free_item', 'フリー項目')], max_length=50, verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='note',
            name='department',
            field=models.CharField(choices=[('Brain', '脳神経'), ('Respiratory', '呼吸器'), ('Circulation', '循環器'), ('Digestive', '消化器'), ('Kidney_Urology', '腎・泌尿器'), ('Endocrine_metabolism_nutrition', '内分泌・代謝・栄養'), ('Orthopedics', '整形外科'), ('Hematology', '血液'), ('Ophthalmology', '眼科'), ('Dermatology', '皮膚科'), ('Otorhinolaryngology', '耳鼻咽喉科'), ('Dental', '歯科口腔外科'), ('Obstetrics', '産婦人科'), ('Psychiatry', '精神科'), ('Firstaid_icu', '救急・ICU'), ('Others', 'その他')], max_length=50, verbose_name='診療科'),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]