import pytz as pytz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from .forms import CustomUserCreationForm, CustomAuthenticationForm, LessonForm, ProfileForm
from .models import Course, Lesson, Test, Question, Profile


def home(request):
    courses = Course.objects.all()
    profile_picture_url = None

    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
            profile_picture_url = user_profile.profile_picture.url
        except Profile.DoesNotExist:
            # Handle the case where the profile does not exist
            pass

    return render(request, 'home.html', {'courses': courses, 'profile_picture_url': profile_picture_url})
# @login_required
# def home(request):
#     # Assuming user_profile is obtained correctly
#     user_profile = request.user.profile
#
#     profile_picture_url = None
#     if user_profile.profile_picture and user_profile.profile_picture.file:
#         # Check if there is a profile picture associated and it has a file
#         profile_picture_url = user_profile.profile_picture.url
#
#     return render(request, 'home.html', {'profile_picture_url': profile_picture_url})
# def home(request):
#     courses = Course.objects.all()
#     if request.user.is_authenticated:  # Ensure the user is authenticated
#         user_profile = Profile.objects.get(user=request.user)
#         profile_picture_url = user_profile.profile_picture.url
#     else:
#         profile_picture_url = None
#     return render(request, 'home.html', {'courses': courses, 'profile_picture_url': profile_picture_url})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    course = lesson.course

    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson updated successfully.')
            return redirect('lesson_detail', lesson_id=lesson_id)
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'lesson_detail.html', {
        'lesson': lesson,
        'form': form,
        'course': course,
    })


def course_lessons(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lesson_set.all()
    return render(request, 'course_lessons.html', {'course': course, 'lessons': lessons})


def start_test(request, test_id):
    test = Test.objects.get(id=test_id)
    questions = Question.objects.filter(test=test)

    return render(request, 'start_test.html', {'test': test, 'questions': questions})


def submit_test(request, test_id):
    if request.method == 'POST':
        test = Test.objects.get(id=test_id)
        questions = Question.objects.filter(test=test)
        score = 0
        for question in questions:
            selected_choice = request.POST.get(f'question_{question.id}', None)
            if selected_choice == question.correct_choice:
                score += 1
        test.end_time = timezone.now()
        test.save()

        return render(request, 'test_result.html', {'test': test, 'score': score})
    return redirect('start_test', test_id)

def test_result(request, test_id):
    test = Test.objects.get(id=test_id)
    questions = Question.objects.filter(test=test)
    score = 0

    for question in questions:
        selected_choice = request.POST.get(f'question_{question.id}', None)
        if selected_choice == question.correct_choice:
            score += 1

    # Lấy thời gian hiện tại theo múi giờ UTC
    current_time_utc = timezone.now()

    # Chuyển múi giờ sang múi giờ Việt Nam
    vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    current_time_vn = current_time_utc.astimezone(vn_tz)

    # Cập nhật thời gian kết thúc của bài kiểm tra
    test.end_time = current_time_vn
    test.save()

    # Tạo URL cho danh sách bài học
    course_id = test.course.id
    course_lessons_url = reverse('course_lessons', args=[course_id])

    return render(request, 'test_result.html', {'test': test, 'score': score, 'current_time_vn': current_time_vn ,course_lessons_url:'course_id'})

# def profile_view(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     user_profile = get_object_or_404(Profile, user=user)
#     return render(request, 'profile.html', {'user_profile': user_profile})

# def profile_view(request, user_id):
#     try:
#         user = get_object_or_404(User, id=user_id)
#         user_profile = get_object_or_404(Profile, user=user)
#     except Profile.DoesNotExist:
#         raise Http404("Profile does not exist")
#     if request.user.is_authenticated:
#         {'user_profile': user_profile}['user_authenticated'] = True
#     return render(request, 'profile.html', {'user_profile': user_profile})

def profile_view(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)
        user_profile = get_object_or_404(Profile, user=user)
        return render(request, 'profile.html', {'user_profile': user_profile})
    except Profile.DoesNotExist:
        return HttpResponse("Profile does not exist")

# def profile_view(request, user_id):
#     # Use get_object_or_404 to get the user's profile or return a 404 response if the profile is not found
#     user_profile = get_object_or_404(Profile, user__id=user_id)
#
#     # Check if the profile picture exists before accessing its URL
#     profile_picture_url = user_profile.profile_picture.url if user_profile.profile_picture else None
#
#     return render(request, 'profile.html', {'user_profile': user_profile, 'profile_picture_url': profile_picture_url})

def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', user_id=user_profile.user.id)
    else:
        form = ProfileForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'form': form, 'user_profile': user_profile})
def huong_dan_su_dung(request):
    return render(request, 'huong_dan_su_dung.html')

# def edit_profile(request):
#     user_profile = get_object_or_404(Profile, user=request.user)
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_view')  # Redirect to the user profile view
#     else:
#         form = ProfileForm(instance=user_profile)
#
#     return render(request, 'edit_profile.html', {'form': form})



