from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Test, Category, Page
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime

# Create your views here.
@login_required
def index(request):
    # request.session.set_test_cookie()
    category_list = Category.objects.order_by('-likes')[:5]
    page_likes_list = Page.objects.order_by('-views')[:5]
    page_send = {'categories' : category_list, 'views':page_likes_list}



    # visits_func(request,response)
    visits_func_session(request)
    print(request.COOKIES.get('visits'))
    page_send['visits'] = request.session['visits']
    response = render(request, 'rango/index.html', page_send)
    return response

@login_required
def category(request, category_name_slug):
    context_dic ={}
    try:
        category = Category.objects.get(name=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dic['pages'] = pages
        context_dic['category'] = category
        context_dic['test'] = category_name_slug
    except Category.DoesNotExist:
        context_dic['pages'] = None
        context_dic['category'] = None
    return render(request, 'rango/category.html', context_dic)

def number(request,pk,pq):
    return HttpResponse(pk+pq)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

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
            form.save(commit = True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form' : form})

@login_required
def add_page(request,category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None



    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit = False)
            page.category = category
            page.save()
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add_page.html', {'form': form ,
                                                   'method':request,
                                                   'cns':category_name_slug,
                                                   'category' : category,
                                                   })

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else: print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'rango/registration.html',
                  {'user_form': user_form,
                   'profile_form' : profile_form,
                   'registered': registered})

def user_login(request):
    if request.method == 'POST':
        print(request.method +'yada yada')

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is inactive you loser!")

        else:
            return HttpResponse('invalid details {0}{1}'.format(username,password))

    else:
        print(request.method +'yada yada')
        return render(request,'rango/login.html',{})

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def restricted(request):
    return HttpResponse('please clap and login')


'''HELPER FUNCTIONS'''
def visits_func(request,response):
    visits = int(request.COOKIES.get('visits','0'))
    last_visits_cookie = request.COOKIES.get('last_visit',str(datetime.now())[:-7])

    last_visits = datetime.strptime(last_visits_cookie , '%Y-%m-%d %H:%M:%S')
    visits += 1

    if (datetime.now() - last_visits).days>0:

        last_visits = str(datetime.now())
        response.set_cookie('last_visit',str(datetime.now()))
    else:
        response.set_cookie('last_visit', last_visits_cookie)

    response.set_cookie('visits',int(visits))

def get_server_side_cookie(request,cookie,default=None):
    val = int(request.session.get(cookie))
    print(val,'this is val')
    if not val:
        return default
    else:
        return val



def visits_func_session(request):
    visits = int(get_server_side_cookie(request,'visits',0))
    last_visits_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now())[:-7])
    last_visits = datetime.strptime(last_visits_cookie , '%Y-%m-%d %H:%M:%S')
    visits += 1

    if (datetime.now() - last_visits).days>0:

        last_visits = str(datetime.now())
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visits_cookie

    request.session['visits'] = int(visits)











def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request,'visits','1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0 :
        print(visits)
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        visits=1
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits