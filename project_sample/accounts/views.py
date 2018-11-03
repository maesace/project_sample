from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

User = get_user_model()


class UserView(LoginRequiredMixin, TemplateView):
    template_name = "user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        return context
