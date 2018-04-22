
import os, time, werkzeug
from flask import Flask, Response, request, current_app
from flask_basicauth import BasicAuth
from flask_restplus import Api
from flask_restplus import Resource
from flask_restplus import reqparse
from services.GenericInfoProvider import GenericInfoProvider
from services.ImageFileSaver import ImageFileSaver


# parametri di autenticazione al servizio di API
# l'autenticazione puo' essere richiesta a compertura
# dell'intero servizio o per singolo end-point
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'generic-user'
app.config['BASIC_AUTH_PASSWORD'] = 'p4ssw0rd'
app.config['BASIC_AUTH_FORCE'] = True
app.config['DEBUG'] = True
app.config['DATA_FOLDER'] = 'data'
basic_auth = BasicAuth(app)

# parametri per Swagger
# para
api = Api(app,
          version='0.1',
          title='Advanced Analytics API',
          description='The collection of APIs capable of performing '\
          'machine learning and artificial intelligent tasks')

# istanzio l'oggetto che contiene tutte le informazioni
# da per da mostrare dentro Swagger e tutti i metodi
# che forniscono le informazioni richieste
gen_info = GenericInfoProvider()
namespace_gen_info = gen_info.get_namespace(api)
parser_gen_info = gen_info.get_generic_parser(api)
# esempio di end point
@namespace_gen_info.route('/')
class Car(Resource):
    @api.doc(parser=parser_gen_info)
    def get(self):
        # calcolo il tempo totale che il servizio
        # impiega ad eseguire la funzione
        # non e' il tempo totale di risposta
        start_time = time.time()
        # parso gli argomenti come definiti nel 'parser'
        # della documentazione di Swagger
        args = parser_gen_info.parse_args()
        # passo al classifier il testo
        response = gen_info.get_generic_info(args['targa'])
        # aggiungo al risulato la classe identificata
        time_e = time.time() - start_time
        response['exc_time'] = time_e
        return response, 200


img_saver = ImageFileSaver()
namespace_img_saver = img_saver.get_namespace(api)
parser_img_saver = img_saver.get_parser(api)
@namespace_img_saver.route('/')
class ImageUpload(Resource):
    @api.doc(parser=parser_img_saver)
    #@api.expect(file_upload)
    def post(self):
        args = parser_img_saver.parse_args()
        print('args', args)
        #print('file type', args['jpeg_file'].mimetype)
        if args['jpeg_file'].mimetype == 'image/jpeg':
            json_response = img_saver.save_image_file_system(current_app.config.get('DATA_FOLDER'),args['jpeg_file'],args['id_img'],args['jpeg_file'])
            return json_response, 200
        else:
            return {'status': 'Error', 'message':'No jpeg image'}, 404

##########################
#
# AVVIO DEL APPLICAZIONE
#
##########################
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0')
