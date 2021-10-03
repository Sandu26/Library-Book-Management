from django import forms
from .models import Book

#Create book form
class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name','author','genre','height','publisher')
        labels = {
            'name':'Name',
            'author':'Author',
            'genre':'Genre',
            'height':'Height',
            'publisher':'Publisher'
        }

    def __init__(self, *args, **kwargs):
        super(BookForm,self).__init__(*args, **kwargs)
        self.fields['height'].required = False