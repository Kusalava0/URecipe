from logging import exception
from webbrowser import get
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from polls.models import Recipe, Ingredients
from django.contrib.auth import authenticate, login, logout
from .forms import UserImageForm
from .models import Recipe

context = {}


def my_recipe(request):
    if request.user.is_authenticated:
        usr = User.objects.get(username=request.user.username)
        context['heading_card'] = "My Recipes.."
        context['recipes'] = usr.recipes.all()
        return render(request, 'polls/index.html', context)
    else:
        context['heading_card'] = "Recipes you may like.."
        redirect('/home/')


def home(request):
    context = {}
    if request.method == "POST":
        try:
            nme = request.POST.get('search')
            cont = Ingredients.objects.filter(name__iexact=nme)
            context['recipes'] = []
            for val in cont:
                context['recipes'].extend(val.ing_recipe.all())

            context['heading_card'] = "Recipes with ingredient " + nme
        except:
            context['error'] = "Ingredient not found"
            redirect('/home/')
    else:
        context['recipes'] = Recipe.objects.all()
        context['heading_card'] = "Recipes you may like.."

    return render(request, 'polls/index.html', context)


def add(request):
    try:
        ttle = request.POST.get('title')
        desc = request.POST.get('adding')
        vals = dict(request.POST)['ing_val']
        form = UserImageForm(request.POST, request.FILES)
        # if Recipe.objects.get(title=ttle):
        #     raise Exception("Recipe with this title already Exists")

        try:
            if ttle == "" or desc == "" or len(vals) == 0:
                raise Exception("Cannot be empty")

            usr = User.objects.get(username=request.user.username)

            if form.is_valid():
                img = form.cleaned_data.get("image")
                if img:
                    art = Recipe.objects.create(
                        title=ttle, description=desc, user=usr, image=img)
                else:
                    art = Recipe.objects.create(
                        title=ttle, description=desc, user=usr)
                    art.save()
            else:
                art = Recipe.objects.create(
                    title=ttle, description=desc, user=usr)
                art.save()

            for val in vals:
                if val == '':
                    continue
                try:
                    ing = Ingredients.objects.create(name=val)
                    ing.ing_recipe.add(art)
                    ing.save()
                except:
                    ing = Ingredients.objects.get(name=val)
                    ing.ing_recipe.add(art)
                    ing.save()
        except:
            context['error'] = "Item cannot be empty"
    except:
        context['error'] = "Invalid Entry"


def edit(request, id):

    if not request.user.is_authenticated:
        return redirect('/login/')

    try:
        rsp = Recipe.objects.get(title=id)
        if str(rsp) == request.user.username:

            if request.method == "POST":
                ttle = request.POST.get('title')
                desc = request.POST.get('adding')
                vals = dict(request.POST)['ing_val']
                # print(request.POST.get('recipe-image'))
                if ttle == '' or desc == '' or len(vals) == '':
                    raise Exception('Cannot be empty')
                rsp.delete()
                add(request)

            else:
                context['form'] = UserImageForm()
                context['recipe'] = rsp

                return render(request, 'polls/edit.html', context)
    except:
        context['error'] = 'Recipe not found'

    return redirect('/home/')


def add_recipes(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.method == "POST":
        add(request)
        return redirect('/home/')
    else:
        context['form'] = UserImageForm()
        return render(request, 'polls/add.html', context)


def description(request, recipe_title):
    try:
        cont = Recipe.objects.get(title=recipe_title)
        context = {"recipe": cont, "ingredients": cont.ingredient.all()}
        return render(request, 'polls/description.html', context)
    except:
        context = {'error': 'Title not Found'}

    return redirect('/home/')


def register(request):
    if request.method == "POST":
        name = request.POST.get("Profile")
        email = request.POST.get('email')
        psw = request.POST.get('psw')
    try:
        if name == "" or email == "" or psw == "":
            raise Exception("Cannot be Empty")
        usr = User.objects.create_user(name, email, psw)
        usr.save()
        return redirect('/home/')
    except:
        context = {'error': 'Username already found'}
    return render(request, 'polls/register.html', context)


def user_login(request):
    if request.method == 'POST' and not request.user.is_authenticated:
        name = request.POST.get('username')
        psw = request.POST.get('psw')
        try:
            user = authenticate(request, username=name, password=psw)
            login(request, user)
        except:
            context['error'] = 'Invalid Username/Password'

    if not request.user.is_authenticated:
        return render(request, 'polls/login.html', context)
    else:
        return redirect('/home/')


def user_logout(request):
    if request.user.is_authenticated:
        context['message'] = 'Logout successful'
        logout(request)
        return redirect('/home/')
    else:
        context['error'] = "Login to continue"
        return redirect('/login/')
