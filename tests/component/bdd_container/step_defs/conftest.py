import pytest
from pytest_bdd import parsers, then, when

from .db_helper import DBHelper
from .http_client import HttpClient


@pytest.fixture(autouse=True, scope="module")
def client():
    return HttpClient


@when(parsers.parse("user makes get request to {end_point} endpoint"))
def get_request(context, client, end_point):
    context['response'] = client.get(end_point)


@when(parsers.parse("user starts extraction process for the date {order_date}"))
def post_request(context, client, order_date):
    context['response'] = client.post("/extract")


@then(parsers.parse("the request should be completed with status code {response_code:d}"))
def check_status_code(context, response_code):
    assert context['response'].status_code == response_code


@then(parsers.parse("the response should have following properties: {properties}"))
def verify_properties_in_res(context, properties):
    res = context['response'].json()
    for _p in properties.split(","):
        assert _p in res.keys()


@then(parsers.parse("in the response, {key} should be {val}"))
def assert_property_values(context, key, val):
    res = context['response'].json()
    assert str(res[key]) == val


@then(parsers.parse("the data should be available in the DB for the date {order_date} and count should be {count}"))
def validate_output_against_db(context, order_date, count):
    assert DBHelper.get_table_records_count(order_date) == int(count)


@pytest.fixture
def context():
    return {}
