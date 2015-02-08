# coding=utf-8
from pyramid.renderers import get_renderer
from pyramid.view import view_config


def site_layout():
    renderer = get_renderer("templates/global_layout.pt")
    layout = renderer.implementation().macros['layout']
    return layout

@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):
    if "name" in request.params:
        personName = request.params["name"]
        personEmail = request.params["email"]
        post = {"name":personName,
                "email":personEmail}

        request.db['MemberRegistration'].insert(post,safe=True)
    return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='about', renderer='templates/about.pt')
def about_view(request):

    return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='contact', renderer='templates/contact.pt')
def contact_view(request):
    if "name" in request.params:
        personName = request.params["name"]
        personEmail = request.params["email"]
        telephone = request.params["tel"]
        body = request.params["body"]
        post = {"name":personName,
                "email":personEmail,
                "telephone":telephone,
                "body":body}
        request.db['CustomerComments'].insert(post,safe=True)
    return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='project', renderer='templates/project.pt')
def project_view(request):
     if "name" in request.params:
        personName = request.params["name"]
        personEmail = request.params["email"]
        project = request.params["project"]
        post = {"name":personName,
                "email":personEmail,
                "project":project}
        request.db['ClassRegistration'].insert(post,safe=True)
     return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='hackerspace', renderer='templates/hackerspace.pt')
def hackerspace_view(request):

    return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='media', renderer='templates/media.pt')
def media_view(request):

    return {'project': 'ArrancaPr', "layout": site_layout()}