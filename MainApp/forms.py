from django.forms import ModelForm, TextInput, Textarea, ChoiceField
from MainApp.models import Snippet

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code', 'private']
        labels = {'name': '', 'lang':'', 'code':'', 'private':'Приватный'}
        widgets = {
            'name':TextInput(attrs={'placeholder' : 'Название сниппета'}),
            'code':Textarea(attrs={'placeholder' : 'Код сниппета'}),
            # 'private':ChoiceField(attrs={'label' : 'Приватный'} ),
        }