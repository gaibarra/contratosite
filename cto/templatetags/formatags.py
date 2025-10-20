import datetime
from django import template
from django.template import Context, loader

from cto.models import Partes, Departamento, Contratos, Doctos

from django.contrib.auth.models import User

register = template.Library()


def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
        )
    return CurrentTimeNode(format_string[1:-1])



class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string

    def render(self, context):
        return datetime.datetime.now().strftime(self.format_string)


def view_1(request):
    # ...
    t = loader.get_template('cto/contratos.html')
    c = Context({
        'app': 'cto',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
        'message': 'I am view 1.'
    })
    #print (c)
    return t.render(c)




@register.simple_tag
def cuenta_archivos():
    a = Doctos.objects.filter().count()
    return a
    


