# from atexit import register
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Note
from .forms import NoteForm,AccountForm, AddAccountForm
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('note:home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('note:Login'))


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "index.html",context=params)

#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        # return render(request,"App_Folder_HTML/register.html",context=self.params)
        return render(request,"register.html",context=self.params)


    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        # return render(request,"App_Folder_HTML/register.html",context=self.params)
        return render(request,"register.html",context=self.params)


class IndexView(TemplateView):
    template_name = 'index.html'

class NoteCreateView(CreateView):
    template_name = 'note_create.html'
    form_class = NoteForm
    success_url = reverse_lazy('note:note_create_complete')

class NoteCreateCompleteView(TemplateView):
    template_name = 'note_create_complete.html'

class NoteListView(ListView):
    template_name = 'note_list.html'
    model = Note

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Note.objects.filter(
                Q(title__icontains=q_word) | Q(text__icontains=q_word))
        else:
            object_list = Note.objects.all()
        return object_list

class NoteDetailView(DetailView):
    template_name = 'note_detail.html'
    model = Note

class NoteUpdateView(UpdateView):
    template_name = 'note_update.html'
    model = Note
    fields = ('department', 'category', 'title', 'text',)
    success_url = reverse_lazy('note:note_list')

    def form_valid(self, form):
        note = form.save(commit=False)
        note.updated_at = timezone.now()
        note.save()
        return super().form_valid(form)

class NoteDeleteView(DeleteView):
    template_name = 'note_delete.html'
    model = Note
    success_url = reverse_lazy('note:note_list')

# #検索機能
# def get_queryset(self):
#     try:
#         q = self.request.GET["search"]
#     except:
#         q = None
#     return Note.objects.search(query=q)

# #検索機能
# def find(request):
#     if (request.method == 'POST'):
#         form = FindForm(request.POST)
#         find = request.POST['find']
#         data = Note.objects.filter(name=find)
#         msg = 'Result: ' + str(data.count())
#     else:
#         msg = 'search words...'
#         form = FindForm()
#         data =Note.objects.all()
#     params = {
#         'title': 'msg',
#         'text': msg,
#         'form':form,
#         'data':data,
#     }
#     return render(request, 'note/find.html', params)

# #検索機能
# class NoteList(ListView):
#     model = Note
#     def get_queryset(self):
#         q_word = self.request.GET.get('query')

#         if q_word:
#             object_list = Note.objects.filter(
#                 Q(title__icontains=q_word) | Q(text__icontains=q_word))
#         else:
#             object_list = Note.objects.all()
#         return object_list