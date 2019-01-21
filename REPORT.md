## Anwendungsentwicklung - Verwendung von APIs

#### Implementieren Sie eine REST-Schnittstelle mit Flask um eine einfache TODO-Liste abzubilden und diese über einen Vue.js Client anzuzeigen und bearbeiten zu können.

#### Definieren Sie einen Test-Endpunkt auf localhost mit der Port Nummer 8080. Was müssen Sie dafür beim Flask-Server konfigurieren?
- In app.run() port=8080 hinzufügen.
```python
app.run(port=8080)
```
#### Implementieren Sie eine TODO-Liste mit Flask mit folgenden Elementen: {id, todo, assignee, done}. Was haben Sie geändert oder welche Elemente haben Sie neu definiert?
- Alle Elemente die Books waren in Todo umgewandelt, Die Daten im Dictionary geändert, preis entfernt, Alle Methodennamen mit "books", auf "todo" geändert.
```python
def all_todos():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TODO.append({
            'id': uuid.uuid4().hex,
            'todo': post_data.get('todo'),
            'assignee': post_data.get('assignee'),
            'done': post_data.get('done')
        })
        response_object['message'] = 'Todo added!'
```
#### Bereiten Sie die grafische Oberfläche für eine einfache Erstellung, Anzeige, Löschung und Anpassung der TODOs vor. Welche Komponenten müssen dafür erstellt werden?
- In Books.vue Books auf Todo geändert und den preis entfernt, Funktionsnamen ebenfalls geändert, Daten auf todo, assignee und done geändert. 
```vue
<table class="table table-hover">
    <thead>
        <tr>
            <th scope="col">Title</th>
            <th scope="col">Author</th>
            <th scope="col">Read?</th>
            <th scope="col">Purchase Price</th>
            <th></th>
         </tr>
     </thead>
     <tbody>
        <tr v-for="(todo, index) in todos" :key="index">
            <td>{{ todo.title }}</td>
            <td>{{ todo.author }}</td>
            <td>
              <span v-if="todo.read">Yes</span>
              <span v-else>No</span>
            </td>
            <td>${{ todo.price }}</td>
            <td>
              <button type="button"
                    class="btn btn-warning btn-sm"
                    v-b-modal.todo-update-modal
                    @click="edittodo(todo)">
                Update
              </button>
              <button type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeletetodo(todo)">
                Delete
              </button>
              <router-link :to="`/order/${todo.id}`"
                        class="btn btn-primary btn-sm">
                Purchase
              </router-link>
            </td>
          </tr>
      </tbody>
</table>
```
#### Ermöglichen Sie die einfache Erweiterung der grafischen Oberfläche und beschreiben Sie notwendige Schritte um neue Komponenten zur Anmeldung oder persönlichen Definition von personenbezogenen TODOs zu ermöglichen.
- Möglich durch neues .vue File. index.js braucht weitere route
#### Wie würden Sie eine einfache Authentifizierung implementieren? Beschreiben Sie die notwendigen Schritte!
- Datenbankzugriff nur mittels Username & Passwort

## Anwendungsentwicklung - Anforderungsmanagement und SW-Design

#### Passen Sie das bereitgestellte Beispiel (flask-vue-crud) soweit an, dass eine Verwendung der bestehenden API durch einen eigenen Python-Client ermöglicht wird. Veränderungen der definierten Schnittstelle sind so weit wie möglich zu vermeiden.

#### Implementieren Sie einen Client in Python, der sich mit der vorhandenen Server-Einheit verbindet und die Daten in eine eigene JSON Struktur lädt.
- Neues Python-File erstellt, import von request und json, verbinden mit dem Server mittels response = request.get(url), response.json um Daten als json zu bekommen
```python
import requests
import json

url = "http://127.0.0.0:8080/todo"
response = requests.get(url)
asJson = response.json
```
#### Was würden Sie bei der Server-API anders definieren, damit verschiedene Clients auf die angebotenenen Funktionen zugreifen könnten?
- Verwendung von CORS (Cross-Origin RequestS(Eine Anfrage auf eine Ressource ausserhalb des Ursprungs.)). Aktivierung von CORS verläuft folgendermaßen (App.py):
```py
# enable CORS 
CORS(app)
```

## Softwareentwicklungsprozess - Verifikation und kontinuierliche Entwicklung

#### Schreiben Sie zu den funktionalen Anforderungen des bereitgestellten Beispiels (flask-vue-spa) entsprechende Testfälle um deren korrekte Implementierung überprüfen zu können.

#### Welche Tools würden Sie einsetzen, und wie würden die entsprechenden Konfigurationsdateien aussehen? Erstellen Sie ein Konzept!
- Tox, pytest, Cypress, TravisCI, lokale Ausführung der pytests mittels Tox, automatische Ausführung von testcases bei jedem push mittels travisCI, Testen der graphischen Oberfläche mittels Cypress. 
```
npm install cypress. 
```
starten mit
```
npx cypress open
```
Pytests in eigener Klasse definieren. Tox.ini aktualisieren: 
```ini
[pytest]
testpaths = tesing/pytest
python_files = test_*.py
python_classes = Test
```
push auf TravisCI
#### Bereiten Sie einen einfachen Test für den Aufruf der Random Funktion vor. Wie würden Sie diesen starten?
- Test für Random Funktion. testRnd.py. Vergleichen ob Statuscode = 200. Wenn dem so ist -> Keine Fehler.
```python
import pytest
from run import app

@pytest.fixture
def client(req):
test_cl = app.test_cl()
return test_cl

def testRand(client):
res = client.get('/api/random')
assert res.status_code = 200
```
Ausfürhung entweder mittels tox oder pytest (pytest testRnd.py)
#### Implementieren Sie einen einfachen grafischen Test. Worauf achten Sie dabei?
- In cypress/integration erstellen wir ein neues Directory namens frontend
```js
describe('Homepage', function() {
    it('Open Homepage', function() {
        cy.visit('http://localhost:8080/')
        cy.get('button').click()
    })
})
```
#### Definieren Sie eine Konfiguration mit TravisCI für eine kontinuierliche Integration. Was müssen Sie dabei für die Python Tests und was für die grafischen Tests vorsehen?
- .travis.yml file createn
```yml
python: 3.7
node_js: 10
```
- Teil für Tox:
```yml
jobs:
  include:
    - stage: Tox Test
      name: "Unit Tests"
      language: python
      python: 3.7
      script: tox
```

- Teil für Cypress:
```yml
    - stage: Cypress Test
      name: "Frontend Testing Cypress"
      language: node_js
      node_js: 10
      npm: true
      directories:
        - /.npm
        - /.cache
        - node_modules
      install:
        - cd src/router
        - npm ci
      script: npm run cy:run
```
#### Welche Tests würden Sie für die Grenzen der Random Funktion vorsehen?
- Einfaches Überprüfen von OG und UG mittels pytest
