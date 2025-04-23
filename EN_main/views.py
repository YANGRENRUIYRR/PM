from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from main.models import Website, Username
from main.forms import WebsiteForm, UsernameForm
def help(request):
    return render(request, 'EN_main/help.html')
def index(request):
    return render(request, 'EN_main/index.html')
@login_required(login_url='/EN/accounts/login')
def websites(request):
    websites = Website.objects.filter(owner=request.user).order_by('date_added')
    context = {'websites': websites}
    return render(request, 'EN_main/websites.html', context)
@login_required(login_url='/EN/accounts/login')
def website(request, website_id):
    website = Website.objects.get(id=website_id)
    if website.owner != request.user:
        raise Http404
    usernames = website.username_set.order_by('-date_added')
    context = {'website': website, 'usernames': usernames}
    return render(request, 'EN_main/website.html', context)
@login_required(login_url='/EN/accounts/login')
def new_website(request):
    if request.method != 'POST':
        form = WebsiteForm()
    else:
        form = WebsiteForm(data=request.POST)
        if form.is_valid():
            new_website = form.save(commit=False)
            new_website.owner = request.user
            new_website.save()
            return redirect('EN_main:websites')
    context = {'form': form}
    return render(request, 'EN_main/new_website.html', context)
@login_required(login_url='/EN/accounts/login')
def new_username(request, website_id):
    """Add a new username for a particular website."""
    website = Website.objects.get(id=website_id)
    if(not (request.user==website.owner)):
        raise Http404
    if request.method != 'POST':
        form = UsernameForm()
    else:
        form = UsernameForm(data=request.POST)
        if form.is_valid():
            new_username = form.save(commit=False)
            new_username.website = website
            new_username.save()
            return redirect('EN_main:website', website_id=website_id)
    context = {'website': website, 'form': form}
    return render(request, 'EN_main/new_username.html', context)
@login_required(login_url='/EN/accounts/login')
def edit_username(request, username_id):
    username = Username.objects.get(id=username_id)
    website = username.website
    if website.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = UsernameForm(instance=username)
    else:
        form = UsernameForm(instance=username, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('EN_main:website', website_id=website.id)
    context = {'username': username, 'website': website, 'form': form}
    return render(request, 'EN_main/edit_username.html', context)