from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Product, Category, Image, Location, LovedProduct
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from .forms import ProductForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin


class ProductDelete(UserPassesTestMixin, DeleteView):
    model = Product

    def test_func(self):
        return self.request.user.username == str(self.get_object().author)
    success_url = '../../'
    template_name = 'product_confirm_delete.html'


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product

    def test_func(self):
        return self.request.user.username == str(self.get_object().author)
    form_class = ProductForm
    template_name = 'product_update_form.html'
    success_url = '../../'


def search(query):
    return redirect('searchview', query=query)


def categories():
    categories = Category.objects.all()
    proCountbyCategory = []
    for category in categories:
        name = category.category
        number = Product.objects.all().filter(category=category.id).count()
        proCountbyCategory.append({'name': name, 'number': number})

    return proCountbyCategory


def locations():
    locations = Location.objects.all()
    locCountbyloc = []
    for loc in locations:
        name = loc.name
        number = Product.objects.all().filter(location=loc.id).count()
        locCountbyloc.append({'name': name, 'number': number})

    return locCountbyloc


def home(request):
    images = Image.objects.all()
    if request.method == 'POST':
        response = search(request.POST['query'])
        return response
    else:
        cateroylist = categories()
        locationlist = locations()
        products = Product.objects.all()
        return render(request, 'home.html', {
            'products': products,
            'categories': cateroylist,
            'locations':  locationlist,
            'images': images
        })


def signup_view(request):
    redirect_to = request.GET.get('next', '')
    if request.method == 'POST' and not request.user.is_authenticated:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(redirect_to)
        else:
            return render(request, 'signup/index.html', {'redirect_to': redirect_to})
    elif request.user.is_authenticated:
        return redirect('homeview')
    else:
        return render(request, 'signup/index.html', {'redirect_to': redirect_to})


def loginview(request):
    redirect_to = request.GET.get('next', '')
    if request.method == 'POST' and not request.user.is_authenticated:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(redirect_to)
        else:
            return render(request, 'login/index.html', {'redirect_to': redirect_to})
    elif request.user.is_authenticated:
        return redirect('homeview')
    else:
        return render(request, 'login/index.html', {'redirect_to': redirect_to})


def url_generetor(title):
    product_url = title.replace(' ', '-').lower()
    urlfound = Product.objects.all().filter(url=product_url).count()
    temp = product_url
    while urlfound != 0:
        product_url = temp + '-' + str(urlfound)
        newcount = Product.objects.all().filter(url=product_url).count()
        if newcount:
            urlfound += 1
        else:
            urlfound = 0
    return product_url


def addpostview(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        condition = request.POST['condition']
        category = Category.objects.get(id=request.POST['category'])
        location = Location.objects.get(id=request.POST['location'])
        post_category = request.POST['post_category']
        details = request.POST['details']
        phone = request.POST['phone']
        url = url_generetor(name)
        product = Product.objects.create(
            name=name,
            author=request.user,
            price=price,
            condition=condition,
            category=category,
            post_category=post_category,
            location=location,
            phone=phone,
            url=url,
            details=details
        )

        product.save()
        return redirect('uploadview', product.id)
    else:
        form = ProductForm
        return render(request, 'add-post.html', {'form': form})


def logoutview(request):
    logout(request)
    return redirect('homeview')


def sorted_locview(request, location):
    if request.method == 'POST':
        response = search(request.POST['query'])
        return response
    else:
        cateroylist = categories()
        locationlist = locations()
        loc_object = Location.objects.get(name=location)
        products = Product.objects.all().filter(location=loc_object.id)
        return render(request, 'home.html', {
            'products': products,
            'categories': cateroylist,
            'locations': locationlist,
        })


def categoryview(request, category):
    if request.method == 'POST':
        response = search(request.POST['query'])
        return response
    else:
        category_object = Category.objects.get(category=category)
        products = Product.objects.all().filter(category=category_object.id)
        cateroylist = categories()
        locationlist = locations()
        return render(request, 'home.html', {
            'products': products,
            'categories': cateroylist,
            'locations': locationlist,
        })


def productview(request, url):
    isLoved = False
    product = Product.objects.get(url=url)
    if request.user.is_authenticated:
        user_loved = LovedProduct.objects.filter(user=request.user).first()
        print("user found")

        isLoved = False
        if user_loved:
            found_love = LovedProduct.objects.filter(
                user=request.user, Product=product.id).first()

        if found_love:
            isLoved = True
            print("found love")

    context = {
        'product': product,
        'isLoved': isLoved,
    }
    return render(request, 'product.html', context)


def searchview(request, query):
    if request.method == 'POST':
        response = search(request.POST['query'])
        return response

    search_list = query.split()
    products = Product.objects.all().filter(name__contains=query)

    for text in search_list:
        products = products | Product.objects.all().filter(name__contains=text)

    cateroylist = categories()
    return render(request, 'home.html', {
        'products': products,
        'categories': cateroylist})


def uploadview(request, id):
    product_exit = Product.objects.filter(id=id).count()
    if product_exit and Product.objects.get(id=id).author == request.user:
        return render(request, 'upload-image.html', {'id': id, 'product': Product.objects.get(id=id)})
    else:
        return redirect('homeview')


def uploadview2(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        product = Product.objects.get(id=request.POST['id'])
        if product.author == request.user:
            image = Image.objects.create(image=file)
            product.image.add(image)
    return HttpResponse('upload')


def productSaveview(request, id):
    redirect_to = request.GET.get('next', '')
    object = LovedProduct.objects.get(user=request.user.id)
    product = Product.objects.get(id=id)
    object.Product.add(product)
    return redirect(redirect_to)


def unlineview(request, id):
    redirect_to = request.GET.get('next', '')
    object = LovedProduct.objects.get(user=request.user.id)
    product = Product.objects.get(id=id)
    object.Product.remove(product)
    return redirect(redirect_to)


def savedproductview(request, user):
    if request.user.username == user:
        object = LovedProduct.objects.get(user=request.user)
        products = object.Product.all()
        context = {
            'products': products,
            'title': 'My saved products list'
        }
        return render(request, 'filter-products.html', context)
    else:
        raise PermissionDenied


def myproductview(request, user):
    if request.user.username == user:
        products = Product.objects.all().filter(author=request.user)
        context = {
            'products': products,
            'title': 'My products list'
        }
        return render(request, 'filter-products.html', context)
    else:
        raise PermissionDenied
