from django import forms
from blog.models import Post, Comment
from django.contrib.auth.models import User

#blog

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','text','postimage')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'postcontent editable'}),            
        }
        

class CommentForm(forms.ModelForm):

        class Meta:
            model = Comment
            fields = ('text',)

            widgets = {
                
                'text':forms.Textarea(attrs={'class':'postcontent editable'})
    
            }