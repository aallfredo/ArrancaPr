from pyramid.renderers import get_renderer
from pyramid.view import view_config


def site_layout():
    renderer = get_renderer("templates/global_layout.pt")
    layout = renderer.implementation().macros['layout']
    return layout

@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):
    return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='about', renderer='templates/about.pt')
def about_view(request):
    return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='contact', renderer='templates/contact.pt')
def contact_view(request):
    return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='project', renderer='templates/project.pt')
def project_view(request):
    return {'project': 'ArrancaPr', "layout": site_layout()}
