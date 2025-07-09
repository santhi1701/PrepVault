
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class QuizTopic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    topic = models.ForeignKey(QuizTopic, on_delete=models.CASCADE)
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])

    def __str__(self):
        return self.question_text  # ✅ FIXED

class UserQuizResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    attempted_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user.username} - {self.question}"
class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('exam', 'Exam Preparation'),
        ('interview', 'Interview Preparation'),
    ]

    title = models.CharField(max_length=100)
    url = models.URLField()
    subject = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.title} ({self.subject})"
