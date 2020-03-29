from django.http import HttpResponse
from django.views.generic.edit import FormView

from .forms import MyContextForm


class Calculate(FormView):

    template_name = "home.html"
    form_class = MyContextForm
    success_url = '/'

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)

        if form.is_valid():
            form.fields['r1_value'].initial = 3
            context['result'] = form.cleaned_data['input_voltage'] + 1

        context['form'] = form
        return self.render_to_response(context)

