from django.shortcuts import render
from .models import Link
from .forms import LinkModelForm

def home_view(request):
    no_of_discounted_items = 0
    error = None
    form = LinkModelForm(request.POST or None)
    if request.method == "POST":
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Couldn't get the name or the price!"
        except:
            error = 'Something went wrong!'

    form = LinkModelForm(request)
    qs = Link.objects.all()
    no_of_items = qs.count()

    if no_of_items > 0:
        discounted_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discounted_list.append(item)
            no_of_discounted_items = len(discounted_list)

    context = {
        'form': form,
        'qs': qs,
        'no_of_items': no_of_items,
        'no_of_discounted_items': no_of_discounted_items,
        'error': error
    }
    return render(request, 'links/home.html', context=context)