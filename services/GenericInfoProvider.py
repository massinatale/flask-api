import os, re

class GenericInfoProvider(object):

    # costruttore
    def __init__(self):
        print ("init a generic info provider service") # never prints

    # restutisce le informazioni per Swagger
    def get_namespace(self, api):
        return api.namespace('Informazioni generiche',
                           description='descrizione dei dati',
                           path='/getinfo/')

    # restutisce le informazioni per Swagger
    # con gli attributi da passare al metodo
    def get_generic_parser(self, api):
        parser = api.parser()
        parser.add_argument('attributo_01',
                            type=str,
                            required=True,
                            help='descrizione primo attributo',
                            location='args')
        parser.add_argument('attributo_02',
                            type=str,
                            required=True,
                            help='descrizione secondo attributo',
                            location='args')
        return parser

    # verifica la seguenza dei caratteri alfanumerici
    def get_verify(self, attributo_01: str):
        # if re.match(regex, content) is not None:
        regex = '[A-Z]{2}\d{3}[A-Z]{2}'
        return re.match(regex, attributo_01)

    # resituisce le informazioni
    def get_generic_info(self, attributo_01: str, attributo_02: str):
        attributo_01 = attributo_01.upper()
        response = {}
        # verifico se gli attributi rispettino determinate caratteristiche
        if self.get_verify(attributo_01):
            print('targa',attributo_01)
            dato_01 = ''
            response = {'attributo_01': attributo_01,
                        'attributo_02': attributo_02,
                        'dato_02' : dato_01}
        else:
            response = {'errore': 'l\'attributo_01 deve avere una sequenza di wwdddww'}
        return response
