from pytest_bdd import scenarios, given, when, then, parsers
import pytest
import json
pytestmark = pytest.mark.api
scenarios('../features/todo_api.feature')

@when("zavolám GET na /api/todos")
def call_get(client):
    client.response = client.get("/api/todos")

@then("odpověď obsahuje prázdný seznam")
def check_empty_list(client):
    assert client.response.json == []

@when(parsers.parse('pošlu POST na /api/todos s úkolem "{task}"'))
def post_task(client, task):
    client.response = client.post("/api/todos", json={"task": task})

@then("odpověď má status 201")
def status_created(client):
    assert client.response.status_code == 201

@then('odpověď obsahuje stav "created"')
def check_created_status(client):
    assert client.response.json["status"] == "created"

@given('přidám úkol "Uklidit" přes API')
def given_task(client):
    client.post("/api/todos", json={"task": "Uklidit"})

@when("pošlu PUT na /api/todos/0")
def mark_done(client):
    client.response = client.put("/api/todos/0")

@then('odpověď obsahuje stav "updated"')
def check_updated(client):
    assert client.response.json["status"] == "updated"
