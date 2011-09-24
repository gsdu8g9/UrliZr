"""
This file is part of UrliZr.

UrliZr is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

UrliZr is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.shortcuts import render_to_response,redirect
from UrliZr.front.models import Urliz
from UrliZr.front.forms import UrlizForm
from django.http import HttpResponseBadRequest

def translate(request, method, url):
  form = UrlizForm({'url': url})
  
  if form.is_valid():
    if Urliz.objects.filter(url__exact=form.cleaned_data['url']).count() == 0:
      u = Urliz(url=form.cleaned_data['url'])
      u.save()
    else:
      u = Urliz.objects.get(url=form.cleaned_data['url'])

    if method == 'raw':
      return redirect('raw', uid=u.uid)

    elif method == 'json':
      return redirect('json', uid=u.uid)

    elif method == 'xml':
      return redirect('xml', uid=u.uid)

    else:    
      return HttpResponseBadRequest

def raw(request, uid):
  return render_to_response('api/raw.tpl', {
    'url': uid,
    'host': request.get_host()
  }, mimetype='text/plain')

def json(request, uid):
  return render_to_response('api/json.tpl', {
    'url': uid,
    'host': request.get_host()
  }, mimetype='text/json')

def xml(request, uid):
  return render_to_response('api/xml.tpl', {
    'url': uid,
    'host': request.get_host()
  }, mimetype='text/xml')
