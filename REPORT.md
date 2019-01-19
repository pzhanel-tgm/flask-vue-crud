Anwendungsentwicklung - Verwendung von APIs

- app.run(port=8080), In app.run() port=8080 hinzufügen.
- Alle Elemente die Books waren in Todo umgewandelt, Die Daten im Dictionary geändert, preis entfernt
- In Books.vue Books auf Todo geändert und den preis entfernt, Funktionsnamen ebenfalls geändert, Daten auf todo, assignee und done geändert. 
- 
-

Anwendungsentwicklung - Anforderungsmanagement und SW-Design

- Neues Python-File erstellt, ...
-

Softwareentwicklungsprozess - Verifikation und kontinuierliche Entwicklung

- Tox, pytest, Cypress, TravisCI, lokale Ausführung der pytests mittels Tox, automatische Ausführung von testcases bei jedem push mittels travisCI, Testen der graphischen Oberfläche mittels Cypress. npm install cypress. 
starten mit cypress open
Pytests in eigener Klasse definieren. Tox.ini aktualisieren: testpaths = tesing/pytest; python_files = test_*.py; python_classes = Test''
push auf TravisCI
- Test für Random Funktion. testRnd.py. Vergleichen ob Statuscode = 200. -> Keine Fehler.
import pytest; from run import app; @pytest.fixture; def client(req):
test_cl = app.test_cl(); return test_cl;
def testRand(client):
res = client.get('/api/random');
assert res.status_code = 200
Ausführung entweder mittels tox oder pytest (pytest testRnd.py)
- 
- .travis.yml file createn
- Einfaches Überprüfen von OG und UG mittels pytest