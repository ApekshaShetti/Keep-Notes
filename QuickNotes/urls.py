from django.urls import path,include
from .views import getRoutes, getNotes, getNote, updateNote, deleteNote, createNote,register,login

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('notes/', getNotes, name="notes"),
    path('notes/create', createNote, name="create-note"),
    path('notes/<str:pk>/update', updateNote, name="update-note"),
    path('notes/<str:pk>/delete', deleteNote, name="delete-note"),
    path('notes/<str:pk>/', getNote, name="note"),
]