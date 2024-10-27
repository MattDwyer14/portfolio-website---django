from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Project, Technology

def project_list(request):
    # Get technologies used in projects and count usage
    technologies = Technology.objects.filter(projects__isnull=False) \
                                      .annotate(project_count=Count('projects')) \
                                      .order_by('name')
    
    selected_techs = request.GET.getlist('technologies')
    
    projects = Project.objects.all()
    if selected_techs:
        projects = projects.filter(technologies__name__in=selected_techs).distinct()
    
    context = {
        'projects': projects,
        'technologies': technologies,
        'selected_techs': selected_techs
    }
    return render(request, 'projects/list.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/detail.html', {'project': project})