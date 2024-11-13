from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from core.models import Person
from django.urls import reverse

def home(request):
    query = request.GET.get('q', '')
    order = request.GET.get('order', 'id')

    if query:
        persons = Person.objects.filter(name__icontains=query).order_by(order)  # (containing)
    else:
        persons = Person.objects.all().order_by(order)

    paginator = Paginator(persons, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "index.html", {'persons': page_obj, 'query': query, 'order': order})

def form(request):
    return render(request, "form.html")

def save(request):
    if request.method == "POST":
        person = Person(
            name=request.POST.get("name")
        )
        person.save()
        return redirect('url_home')
    return render(request, 'form.html')

def update(request, id):
    person = Person.objects.get(id=id)
    query = request.GET.get('q', '')
    page_number = request.GET.get('page', 1)
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.save()

        return redirect(f'/core/?q={query}&page={page_number}')

    return render(request, 'form.html', {'person': person, 'q': query, 'page':page_number })

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()

    query = request.GET.get('q', '')  # Se não houver pesquisa, a string será vazia
    page_number = request.GET.get('page', 1)  # Se não houver página, define a página 1

    # Filtra as pessoas com base no termo de pesquisa
    if query:
        results = Person.objects.filter(name__icontains=query)
    else:
        results = Person.objects.all()

    # Configura a paginação
    paginator = Paginator(results, 5)
    page_obj = paginator.get_page(page_number)

    # Redireciona de volta para a URL de pesquisa com os mesmos parâmetros
    return redirect(f'/core/search/?q={query}&page={page_obj.number}')



'''
def search(request):
    query = request.GET.get('q', '')
    order = request.GET.get('order', 'id')

    if query:
        persons = Person.objects.filter(name__icontains=query).order_by(order)  # (containing)
    else:
        persons = Person.objects.all().order_by(order)

    # Pagination
    paginator = Paginator(persons, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'persons': page_obj, 'query': query, 'order': order})
'''