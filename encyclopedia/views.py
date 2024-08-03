from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import choice
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getEntry(request, title):
    entry = util.get_entry(title)
    if entry != None:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": markdown.markdown(entry)
        })
    else:
        return render(request, "encyclopedia/error404.html")

def search(request):
    entries = util.list_entries()
    if request.method == "GET":
        query = request.GET.get("q")
        if query in entries:
            return redirect(f"/wiki/{query}")
        else:
            searchResults = []
            for i in entries:
                if query.lower() in i.lower():
                    searchResults.append(i)
            return render(request, "encyclopedia/results.html", {
                "searchResults": searchResults
            })
        
def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("textarea")
        if util.get_entry(title) == None:
            util.save_entry(title, content)
        else:
            return HttpResponse("An encyclopedia entry already exists with the provided title. Please change the title")
        return redirect(f"/wiki/{title}")
    else:
        return render(request, "encyclopedia/new.html")
    
def edit(request, title):
    entry = util.get_entry(title)
    if request.method == "POST":
        editedTitle = request.POST.get("title")
        content = request.POST.get("textarea")
        if (editedTitle != title):
            if util.get_entry(editedTitle) != None:
                return HttpResponse("An encyclopedia entry already exists with the provided title. Please change the title")
        util.save_entry(title, content)
        return redirect(f"/wiki/{editedTitle}")
    else:
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": entry
        })
def random(request):
    entries = util.list_entries()
    randomPage = choice(entries)
    if entries:
        return redirect(f"/wiki/{randomPage}")
    else:
        return render(request, "encyclopedia/index.html")




        
