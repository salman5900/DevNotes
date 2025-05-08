from django.shortcuts import render,redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required
def all_notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-date') 
    return render(request, 'notesEngine/all_notes.html', { 'notes': notes }) 

def add_note(request):
    if request.method ==  'POST':
        form = forms.CreateNote(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notesEngine:all_notes')
    else:
        form = forms.CreateNote()
    return render(request, 'notesEngine/add_note.html', { 'form': form })

def note(request, slug):
    note = Note.objects.get(slug=slug)
    return render(request, 'notesEngine/note.html', { 'note': note })
