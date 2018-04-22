import os, re, werkzeug

class ImageFileSaver(object):

    # costruttore
    def __init__(self):
        print ("init a generic image file saver service") # never prints

    # restutisce le informazioni per Swagger
    def get_namespace(self, api):
        return api.namespace('File Saver',
                           description='descrizione del servizio',
                           path='/saveimg/')


    # restutisce le informazioni per Swagger
    # con gli attributi da passare al metodo
    def get_parser(self, api):
        parser = api.parser()
        parser.add_argument('jpeg_file',
                                 type=werkzeug.datastructures.FileStorage,
                                 location='files',
                                 required=True,
                                 help='JPG file')
        parser.add_argument('id_img',
                                 type=str,
                                 required=True,
                                 help='id_img',
                                 location='args')
        parser.add_argument('img_type',
                                 type=str,
                                 required=True,
                                 help='tio di immagine caricata',
                                 choices=('img_type_01', 'img_type_02', 'img_type_03'),
                                 default='img_type_01',
                                 location='args')
        return parser

    # resituisce le informazioni
    def save_image_file_system(self, data_folder, img_type: str, id_img:str, file_img):
        if file_img.mimetype == 'image/jpeg':
            destination = os.path.join(data_folder, 'jpeg_file\\')
            print('destination: ', destination)
            if not os.path.exists(destination):
                os.makedirs(destination)
            id_file = id_img + '_' + 'v.1.jpg'
            name_file = '%s%s' % (destination, id_file)
            print(name_file)
            print(file_img.save(name_file))
            response = {'status': 'Done',
                             'file_name': name_file}
            return response, 200
        else:
            return {'status': 'Error', 'message':'No jpeg image'}, 404
