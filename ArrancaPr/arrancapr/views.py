# coding=utf-8
from pyramid.renderers import get_renderer
from pyramid.view import view_config
from datetime import datetime

def site_layout():
    renderer = get_renderer("templates/global_layout.pt")
    layout = renderer.implementation().macros['layout']
    return layout

@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):
    showMessage = False
    if "name" in request.params:
        personName = request.params["name"]
        personEmail = request.params["email"]
        ctype = request.params["optradio"]
        post = {"name":personName,
                "email":personEmail,
                "participation_type":ctype,
                "date": datetime.now()}
        request.db['MemberRegistration'].insert(post)
        showMessage = True
    return {'project': 'ArrancaPr', "layout": site_layout(), "msg": showMessage}

@view_config(route_name='about', renderer='templates/about.pt')
def about_view(request):
  showMessage = False
  if "name" in request.params:
        personName = request.params["name"]
        personEmail = request.params["email"]
        telephone = request.params["tel"]
        body = request.params["body"]
        post = {"name":personName,
                "email":personEmail,
                "telephone":telephone,
                "body":body}
        request.db['CustomerComments'].insert(post)
        showMessage = True
  return {'project': 'ArrancaPr', "layout": site_layout(), "msg": showMessage}

@view_config(route_name='calendar', renderer='templates/calendar.pt')
def calendar_view(request):
    return {'project': 'ArrancaPr', "layout": site_layout()}
  
@view_config(route_name='project', renderer='templates/project.pt')
def project_view(request):
     return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='hackerspace', renderer='templates/hackerspace.pt')
def hackerspace_view(request):

    return {'project': 'ArrancaPr', "layout": site_layout()}

@view_config(route_name='media', renderer='templates/media.pt')
def media_view(request):

    return {'project': 'ArrancaPr', "layout": site_layout()}


@view_config(route_name='classes', renderer='templates/classes.pt')
def classes_view(request):
    showMessage = False
    if "name" in request.params:
        personName = request.params["name"]
        personEmail = request.params["email"]
        project = request.params["project"]
        post = {"name":personName,
                "email":personEmail,
                "project":project}
        request.db['ClassRegistration2016'].insert(post)
        showMessage = True
    liveClasses = []
    for classes in request.db['Classes'].find({"obsolete":"false"}):
        liveClasses.append(classes)
    return {'project': 'ArrancaPr', "layout": site_layout(), "collection":liveClasses, "msg": showMessage}


@view_config(route_name='workshops', renderer='templates/workshops.pt')
def workshops_view(request):
    showMessage = False
    if "name" in request.params:
        personName = request.params["name"]
        personEmail = request.params["email"]
        project = request.params["project"]
        post = {"name":personName,
                "email":personEmail,
                "project":project}
        request.db['ClassRegistration2016'].insert(post)
        showMessage = True

    liveWorkshops = []
    for w in request.db['Workshops'].find({"obsolete":"false"}):
        liveWorkshops.append(w)
    return {'project': 'ArrancaPr', "layout": site_layout(), "collection":liveWorkshops, "msg": showMessage}