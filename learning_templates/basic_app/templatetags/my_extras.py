from django import template

register = template.Library()

@register.filter(name ='cut')
def cut(value,arg):
    '''
    This function cuts the arg part from the value passed and replace with space
    '''
    return value.replace(arg,'')

# register.filter('cut', cut)
