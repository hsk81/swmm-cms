from property.models import *

class PropertyController:

    def value (request, name):

        return {
            name.replace ('-','_'): Property.value (name)
        }

    value = staticmethod (value)

    def values (request):

        return dict (
            map (
                lambda p: (
                    p.name.replace ('-','_'), Property.value (p.name)
                ), Property.objects.all()
            )
        )

    values = staticmethod (values)
    