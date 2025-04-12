from django import forms
from .models import author,book,borrowRecord

class authorForm(forms.ModelForm):
    class Meta:
        model = author
        fields = ('name','email','bio')
        
        
    def valid_email(self):
        email = self.valid_email.get('email')
        if not email.endswith('gmail.com'):
            raise forms.ValidationError('only valid email are allowed')
        return email
    
class bookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ('title', 'genre', 'published_date', 'author')
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
        
class borrowRecordForm(forms.ModelForm):
    class Meta:
        model = borrowRecord
        fields = ('borrow_name','book','borrow_date','return_date')
        widgets = {
            'borrow_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }