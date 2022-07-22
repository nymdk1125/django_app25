from gettext import find
from django import forms
from .models import Note,Account
from django.contrib.auth.models import User

# ノートクラス作成
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('department', 'category', 'title', 'text',)
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('last_name','first_name',)
        labels = {'last_name':"苗字",'first_name':"名前",}

# #検索フォーム
# class SearchForm(forms.Form):
#     search = forms.CharField(label='Search',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

# #検索フォーム
# class FindForm(forms.Form):
#     find = forms.CharField(label='Find',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))



