from django.urls import path,include
from .views import getRoutes, getNotes, getNote, updateNote, deleteNote, createNote,register,login

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('notes/<str:email>/all', getNotes, name="notes"),
    path('notes/create', createNote, name="create-note"),
    path('notes/<str:pk>/update', updateNote, name="update-note"),
    path('notes/<str:pk>/delete', deleteNote, name="delete-note"),
    path('note/<str:pk>/', getNote, name="note"),
]