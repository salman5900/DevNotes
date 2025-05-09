from django.shortcuts import render,redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required
def all_notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-date') 
    return render(request, 'notesEngine/all_notes.html', { 'notes': notes }) 

@login_required
def edit_note(request, slug):
    note = Note.objects.get(slug=slug, user=request.user)
    
    if request.method == 'POST':
        form = forms.CreateNote(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notesEngine:note', slug=note.slug)
    else:
        form = forms.CreateNote(instance=note)
    
    return render(request, 'notesEngine/edit_note.html', { 'form': form,'note': note, })

def delete_note(request, slug):
    # Fetch the note by its slug and the user making the request
    note = Note.objects.get(slug=slug, user=request.user)
    # Delete the note from the database
    note.delete()
    # Redirect the user to the "all_notes" page after deletion
    return redirect('notesEngine:all_notes')

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
