from pytest_bdd import scenarios, given, when, then, parsers
import pytest
pytestmark = pytest.mark.html
scenarios('../features/todo_html.feature')

@given("aplikace běží")
def app_runs():
    pass

@when("navštívím domovskou stránku")
def visit_homepage(client):
    client.get("/")

@then('uvidím nadpis "My Tasks"')
def check_title(client):
    response = client.get("/")
    assert b"My Tasks" in response.data

@when(parsers.parse('přidám úkol "{task}" přes formulář'))
def add_task_form(client, task):
    client.post("/add", data={"task": task}, follow_redirects=True)

@then(parsers.parse('uvidím úkol "{task}" na stránce'))
def see_task_on_page(client, task):
    response = client.get("/")
    assert task.encode() in response.data
