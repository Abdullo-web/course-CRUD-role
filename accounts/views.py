from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth import authenticate,login,logout
from .permissions import permission_required


def register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            return render(request, 'register.html', {'error': 'zapolnite polya'})
        user = User.objects.filter(username=username).exists()
    
        if user:
            return render(request, 'register.html', {'error':'imya zanity'})
    
        user = User.objects.create_user(username=username,password=password)
    
        return redirect('login')
    return render(request,'register.html')


def login_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            return render(request, 'login.html', {'error': 'zapolnite polya'})
        
        user = authenticate(request, username = username, password=password)
        
        if user is None:
            return render(request, 'login.html', {'error': 'takoy polzovatel ne sushetvuet'})
        
        login(request,user)
            
        return redirect('view_course')
        
    return render(request,'login.html')

def logout_user(request):

    logout(request)
    
    return redirect('login')

@permission_required('admin','manager')
def create_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        
        if not title or not description or not price:
            return render(request, 'create_course.html', {'error': 'zapolnite polya'})
        
        Course.objects.create(title=title,description=description,price=price)
        
        return redirect('view_course')
    
    return render(request, 'create_course.html')


@permission_required('admin','manager','editor','user')
def view_course(request):
    courses = Course.objects.all()
    
    return render(request, 'view_course.html', {'courses': courses})


@permission_required('admin','manager')
def update_course(request,id):
    course = get_object_or_404(Course ,id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
            
        if not title or not description or not price:
            return render(request, 'update_course.html', {'course': course,'error': 'zapolnite polya'})

        course.title = title
        course.description = description
        course.price = price
        course.save()
        
        return redirect('view_course')
    
    return render(request, 'update_course.html', {'course': course})



@permission_required('admin')
def delete_course(request,id):
    course = get_object_or_404(Course,id=id)
    if request.method == 'POST':
        course.delete()
        return redirect('view_course')

    return redirect('view_course')
        
        
        
        
        
        
        
        
