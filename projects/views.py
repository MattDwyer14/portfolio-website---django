from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Project, Technology, ProjectType

def project_list(request):
    technologies = Technology.objects.filter(projects__isnull=False) \
                                      .annotate(project_count=Count('projects')) \
                                      .order_by('name')
    
    project_types = ProjectType.objects.filter(projects__isnull=False) \
                                       .annotate(project_count=Count('projects')) \
                                       .order_by('name')
    
    selected_techs = request.GET.getlist('technologies')
    selected_types = request.GET.getlist('projecttype')
    
    projects = Project.objects.all()
    if selected_techs:
        projects = projects.filter(technologies__name__in=selected_techs).distinct()
    if selected_types:
        projects = projects.filter(projecttype__name__in=selected_types).distinct()
    
    context = {
        'projects': projects,
        'technologies': technologies,
        'projecttype': project_types,
        'selected_techs': selected_techs,
        'selected_types': selected_types
    }
    return render(request, 'projects/list.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/detail.html', {'project': project})
