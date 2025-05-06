import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--environment", action="store", default="QA", help="environment selection"
    )
# def pytest_addoption2(parser):
#     parser.addoption(
#         "--environment", action="store", default="QA", help="Environment selection"
#     )

@pytest.fixture(scope="function")
def browserinstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(45)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)
        driver.implicitly_wait(45)
    yield driver
@pytest.fixture(scope="function")
def Environment_selection(request):
    global URL
    environment = request.config.getoption("environment")
    yield environment
