from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def home_view(request):
    form = FindForm

    return render(request, "scraping/home.html",
                  {'form': FindForm})


def list_view(request):
    form = FindForm
    city = request.GET.get('city')
    language = request.GET.get('language')
    context = {'city': city, 'language': language, 'form': FindForm}

    if city or language:
        _filter = {}

        if city:
            _filter['city__name'] = city
        if language:
            _filter['language__name'] = language

    qs = Vacancy.objects.filter(**_filter)

    paginator = Paginator(qs, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context['object_list'] = page_obj
    return render(request, "scraping/list.html", context)
