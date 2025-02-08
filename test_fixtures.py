import pytest
from selene import browser, be, have, by


def test_first(setting_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_second(setting_browser):
    browser.open("https://duckduckgo.com/")
    browser.element('[name="q"]').should(be.blank).type('pupalupalupapupa').press_enter()
    browser.element('html').should(have.text('результаты не найдены'))