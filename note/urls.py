from django.urls import path
from . import views

app_name = 'note'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('note/create/', views.NoteCreateView.as_view(), name='note_create'),
    path('note/create/complete/', views.NoteCreateCompleteView.as_view(), name='note_create_complete'),
    path('note/list/', views.NoteListView.as_view(), name='note_list'),
    path('note/detail/<uuid:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('note/update/<uuid:pk>/', views.NoteUpdateView.as_view(), name='note_update'),
    path('note/delete/<uuid:pk>/', views.NoteDeleteView.as_view(), name='note_delete'),
    path('',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),
    path('register', views.AccountRegistration.as_view(), name='register'),
    path('home',views.home,name='home'),
    # path('note',views.NoteList.as_view(),name='note'),
]