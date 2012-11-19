from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from models import *
from forms import *

@login_required
def new(request):

    output = {}
    form = ProjectForm()

    if request.POST:
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print form.errors

    output['form'] = form

    return render_to_response("project/new.html", output, context_instance=RequestContext(request))

@login_required
def list(request, username, type=None):

    output = {}
    user = User.objects.get(username=username)
    finished = False
    if type == 'closed':
        finished = True

    if type == "all":
        projects = Project.objects.filter(creator=user)[:10]
    else:
        projects = Project.objects.filter(creator=user).filter(finished=finished)[:10]

    output['user'] = user
    output['projects'] = projects
    output['finished'] = finished
    output['type'] = type

    return render_to_response("project/list.html", output, context_instance=RequestContext(request))

@login_required
def show(request, id, slug):

    output = {}
    project = get_object_or_404(Project, id=id)
    comments = CommentProject.objects.filter(project=project).order_by('-id')[:10]
    comment_form = CommentProjectForm(initial={'project': id, 'creator': request.user.id})

    trainings = TrainingDay.objects.filter(project=project)
    exercises = TrainingExercise.objects.filter(day__in=trainings)
    evolutions = Evolution.objects.filter(project=project).order_by('-id')[:6]
    meals = Meal.objects.filter(project=project).order_by('meal')

    output['project'] = project
    output['comments'] = comments
    output['comment_form'] = comment_form
    output['trainings'] = trainings
    output['exercises'] = exercises
    output['evolutions'] = evolutions
    output['meals'] = meals

    return render_to_response("project/show.html", output, context_instance=RequestContext(request))

@login_required
def comment(request, project):

    output = {}
    project = get_object_or_404(Project, id=project)

    if request.POST:
        form = CommentProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('project.views.show', kwargs={'id': project.id, 'slug': project.slugify()}))
        else:
            return HttpResponse(form)

@login_required
def create_training_day(request, project):

    output = {}
    project = get_object_or_404(Project, id=project)
    comments = CommentProject.objects.filter(project=project).order_by('-id')[:10]
    comment_form = CommentProjectForm(initial={'project': project, 'creator': request.user.id})

    if not project.creator == request.user:
        raise Http404

    form = TrainingDayForm(initial={'project': project.id})

    if request.POST:
        form = TrainingDayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse('project.views.show', kwargs={'id': project.id, 'slug': project.slugify()}))


    output['project'] = project
    output['comments'] = comments
    output['comment_form'] = comment_form
    output['form'] = form
    
    return render_to_response("project/create_training_day.html", output, context_instance=RequestContext(request))

@login_required
def create_training_exercise(request, project):

    output = {}
    project = get_object_or_404(Project, id=project)
    comments = CommentProject.objects.filter(project=project).order_by('-id')[:10]
    comment_form = CommentProjectForm(initial={'project': project, 'creator': request.user.id})

    if not project.creator == request.user:
        raise Http404

    form = TrainingExerciseForm()
    form.fields["day"].queryset = TrainingDay.objects.filter(project=project)

    if request.POST:
        form = TrainingExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse('project.views.show', kwargs={'id': project.id, 'slug': project.slugify()}))


    output['project'] = project
    output['comments'] = comments
    output['comment_form'] = comment_form
    output['form'] = form
    
    return render_to_response("project/create_training_exercise.html", output, context_instance=RequestContext(request))

@login_required
def delete_train(request, train):

    train = TrainingDay.objects.get(id=train)
    if not train.project.creator == request.user:
        raise Http404    

    train.delete()
    return redirect(reverse('project.views.show', kwargs={'id': train.project.id, 'slug': train.project.slugify()}))

@login_required
def create_evolution(request, project):

    output = {}
    project = get_object_or_404(Project, id=project)
    comments = CommentProject.objects.filter(project=project).order_by('-id')[:10]
    comment_form = CommentProjectForm(initial={'project': project, 'creator': request.user.id})

    if not project.creator == request.user:
        raise Http404

    form = EvolutionForm(initial={'project': project.id})

    if request.POST:
        form = EvolutionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse('project.views.show', kwargs={'id': project.id, 'slug': project.slugify()}))


    output['project'] = project
    output['comments'] = comments
    output['comment_form'] = comment_form
    output['form'] = form
    
    return render_to_response("project/create_evolution.html", output, context_instance=RequestContext(request))

@login_required
def create_meal(request, project):

    output = {}
    project = get_object_or_404(Project, id=project)
    comments = CommentProject.objects.filter(project=project).order_by('-id')[:10]
    comment_form = CommentProjectForm(initial={'project': project, 'creator': request.user.id})

    if not project.creator == request.user:
        raise Http404

    if request.POST:
        meal = request.POST.get('meal')
        foods = request.POST.getlist('foods')

        meal = Meal(project=project, meal=meal)
        meal.save()

        for food in foods:
            if food:
                food = Food(meal=meal, food=food)
                food.save()
                food = None

        return redirect(reverse('project.views.show', kwargs={'id': project.id, 'slug': project.slugify()}))

    output['project'] = project
    output['comments'] = comments
    output['comment_form'] = comment_form

    return render_to_response("project/create_meal.html", output, context_instance=RequestContext(request))

@login_required
def create_suplement(request, project):

    output = {}
    project = get_object_or_404(Project, id=project)
    comments = CommentProject.objects.filter(project=project).order_by('-id')[:10]
    comment_form = CommentProjectForm(initial={'project': project, 'creator': request.user.id})

    if not project.creator == request.user:
        raise Http404

    form = SuplementForm(initial={'project': project.id})

    if request.POST:
        form = SuplementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse('project.views.show', kwargs={'id': project.id, 'slug': project.slugify()}))


    output['project'] = project
    output['comments'] = comments
    output['comment_form'] = comment_form
    output['form'] = form
    
    return render_to_response("project/create_suplement.html", output, context_instance=RequestContext(request))