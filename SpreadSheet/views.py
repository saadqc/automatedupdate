

# Home Page View
from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    template_name = 'spreadsheet_home.html'

    def get(self, request, *args, **kwargs):
        return render(request=request,
                      template_name=self.template_name)
