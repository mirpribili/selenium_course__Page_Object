
import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
'''

def pytest_addoption(parser):
	parser.addoption('--browser_name',
					 action='store',
					 default='chrome',
					 help='Choose browser: chrome or firefox')
	parser.addoption('--language',
					 action='store',
					 default=None,
					 help='Choose language: en, fr')


@pytest.fixture(scope="function")
def browser(request):
	browser_name = request.config.getoption('browser_name')
	user_language = request.config.getoption('language')
	if browser_name == 'chrome':
		options = Options()
		options.add_experimental_option('prefs',
										{'intl.accept_languages': user_language})
		print("\n\nStart chrome browser for test...")
		browser = webdriver.Chrome(options=options)
	elif browser_name == "firefox":
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_language)
		print("\n\nStart firefox browser for test...")
		browser = webdriver.Firefox(firefox_profile=fp)
	else:
		print("Browser <browser_name> still is not implemented")
	yield browser
	print("\nQuit browser...")
	browser.quit()
'''
# Conftest.py - конфигурация тестов - https://stepik.org/lesson/237240/step/4?unit=209628
# https://stepik.org/lesson/237240/step/6?unit=209628
# https://stepik.org/lesson/237240/step/9?unit=209628
# Конкретно этот создан по новому - https://stepik.org/lesson/199980/step/6?unit=174035

def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store', default="Chrome",
					 help="Выберите браузер: Chrome или Firefox")
	parser.addoption('--language', action='store', default="en",
					 help="Выберите язык: ru, en or fr")


@pytest.fixture(scope="function")
def browser(request):
	browser_name = request.config.getoption("browser_name")
	user_language = request.config.getoption("language")
	browser = None
	if browser_name == "Chrome":
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		print("\nЗапуск браузера Chrome для теста..")
		browser = webdriver.Chrome(options=options)
	elif browser_name == "Firefox":
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_language)
		print("\nЗапуск браузера Firefox для теста..")
		browser = webdriver.Firefox(firefox_profile=fp)
	else:
		raise pytest.UsageError("--browser_name должно быть Chrome или Firefox")
	yield browser
	print("\nЗакрытие браузера..")
	browser.quit()
