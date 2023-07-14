from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import CreateView

from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm


    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.save()

        return redirect('homepage')
