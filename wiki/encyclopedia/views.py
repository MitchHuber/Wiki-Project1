from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import random, markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def look(request,title):
    if util.get_entry(title) == None:
        return HttpResponseNotFound(f'<h1> There was no entry with the title of {title}')
    return render(request, "encyclopedia/entry.html",{
        "content": markdown2.markdown(util.get_entry(title)), "title": title
    })

def title(request, title):
    if util.get_entry(title) == None:
        return HttpResponseNotFound(f'<h1>There was no entry found with the title of {title}')
    return render(request, "encyclopedia/entry.html", {
        "content": markdown2.markdown(util.get_entry(title)), "title": title
    })

def entry(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    if util.get_entry(title):
        return HttpResponseNotFound(f'<h1>There was already an entry with the title of {title}</h1>')
    else:
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html",{
            "content": markdown2.markdown(util.get_entry(title))
            })

def edit(request):
    title = request.POST.get('title')
    information = request.POST.get('content')

    return render(request, "encyclopedia/edit.html", {
        "content": markdown2.markdown(information), "title": title
    })

def saventry(request):
    title = request.POST.get('title')
    information = request.POST.get('content')

    util.save_entry(title, information)
    return render(request, "encyclopedia/entry.html",{
        "content": markdown2.markdown(util.get_entry(title)), "title": title
    })

def newPage(request):
    return render(request, "encyclopedia/newpage.html")

def ranentry(request):
    list = util.list_entries()
    value = random.randint(0, len(list))

    return render(request, "encyclopedia/entry.html", {
        "content": markdown2.markdown(util.get_entry(list[value - 1]))
    })

def search(request):
    search = request.POST.get('q')
    entries = util.list_entries()
    matches = []

    for entry in entries:
        if search in entry:
            matches.append(entry)
    if not matches:
        matches = None

    return render(request, "encyclopedia/search.html",{
        "matches": matches
    })
