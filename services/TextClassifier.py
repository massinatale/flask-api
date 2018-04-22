import os
from sklearn.externals import joblib

class TextClassifier(object):

    def __init__(self):
        print ("init Text classifier service") # never prints
        self.clf = ''
        self.vectorizer = ''

    def get_namespace(self, api):
        return api.namespace('Text classifier',
                           description='Text classifier assigns categories '\
                           'to documents ',
                           path='/textclassifier')

    def get_parser(self, api):
        parser = api.parser()
        parser.add_argument('text',
                            type=str,
                            required=True,
                            help='Text to analyze',
                            location='args')
        return parser

    def start_service(self):
        # da cambiare con il comando di localizzazione della cartella dove
        # sta girando il servizio
        print(os.path.expanduser('~'))
        dir_path = os.path.join(os.path.expanduser('~'), '/model/', clf_name)
        model_path = os.path.join(dir_path, 'model')
        self.clf = joblib.load(model_path)

        vectorizer_path = os.path.join(dir_path, 'vectorizer')
        self.vectorizer = joblib.load(vectorizer_path)
        # da cambiare con sintassi migliore
        return {'message': 'IntentClfService for %s is up and running' % (clf_name),
                'service_status': 'running'}

    def get_class(self, text):
        print(text)
        #example_counts = self.vectorizer.transform(sentence).todense()
        #predictions = self.clf.predict(example_counts)
        #print(predictions)  # [1, 0]

        '''
        response = {'sentence': request['sentence'],
                    'intent': predictions[0],
                    'exc_time': time.time() - start_time}
        '''
        #print(response)
        return 'cioa anche a te'
