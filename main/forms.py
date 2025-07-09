# main/forms.py

from django import forms
from .models import Question, QuizTopic

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['topic', 'question_text', 'option1', 'option2', 'option3', 'option4', 'correct_option']
        widgets = {
            'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'option1': forms.TextInput(attrs={'class': 'form-control'}),
            'option2': forms.TextInput(attrs={'class': 'form-control'}),
            'option3': forms.TextInput(attrs={'class': 'form-control'}),
            'option4': forms.TextInput(attrs={'class': 'form-control'}),
            'correct_option': forms.Select(attrs={'class': 'form-select'}),
            'topic': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
    'question_text': 'Enter the question',
    'option1': 'Option A',
    'option2': 'Option B',
    'option3': 'Option C',
    'option4': 'Option D',
    'correct_option': 'Correct Answer',
    'topic': 'Quiz Topic',
}

