from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView

from .forms import ProfileForm
from .models import Profile


# @login_required
# def profile(request):
#     return render(request, "accounts/profile.html")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


profile = ProfileView.as_view()


def profile_edit(request):
    try:
        profile = request.user.profile
        print(profile)
    except Profile.DoesNotExist:
        profile = None

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user

            # print(profile.)
            profile.save()

            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form": form,
        "profile": profile,
    }

    return render(request, "accounts/profile_form.html", context)
