
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import QuizTopic, Question, Resource, UserQuizResponse
from django.db.models import Count, Sum,Avg
from .forms import QuestionForm
from django.contrib.admin.views.decorators import staff_member_required
def home(request):
    return render(request, 'main/home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Registration successful. Please login.")
            return redirect('login')
    return render(request, 'main/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def quiz_list(request):
    topics = QuizTopic.objects.all()
    return render(request, 'main/quiz_list.html', {'topics': topics})

@login_required
def quiz_questions(request, topic_id):
    topic = get_object_or_404(QuizTopic, id=topic_id)
    questions = Question.objects.filter(topic=topic)

    if request.method == 'POST':
        score = 0
        results = []

        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                selected_option = int(selected)
                is_correct = (selected_option == question.correct_option)
                if is_correct:
                    score += 1

                # Save user response
                UserQuizResponse.objects.create(
                    user=request.user,
                    question=question,
                    selected_option=selected_option,
                    is_correct=is_correct
                )
                 # Prepare data for results display
                results.append({
                    'question': question.question_text,
                    'selected': getattr(question, f'option{selected_option}'),
                    'correct': getattr(question, f'option{question.correct_option}'),
                    'is_correct': is_correct,
                })

               

        return render(request, 'main/quiz_result.html', {
            'score': score,
            'total': questions.count(),
            'topic': topic,
            'results': results
        })

    return render(request, 'main/quiz_questions.html', {
        'topic': topic,
        'questions': questions
    })



@staff_member_required  # Only admin/staff can access
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Question added successfully!")
            return redirect('add-question')
    else:
        form = QuestionForm()

    return render(request, 'main/add_question.html', {'form': form})
@login_required
def dashboard(request):
    responses = UserQuizResponse.objects.filter(user=request.user)
    total_quizzes = responses.values('question__topic').distinct().count()
    total_questions = responses.count()
    correct_answers = responses.filter(is_correct=True).count()

    # Calculate average score
    topic_scores = {}
    for topic in QuizTopic.objects.all():
        topic_responses = responses.filter(question__topic=topic)
        if topic_responses.exists():
            correct = topic_responses.filter(is_correct=True).count()
            accuracy = (correct / topic_responses.count()) * 100
            topic_scores[topic] = accuracy

    avg_score = round(sum(topic_scores.values()) / len(topic_scores), 2) if topic_scores else 0
    accuracy = round((correct_answers / total_questions) * 100, 2) if total_questions > 0 else 0

    # Detect weak topics (accuracy < 50%)
    weak_topics = [t for t, acc in topic_scores.items() if acc < 50]

    # Recommend quizzes
    recommended = QuizTopic.objects.exclude(id__in=[t.id for t in weak_topics])[:3]

    return render(request, 'main/dashboard.html', {
        'total_quizzes': total_quizzes,
        'avg_score': avg_score,
        'accuracy': accuracy,
        'weak_topics': weak_topics,
        'recommended': recommended
    })


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_dashboard(request):
    context = {
        'total_users': User.objects.count(),
        'total_topics': QuizTopic.objects.count(),
        'total_questions': Question.objects.count(),
        'total_attempts': UserQuizResponse.objects.count(),
    }
    return render(request, 'main/admin_dashboard.html', context)
def interview_resources(request):
    exam_resources = Resource.objects.filter(category='exam')
    interview_resources =Resource.objects.filter(category='interview')

    return render(request, 'main/interview_resources.html', {
        'exam_resources': exam_resources,
        'interview_resources': interview_resources,
    })