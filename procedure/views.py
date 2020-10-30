from django.shortcuts import render
from .models import ProcedureMaster
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
class ProcedureListView(TemplateView):

    model = ProcedureMaster
    template_name = 'procedures.html'
    context_object_name = 'procedures'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProcedureListView, self).get_context_data(**kwargs)
        procedures = ProcedureMaster.objects.all()
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        print(procedures)
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        page = self.request.GET.get('page')
        # paginator = Paginator(users, self.paginate_by)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users= paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        context['procedures'] = procedures
        return context


class ProcedureCreateView(CreateView):
    model = ProcedureMaster
    template_name = 'procedurecreate.html'
    fields = ('auditee_name','started_on','completed_on','reviewer','reviewed_on','time_taken')
    success_url = reverse_lazy('companylist')
    context_object_name = 'procedures'

    def get_context_data(self,*args, **kwargs):
        context = super(ProcedureCreateView, self).get_context_data(**kwargs)
        i=context['form']
        print(context)
        print(i)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('auditee_name', css_class='form-group col-md-6 mb-0'),
                Column('started_on', css_class='form-group col-md-6 mb-0'),
                Column('completed_on', css_class='form-group col-md-6 mb-0'),
                Column('reviewer', css_class='form-group col-md-6 mb-0'),
                Column('reviewed_on', css_class='form-group col-md-6 mb-0'),
                Column('time_taken', css_class='form-group col-md-6 mb-0'),
               

                css_class='form-row'
            ),
            

        )
        

        return context

class CommentCreateView(CreateView):
    model = ProcedureMaster
    template_name = 'procedures.html'
    fields = ('comments','notesfile',)
    success_url = reverse_lazy('companylist')
    context_object_name = 'procedures'

    def get_context_data(self,*args, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        procedures = ProcedureMaster.objects.all()
        i=context['form']
        print(context)
        print(i)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('comments', css_class='form-group col-md-6 mb-0'),
                Column('notesfile', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            

        )
        page = self.request.GET.get('page')
        context['procedures'] = procedures
        return context

class ProceduresListView(TemplateView):

    model = ProcedureMaster
    template_name = 'procedures.html'
    context_object_name = 'procedures'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProceduresListView, self).get_context_data(**kwargs)
        procedures = ProcedureMaster.objects.all()
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        print(procedures)
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        page = self.request.GET.get('page')
        # paginator = Paginator(users, self.paginate_by)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users= paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        context['procedures'] = procedures
        return context


