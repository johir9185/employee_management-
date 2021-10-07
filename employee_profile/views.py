from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, UpdateView

from employee_profile.forms import UserProfileForm
from employee_profile.models import Users


class UserCreateTemplateView(TemplateView):
    template_name = 'users_create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = UserProfileForm()
        return data


class UserSaveView(TemplateView):
    template_name = 'users_create.html'

    def post(self, request, *args, **kwargs):
        form_u = UserProfileForm(data=request.POST)

        # print(form_u.cleaned_data)
        if form_u.is_valid():
            # form_u.cle
            Users.objects.create(**form_u.cleaned_data)
            return self.render_to_response(context={'message': 'User Created successfully!', 'form': UserProfileForm()})
        else:
            return self.render_to_response(context={'message': 'Please try again!', 'form': form_u})


class UserListTemplateView(TemplateView):
    template_name = 'users_list.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['users'] = Users.objects.all()
        return data


class UserUpdate(UpdateView):
    model = Users
    fields = ('full_name', 'email', 'username', 'dob', 'password')
    template_name = 'users_update.html'
    context_object_name = 'users'
    success_url = "/users/"  # posts list url

    # def post(self, request, *args, **kwargs):
    #     form_u = UserProfileForm(data=request.POST)
    #
    #     # print(form_u.cleaned_data)
    #     if form_u.is_valid():
    #         # form_u.cle
    #         Users.objects.create(**form_u.cleaned_data)
    #     return self.render_to_response(context={'message': 'User Updated successfully!', 'form': form_u})
