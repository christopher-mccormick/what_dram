from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
       # select the appropriate template to use
        template = loader.get_template('dramapp/index.html')
        # create and define the context. We don't have any context at the moment
        # but later on we will be putting data in the context which the template engine
        # will use when it renders the template into a page.
        context = RequestContext(request, {})
        # render the template using the provided context and return as http response.
        return HttpResponse(template.render(context))