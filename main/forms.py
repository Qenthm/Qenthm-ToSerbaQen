from django.forms import ModelForm
from main.models import MoodEntry
from django.utils.html import strip_tags

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["item", "description", "price"]
    
    def clean_item(self):
        item = self.cleaned_data["item"]
        return strip_tags(item)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)