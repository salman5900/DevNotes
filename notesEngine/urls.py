from django.urls import path
from . import views

app_name = 'notesEngine'

urlpatterns = [ 
    path('add_note/', views.add_note, name='add_note'),
    path('all_notes/', views.all_notes, name='all_notes'),
    path('<slug:slug>/',views.note,name='note'),
]