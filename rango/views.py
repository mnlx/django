from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Page
from .forms import CategoryForm, PageForm
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_likes_list = Page.objects.order_by('-views')[:5]
    page_send = {'categories': category_list, 'views': page_likes_list}
    visits_func_session(request)
    print(request.COOKIES.get('visits'))
    page_send['visits'] = request.session['visits']
    response = render(request, 'rango/index.html', page_send)
    return response


@login_required
def category(request, category_name_slug):
    context_dic = {}
    try:
        category_obj = Category.objects.get(name=category_name_slug)
        pages = Page.objects.filter(category=category_obj)
        context_dic['pages'] = pages
        context_dic['category_obj'] = category_obj
        context_dic['test'] = category_name_slug
    except Category.DoesNotExist:
        context_dic['pages'] = None
        context_dic['category_obj'] = None
    return render(request, 'rango/category.html', context_dic)


def number(request, pk, pq):
    return HttpResponse(pk+pq)


@login_required
def about(request):
    print(request.method)
    print(request.user)

    return render(request, 'rango/about.html', {})


@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_page(request, category_name_slug):
    try:
        category_obj = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category_obj = None
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.category = category_obj
            page.save()
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add_page.html', {'form': form,
                                                   'method': request,
                                                   'cns': category_name_slug,
                                                   'category_obj': category_obj,
                                                   })


@login_required
def restricted(request):
    return HttpResponse('please clap and login')


@login_required
def like_category(request):
    likes = 'This is empty'
    if request.method == 'GET':
        cat_id = request.GET['category_id']
        likes = 0
        if cat_id:
            cat = Category.objects.get(id=int(cat_id))
            if cat:
                cat.likes += 1
                cat.save()
                likes = cat.likes
    return HttpResponse(likes)


@login_required
def suggest_category(request):
    starts_with = ''

    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    cat_list = get_category_list(8, starts_with)

    return render(request, 'rango/cats.html', {'cats': cat_list})

# START OF HELPER FUNCTIONS


def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)
    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]
    return cat_list


def visits_func(request, response):
    visits = int(request.COOKIES.get('visits', '0'))
    last_visits_cookie = request.COOKIES.get('last_visit', str(datetime.now())[:-7])
    last_visits = datetime.strptime(last_visits_cookie, '%Y-%m-%d %H:%M:%S')
    visits += 1

    if (datetime.now() - last_visits).days > 0:
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        response.set_cookie('last_visit', last_visits_cookie)

    response.set_cookie('visits', int(visits))


def get_server_side_cookie(request, cookie, default=None):
    val = int(request.session.get(cookie))
    print(val, 'this is val')
    if not val:
        return default
    else:
        return val


def visits_func_session(request):
    visits = int(get_server_side_cookie(request, 'visits', 0))
    last_visits_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now())[:-7])
    last_visits = datetime.strptime(last_visits_cookie, '%Y-%m-%d %H:%M:%S')
    visits += 1

    if (datetime.now() - last_visits).days > 0:
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visits_cookie

    request.session['visits'] = int(visits)


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        print(visits)
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

# def get_server_side_cookie(request, cookie, default_val=None):
#     val = request.session.get(cookie)
#     if not val:
#         val = default_val
#     return val
