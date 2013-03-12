from django.http import HttpResponse
from django.template import RequestContext, loader
from dramapp.models import UserForm, UserProfileForm, Whisky, Distillery, Rating
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.http import HttpResponseRedirect
=======
from django.http import HttpResponseRedirect, Http404
from dramapp.models import Whisky 
from dramapp.models import Distillery
from dramapp.models import Rating
>>>>>>> html update
from django.db.models import Q
from django.shortcuts import get_object_or_404

<<<<<<< HEAD
=======

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType 
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def thanks(request):
    template = loader.get_template('dramapp/thanks.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
>>>>>>> html update

def index(request):
# select the appropriate template to use
    template = loader.get_template('dramapp/index.html')
    whisky_list = Whisky.objects.all()
    # add the cat_url data to each category
    for whisky in whisky_list:
        whisky_name = whisky.name #+ whisky.age
        whisky.url = encode_whisky(whisky_name)
        # whisky_age = whisky.age
    # Put the data into the context
    #context = RequestContext(request,{ 'whisky_list': whisky_list })
    distillery_list = Distillery.objects.all()
    context = RequestContext(request, {'distillery_list': distillery_list, 'whisky_list': whisky_list})

    # create and define the context. We don't have any context at the moment
    # but later on we will be putting data in the context which the template engine
    # will use when it renders the template into a page.

    # render the template using the provided context and return as http response.
    return HttpResponse(template.render(context))


def base(request):
    template = loader.get_template('dramapp/base.html')
    whisky_data = Whisky.objects.all()
    distillery_data = Distillery.objects.all()
    context = RequestContext(request, {'distillery_data': distillery_data, 'whisky_data': whisky_data})


def distillery(request):
    template = loader.get_template('dramapp/distillery.html')
    distillery_list = Distillery.objects.all()
    for distillery in distillery_list:
        distillery_name = distillery.name
        distillery.url = encode_distillery(distillery_name)
        # Put the data into the context
    context = RequestContext(request, {'distillery_list': distillery_list})
    # render the template using the provided context and return as http response.
    return HttpResponse(template.render(context))


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        uform = UserForm(data=request.POST)
        pform = UserProfileForm(data=request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            # form brings back a plain text string, not an encrypted password
            pw = user.password
            # thus we need to use set password to encrypt the password string
            user.set_password(pw)
            user.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print uform.errors, pform.errors
    else:
        uform = UserForm()
        pform = UserProfileForm()

    return render_to_response('dramapp/register.html', {'uform': uform, 'pform': pform, 'registered': registered},
                              context)


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to index page.
                return HttpResponseRedirect("../")
            else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")

        else:
            # Return an 'invalid login' error message.
            print  "invalid login details " + username + " " + password

    else:
        # the login is a  GET request, so just show the user the login form.
        return render_to_response('dramapp/login.html', {}, context)


@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('../')

    from bing_search import run_query


def search(request):
    context = RequestContext(request)
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            result_list = run_query(query)

    return render_to_response('dramapp/search.html', {'result_list': result_list}, context)


def whisky(request, whisky_name_url):
    template = loader.get_template('dramapp/whisky.html')

    whisky_name = decode_whisky(whisky_name_url)

    context_dict = {'whisky_name_url': whisky_name_url,
                    'whisky_name': whisky_name}
    # Select the Category object given its name.
    # In models, we defined name to be unique,
    # so there so only be one, if one exists.
    whisk = Whisky.objects.get(name=whisky_name)
    context_dict['whisky'] = whisk

    context = RequestContext(request, context_dict)
    return HttpResponse(template.render(context))


def encode_whisky(whisky_name):
    # returns the name converted for insert into url
    return whisky_name.replace(' ', '_')


def decode_whisky(whisky_url):
    # returns the category name given the category url portion
    return whisky_url.replace('_', ' ')


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query) |
            Q(age__icontains=query) |
            Q(barrelType__icontains=query)

        )
        results = Whisky.objects.filter(qset).distinct()
    else:
        results = []

    return render_to_response("dramapp/search.html", {
        "results": results,
        "query": query
    })


def distilleries_list(request, distillery_name_url):
    template = loader.get_template('dramapp/distilleries.html')

    distillery_name = decode_distillery(distillery_name_url)
    context_dict = {'distillery_name_url': distillery_name_url,
                    'distillery_name': distillery_name}
    # Select the Category object given its name.
    # In models, we defined name to be unique,
    # so there so only be one, if one exists.
    dist = Distillery.objects.get(name=distillery_name)
    context_dict['distillery'] = dist

    context = RequestContext(request, context_dict)

    return HttpResponse(template.render(context))


def encode_distillery(distillery_name):
    # returns the name converted for insert into url
    return distillery_name.replace(' ', '_')


def decode_distillery(distillery_url):
    # returns the category name given the category url portion
    return distillery_url.replace('_', ' ')


def rate(request, whisky_id):
    whisky = get_object_or_404(Whisky, pk=whisky_id)
    if 'rating' not in request.GET or request.GET['rating'] not in ('1', '2', '3', '4', '5'):
        return HttpResponseRedirect(whisky.get_absolute_url())

    try:
        rating = Rating.objects.get(user__pk=request.user.id,
                                    whisky__pk=whisky.id)

    except Rating.DoesNotExist:
        rating = Rating(user=request.user, whisky=whisky)
    rating.rating = int(request.GET['rating'])
    rating.save()
    return HttpResponseRedirect(whisky.get_absolute_url())


<<<<<<< HEAD
rate = login_required(rate)
=======

>>>>>>> html update
