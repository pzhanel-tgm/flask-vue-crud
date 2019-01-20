## Anwendungsentwicklung - Verwendung von APIs

- In app.run() port=8080 hinzufügen.
```python
app.run(port=8080)
```
- Alle Elemente die Books waren in Todo umgewandelt, Die Daten im Dictionary geändert, preis entfernt, Alle Methodennamen mit "books", auf "todo" geändert.
- In Books.vue Books auf Todo geändert und den preis entfernt, Funktionsnamen ebenfalls geändert, Daten auf todo, assignee und done geändert. 
- Möglich durch neues .vue File. index.js braucht weitere route
- Datenbankzugriff nur mittels Username & Passwort

## Anwendungsentwicklung - Anforderungsmanagement und SW-Design

- Neues Python-File erstellt, import von request und json, verbinden mit dem Server mittels response = request.get(url), response.json um Daten als json zu bekommen
```python
import requests
import json

url = "http://127.0.0.0:8080/todo"
response = requests.get(url)
asJson = response.json
```
- Verwendung von CORS. Aktivierung von CORS verläuft folgendermaßen (App.py):
```py
# enable CORS 
CORS(app)
```

## Softwareentwicklungsprozess - Verifikation und kontinuierliche Entwicklung

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

- In cypress/integration erstellen wir ein neues Directory namens frontend
```js
describe('Homepage', function() {
    it('Open Homepage', function() {
        cy.visit('http://localhost:8080/')
        cy.get('button').click()
    })
})
```
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
- Einfaches Überprüfen von OG und UG mittels pytest
