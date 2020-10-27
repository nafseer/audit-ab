# from django.shortcuts import render
# from .models import Profile
# # Create your views here.
# from django.views.generic import ListView,CreateView,TemplateView
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.urls import reverse_lazy
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
# from django.views.generic import CreateView
# from .forms import SignUpForm
# from django.views.generic.edit import UpdateView,DeleteView
# from django.views.generic.detail import DetailView





# # Create your views here.
# @method_decorator(login_required, name='dispatch')
# class UsersListView(TemplateView):

#     model = User
#     template_name = 'users.html'
#     context_object_name = 'users'
#     # paginate_by = 5

#     def get_context_data(self, **kwargs):
#         context = super(UsersListView, self).get_context_data(**kwargs)
#         users = User.objects.all()
#         print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
#         print(users)
#         print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
#         roles = self.get_queryset()
#         page = self.request.GET.get('page')
#         paginator = Paginator(roles, self.paginate_by)
#         try:
#             roles = paginator.page(page)
#         except PageNotAnInteger:
#             roles= paginator.page(1)
#         except EmptyPage:
#             roles = paginator.page(paginator.num_pages)
#         context['users'] = users
#         return context

# # add user in template
# class UserSignUpView(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('users')
#     template_name = 'register.html'

