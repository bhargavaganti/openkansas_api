from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from openkansas_api.resources import RepresentativeHandler, RepresentativeWithPolyHandler

urlpatterns = patterns(
    'openkansas_api.views',
    url(r'^(representative|senator)/(\d+)/([^.]+)?$', 'handle_details', name="openkansas_api_details"),
    url(r'^search/$', 'handle_query', name="openkansas_api_query"),
    url(r'^$', 'handle_index', name='openkansas_api_index'),

)

# various API related patterns
representative_resource = Resource(handler=RepresentativeHandler)
representative_with_poly_resource = Resource(handler=RepresentativeWithPolyHandler)

urlpatterns += patterns('',
    url(
        r'^(?P<type>representative|senator)/(?P<district>\d+)/([^.]+)\.(?P<emitter_format>[a-z]+)$',
        representative_resource,
        name="openkansas_api_details.api"
    ),
    url(
        r'^(?P<type>representative|senator)/(?P<district>\d+)/([^.]+)\.(?P<emitter_format>[a-z]+)/poly$',
        representative_with_poly_resource,
        name="openkansas_api_details.api.poly"
    ),
)

