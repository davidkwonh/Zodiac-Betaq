from django.shortcuts import render, redirect
from . forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "CONGRAGULATIONS ON REGISTERING U SMART PIECE OF ****")
            return redirect("main:homepage")
        messages.error(request, "YOU F***ED UP IDIOT")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form":form})