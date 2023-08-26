from django.http import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from GGDC.models import *
from .forms import FirstyearAdmission
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages


# Create your views here.


def home(request):
    # principal = Principal.objects.all()[:8]
    principal = Principal.objects.filter().only('picture','name','joining_date','leaving_date').order_by('-joining_date')
    news = News.objects.all().order_by('-date_uploaded')[:5]
    gallery = Gallery.objects.all().order_by('-date')[:8]
    newsbanner = NewsBanner.objects.all().order_by('-date_uploaded')[:5]
    pdata = {
        'principal': principal,
        'news': news,
        'gallery' : gallery,
        'newsbanner' : newsbanner
    }
    return render(request, 'index.html', pdata)


def intermediat(request):
    return render(request, 'intermediat.html', {})


def bsc(request):
    return render(request, 'bsc.html', {})


def degree_programs(request):
    return render(request, 'degree_programs.html', {})


def vision(request):
    return render(request, 'vision.html', {})


def mission(request):
    return render(request, 'mission.html', {})


def history(request):
    return render(request, 'history.html', {})


def principal(request):
    return render(request, 'principal.html', {})


def faculty(request):
    # faculty = Faculty.objects.all()[:11]
    faculty = Faculty.objects.filter(status = 'Active')
    bba= Faculty.objects.filter(status = 'Active', department = 'BBA')
    botany= Faculty.objects.filter(status = 'Active', department = 'Botany')
    bsit= Faculty.objects.filter(status = 'Active', department = 'BSIT')
    commerce= Faculty.objects.filter(status = 'Active', department = 'Commerce')
    chemistry= Faculty.objects.filter(status = 'Active', department = 'Chemistry')
    economics= Faculty.objects.filter(status = 'Active', department = 'Economics')
    english= Faculty.objects.filter(status = 'Active', department = 'English')
    home_economics= Faculty.objects.filter(status = 'Active', department = 'Home Economics')
    islamiat= Faculty.objects.filter(status = 'Active', department = 'Islamiat')
    mathematics= Faculty.objects.filter(status = 'Active', department = 'Mathematics')
    pakistan_studies= Faculty.objects.filter(status = 'Active', department = 'Pakistan Studies')
    physical_education= Faculty.objects.filter(status = 'Active', department = 'Physical Education')
    physics= Faculty.objects.filter(status = 'Active', department = 'Physics')
    sindhi= Faculty.objects.filter(status = 'Active', department = 'Sindhi')
    urdu= Faculty.objects.filter(status = 'Active', department = 'Urdu')
    zoology= Faculty.objects.filter(status = 'Active', department = 'Zoology')
    data = {
        'faculty': faculty,
        'bba': bba,
        'botany' : botany,
        'bsit' : bsit,
        'commerce' : commerce,
        'chemistry' : chemistry,
        'economics' : economics,
        'english' : english,
        'home_economics' : home_economics,
        'islamiat' : islamiat,
        'mathematics' : mathematics,
        'pakistan_studies' : pakistan_studies,
        'physical_education' : physical_education,
        'physics' : physics,
        'sindhi' : sindhi,
        'urdu' : urdu,
        'zoology' : zoology,
    }
    return render(request, 'faculty.html', data)


def about(request):
    return render(request, 'about.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def blog_cat(request):
    # return render(request, 'blog_cat.html', {})
    return render(request, 'liabrary.html', {})


def blog_post(request):
    # return render(request, 'blog_post.html', {})
    return render(request, 'liabrary.html', {})


def admission(request):
    if request.user.is_anonymous:
        return redirect("/register")
    else:
        if request.method== "POST":
            # print("hello")
            form = FirstyearAdmission(request.POST, request.FILES)
            if form.is_valid():
                # print('in if')
                form.save()
                return redirect('/admission')
            else:
                print(form.errors)
        else:
            form = FirstyearAdmission()
            firstyearform = { 'form': form}
            return render(request, 'admission_form.html', firstyearform)


def download_books(request):
    if request.user.is_anonymous:
        return redirect("/login")
    bsit = Books.objects.filter(department = 'BSIT')
    bba = Books.objects.filter(department = 'BBA')
    context = {
        'bsit': bsit,
        'bba': bba
    }
    return render(request, 'books.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(
                fh.read(), content_type="application/admin_upload")
            response['content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404


def register(request):
    admission_open = True
    if admission_open == True:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            print('POST receive')
            

            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username Taken!')
                    return redirect('/register')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Taken!')
                    return redirect('/register')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save();
                    # return render(request, 'admission_form.html')
                    return redirect('/login')
            else:
                messages.error(request, 'Password Not Matching!')
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'admission_close.html')
    



def login_user(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.get(email=email.lower()).username
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/index')
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')
    elif request.user.is_authenticated:
        return redirect('/index')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect("/login")

# user: Aisha password: Aisha12345678
