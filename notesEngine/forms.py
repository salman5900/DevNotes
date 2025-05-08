from django import forms 
from . import models

class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title','slug','content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add custom widget classes for styling
        self.fields['title'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter ',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })
        
        self.fields['slug'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter the Slug',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })
        
        self.fields['content'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter the Content',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })