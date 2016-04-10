from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from .models import Profile, Python, Web, WorkHistory, Contact, Education, General, OS, Deployment, Testing, Blog

def home(request):
    tagline = Profile.objects.all()[0].tagline

    return render(request, 'index.html', {'tagline':tagline})

def blog(request):

    blog_list = Blog.objects.order_by('-date_ts')
    for blog in blog_list:
        blog.date_ts = blog.date_ts.strftime('%B %d, %Y')
    paginator = Paginator(blog_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'blogs': blogs})

def about(request):
    return render(request, 'about.html')

def resume(request):
    tagline = Profile.objects.all()[0].tagline
    libraries = ', '.join([obj.library for obj in Python.objects.all()])
    web = ', '.join([obj.lang for obj in Web.objects.all()])
    contact = Contact.objects.all()[0]
    general = ', '.join([obj.name for obj in General.objects.all()])
    deployment = ', '.join([obj.name for obj in Deployment.objects.all()])
    testing = ', '.join([obj.name for obj in Testing.objects.all()])
    os = ', '.join([obj.name for obj in OS.objects.all()])
    work = WorkHistory.objects.order_by('-start_date')
    for obj in work:
        obj.title = obj.title.upper()
        obj.company = obj.company.upper()
        obj.location = obj.location.upper()
        obj.start_date = obj.start_date.strftime('%B %Y').upper()
        if obj.end_date:
            obj.end_date = obj.end_date.strftime('%B %Y').upper()

    education = Education.objects.order_by('-start_date')
    for obj in education:
        obj.start_date = obj.start_date.strftime('%Y').upper()
        if obj.end_date:
            obj.end_date = obj.end_date.strftime('%Y').upper()

    return render(request, 'resume.html', {
        'tagline': tagline,
        'libraries': libraries,
        'web': web, 'work': work,
        'contact': contact,
        'education': education,
        'general': general,
        'deployment': deployment,
        'testing': testing,
        'OS': os,

    })

def contact(request):
    return render(request, 'contact.html')

def lightbox(request):
    return render(request, 'lightbox.html')

def taskdaddy(request):
    return render(request, 'taskdaddy.html')

def spoiler(request):
    return render(request, 'spoiler.html')

def projects(request):
    return render(request, 'projects.html')

