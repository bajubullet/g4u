from django.views.generic.edit import FormView

from accounts.forms import SignupForm


class SignupView(FormView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = '/'

    def form_valid(self, form, *args, **kwargs):
        import pdb
        pdb.set_trace()
        data = form.cleaned_data
        print data
        return super(SignupView, self).form_valid()