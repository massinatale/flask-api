# flask-api
An example of a RESTful API service in Python and Flask


### Setup Git repository
Il codice del progetto e sul repository git di Bitbucket.
Per scaricare in locale il progetto da linea di comando
```console
git clone https://github.com/massinatale/flask-api.git
```

Se è necessario, settare il proxy da linea di comando
```console
git config --global http.proxy http://user:password@server:port
```
Per togliere le configurazioni del proxy
```console
git config --global --unset http.proxy
```


### Setup virtualenv
Il modulo `virtualenv` permette la creazione di un ambiente python isolato, che consente di specificare e versionare i moduli esterni usati dall'applicazione.

Per creare un virtualenv da linea di comando Windows bastano i seguenti passaggi:

```console
> virtualenv env
> \env\Scripts\activate
> pip install -r requirements.txt

> deactivate
```
Attenzione: in alcuni casi potrebbe essere necessario installare i requirements con pip3
```console
> pip3 install -r requirements.txt
```

### Running
Dopo aver creato ed avviato il `virtualenv` è possibile avviare l'applicazione.
Per avviare l'applicazione da linea di comando

```console
> python app.py
```
se l'applicazione si avvia si vedrà un messaggio simile a questo
```console
* Restarting with stat
* Debugger is active!
* Debugger PIN: 134-830-789
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
a questo punto è possibile aprire il browser su http://localhost:5000 .





Atom document preview `crtl` + `shift` + `m`
