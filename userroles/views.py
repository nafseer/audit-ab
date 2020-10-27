from django.shortcuts import render
from .models import UserRoles
# Create your views here.
from django.views.generic import ListView,CreateView,TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.detail import DetailView





# Create your views here.
class UserRolesListView(TemplateView):

    model = UserRoles
    template_name = 'userroles.html'
    context_object_name = 'userroles'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UserRolesListView, self).get_context_data(**kwargs)
        userroles = UserRoles.objects.all()
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        print(userroles)
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        page = self.request.GET.get('page')
        # paginator = Paginator(users, self.paginate_by)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users= paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        context['userroles'] = userroles
        return context

# add user in template
# class UserSignUpView(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('userslist')
#     template_name = 'register.html'

class UserRolesCreateView(CreateView):
    model = UserRoles
    template_name = 'userrolescreate.html'
    fields = ('role_id','role_name','role_description','module_one','module_two','module_three','module_four','module_five')
    success_url = reverse_lazy('userroles')
    context_object_name = 'userroless'

    def get_context_data(self,*args, **kwargs):
        context = super(UserRolesCreateView, self).get_context_data(**kwargs)
        i=context['form']
        print(context)
        print(i)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('role_name', css_class='form-group col-md-6 mb-0'),
                Column('role_description', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                
                Column('module_one', css_class='form-group col-md-4 mb-0'),
                Column('module_two', css_class='form-group col-md-4 mb-0'),
                Column('module_three', css_class='form-group col-md-4 mb-0'),
                Column('module_four', css_class='form-group col-md-4 mb-0'),
                Column('module_five', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            
            

        )
        
        def savevalues(request):
            if request.method=="POST":
                if request.POST.get("modulename"):
                    savedata=UserRoles()
                    savedata.modulename=request.POST.get("modulename")
                    savedata.save()
                    return render(request,'/userroles')
            else:
                    return render(request,'/userroles')


        return context