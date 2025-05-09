from django.urls import path
from . import views

app_name = 'notesEngine'

urlpatterns = [ 
    path('add_note/', views.add_note, name='add_note'),
    path('all_notes/', views.all_notes, name='all_notes'),
    path('<slug:slug>/',views.note,name='note'),
    path('edit/<slug:slug>/', views.edit_note, name='edit_note'),
    path('delete/<slug:slug>/', views.delete_note, name='delete_note'),

]