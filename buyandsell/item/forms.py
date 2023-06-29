from django import forms

from .models import Item

imput='w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','desc','price','image')
        
        
        widgets={'category':forms.Select(attrs={'class':imput}),
                 'name':forms.TextInput(attrs={'class':imput}),
                 'desc':forms.Textarea(attrs={'class':imput}),
                'price':forms.TextInput(attrs={'class':imput}),
                'image':forms.FileInput(attrs={'class':imput})
             
             
             
             }
        
        
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','desc','price','image','is_sold')
        
        
        widgets={
                 'name':forms.TextInput(attrs={'class':imput}),
                 'desc':forms.Textarea(attrs={'class':imput}),
                'price':forms.TextInput(attrs={'class':imput}),
                'image':forms.FileInput(attrs={'class':imput})
             
             
             
             }