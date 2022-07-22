from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
# from django.db.models import Q
# from django.contrib.auth import get_user_model

# セレクトボックスに表示する診療科項目
DEPARTMENT_CHOICES = [
    ('Brain','脳神経'),
    ('Respiratory','呼吸器'),
    ('Circulation','循環器'),
    ('Digestive','消化器'),
    ('Kidney_Urology','腎・泌尿器'),
    ('Endocrine_metabolism_nutrition','内分泌・代謝・栄養'),
    ('Orthopedics','整形外科'),
    ('Hematology','血液'),
    ('Ophthalmology','眼科'),
    ('Dermatology','皮膚科'),
    ('Otorhinolaryngology','耳鼻咽喉科'),
    ('Dental','歯科口腔外科'),
    ('Obstetrics','産婦人科'),
    ('Psychiatry','精神科'),
    ('Firstaid_icu','救急・ICU'),
    ('Others','その他'),
]

# セレクトボックスに表示するカテゴリー項目
CATEGORY_CHOICES = [
    ('Pathology','病態'),
    ('Symptoms','症状'),
    ('Clinical_examination','検査'),
    ('Image_inspection','画像'),
    ('Diagnose','診断'),
    ('Treatment','治療'),
    ('Nurse','看護'),
    ('Free_item','フリー項目')
]

# Noteクラス
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.CharField(verbose_name='診療科', max_length=50, choices=DEPARTMENT_CHOICES)
    category = models.CharField(verbose_name='カテゴリー', max_length=50, choices=CATEGORY_CHOICES)
    title = models.CharField(verbose_name='タイトル', max_length=100)
    text = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)

    def __str__(self):
        return self.department
    
    def __str__(self):
        return self.category

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.text

# departmentクラス
class Department(models.Model):
    department_id = models. IntegerField(default=0)
    department_name = models.CharField(max_length=30)

    def __str__(self):
        return self.department_name
# categoryクラス
class Category(models.Model):
    category_id = models. IntegerField(default=0)
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# #検索機能
# User = get_user_model()

# class NoteQuerySet(models.QuerySet):
#     def search(self, query=None):
#         qs = self
#         qs = qs.filter(public=True)
#         if query is not None:
#             or_lookup = (
#                 Q(title__icontains=query)|
#                 Q(text__icontains=query)            
#             )
#             qs = qs.filter(or_lookup).distinct()
#         return qs.order_by("-timestamp")

# class NoteManager(models.Manager):
#     def get_queryset(self):
#         return NoteQuerySet(self.model, using=self._db)

#     def search(self, query=None):
#         return self.get_queryset().search(user=id, query=query)

# class Note(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     department = models.CharField(verbose_name='診療科', max_length=50, choices=DEPARTMENT_CHOICES)
#     category = models.CharField(verbose_name='カテゴリー', max_length=50, choices=CATEGORY_CHOICES)
#     title = models.CharField(verbose_name='タイトル', max_length=100)
#     text = models.TextField(verbose_name='本文')
#     created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
#     updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)

#     objects = NoteManager()

#     def __str__(self):
#         return self.title
