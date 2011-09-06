from property.models import *

class PropertyController:

    def data (request, name):

        return (
            name.replace ('-','_'), Property.data (name)
        )

    data = staticmethod (data)

    def datas (request):

        properties = map(
            lambda pd: pd.property, PropertyData.objects.all()
        )

        return dict (
            map (
                lambda p: (
                    p.name.replace ('-','_'), Property.data (p.name)
                ), properties
            )
        )

    datas = staticmethod (datas)

    def text (request, name):

        return (
            name.replace ('-','_'), Property.text (name)
        )

    text = staticmethod (text)

    def texts (request):

        properties = map(
            lambda pd: pd.property, PropertyText.objects.all()
        )

        return dict (
            map (
                lambda p: (
                    p.name.replace ('-','_'), Property.text (p.name)
                ), properties
            )
        )

    texts = staticmethod (texts)
    