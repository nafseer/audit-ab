from django.shortcuts import render
from .models import LeadsList
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
class LeadsListView(TemplateView):

    model = LeadsList
    template_name = 'leadslist.html'
    context_object_name = 'leadslist'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(LeadsListView, self).get_context_data(**kwargs)
        leadslist = LeadsList.objects.all()
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        print(leadslist)
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        page = self.request.GET.get('page')
        # paginator = Paginator(users, self.paginate_by)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users= paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        context['leadslist'] = leadslist
        return context


class LeadsListCreateView(CreateView):
    model = LeadsList
    template_name = 'leadslistcreate.html'
    fields = ('leads_id','leads_name','leads_description',)
    success_url = reverse_lazy('userroles')
    context_object_name = 'leadslist'

    def get_context_data(self,*args, **kwargs):
        context = super(LeadsListCreateView, self).get_context_data(**kwargs)
        i=context['form']
        print(context)
        print(i)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('leads_name', css_class='form-group col-md-6 mb-0'),
                Column('leads_description', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            

        )
        

        return context