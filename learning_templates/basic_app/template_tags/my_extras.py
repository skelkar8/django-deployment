from django import template

register = template.Library()

# @register.filter(name = 'cut') #you can use decorators inside

def cut(value,arg):
    """
    This cuts out all values of arg from the string!
    """

    return value.replace(arg,'')


register.filter('cut',cut) #Actually register the function. first arg, what you wanna call the function, second arg, the actual function
