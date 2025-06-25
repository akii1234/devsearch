from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

data = [
    {"id": 1, "title": "Introduction to Python", "description": "A beginner's guide to Python programming."},
    {"id": 2, "title": "Data Structures", "description": "Understanding lists, dictionaries, sets, and tuples."},
    {"id": 3, "title": "Web Development", "description": "Building websites with HTML, CSS, and JavaScript."},
    {"id": 4, "title": "APIs with FastAPI", "description": "Creating and testing REST APIs using FastAPI."},
    {"id": 5, "title": "Databases", "description": "An introduction to SQL and NoSQL databases."},
    {"id": 6, "title": "Machine Learning Basics", "description": "Core concepts of supervised and unsupervised learning."},
    {"id": 7, "title": "DevOps Essentials", "description": "Overview of CI/CD, Docker, and cloud deployments."},
    {"id": 8, "title": "Unit Testing in Python", "description": "Writing test cases using unittest and pytest."},
    {"id": 9, "title": "Git & GitHub", "description": "Version control fundamentals and collaboration with GitHub."},
    {"id": 10, "title": "Interview Preparation", "description": "Tips and practice questions for coding interviews."}
]



def projects(request):
    data = Project.objects.all()
    context = {'projects': data}
    return render(request,'projects/projects.html',context)


def project(request,pk):
    project_obj = Project.objects.get(id=pk)
    tags = project_obj.tags.all()
    context = {'project':project_obj,'tags':tags}              
    return render(request,'projects/single-projects.html',context)
