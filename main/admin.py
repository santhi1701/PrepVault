from django.contrib import admin
from .models import QuizTopic, Question
from .models import UserQuizResponse,Resource
# Register your models here.


admin.site.register(QuizTopic)
admin.site.register(Question)
admin.site.register(UserQuizResponse)
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'title', 'category')
    list_filter = ('category',)
    search_fields = ('subject', 'title')