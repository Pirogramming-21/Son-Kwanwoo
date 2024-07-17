from django.shortcuts import render, redirect, get_object_or_404
from .models import Tool
from .forms import ToolForm

def tool_list(req):
    tools = Tool.objects.all()
    
    search_txt = req.GET.get('search_txt')
    if search_txt:
        tools = tools.filter(name__icontains=search_txt)
    ctx = {'tools': tools}
    return render(req, "tools/tool_list.html", ctx)

def tool_create(req):
    if req.method == "GET":
        form = ToolForm()
        ctx = {'form': form}
        return render(req, "tools/tool_create.html", ctx)
    
    form = ToolForm(req.POST)
    if form.is_valid():
        form.save()
        return redirect("tools:list")
    
    ctx = {'form': form}
    return render(req, "tools/tool_create.html", ctx)

def tool_update(req, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if req.method == "GET":
        form = ToolForm(instance=tool)
        ctx = {"form": form, "pk": pk}
        return render(req, 'tools/tool_update.html', ctx)
    
    form = ToolForm(req.POST, instance=tool)
    if form.is_valid():
        form.save()
        return redirect("tools:list")
    
    ctx = {"form": form, "pk": pk}
    return render(req, 'tools/tool_update.html', ctx)

def tool_detail(req, pk):
    tool = get_object_or_404(Tool, pk=pk)
    ctx = {'tool': tool}
    return render(req, 'tools/tool_detail.html', ctx)

def tool_delete(req, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if req.method == "POST":
        tool.delete()
        return redirect("tools:list")
    ctx = {'tool': tool}
    return render(req, "tools/tool_confirm_delete.html", ctx)
