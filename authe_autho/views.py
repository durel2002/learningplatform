from django.shortcuts import render
from .forms import SigninForm, SignupForm

# Create your views here.
def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
    else:
        form = SigninForm()

    return render(request, "authe_autho/sigin_in.html", {"form": form})