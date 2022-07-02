from selene.support.shared import browser
from selene import be, have


def test_google_should_find_selene(change_size_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_should_find_nothing(change_size_browser):
    browser.element('[name="q"]').should(be.blank).type('qwertyuiopljhgfdx bnmloiuyg').press_enter()
    browser.element('[class="card-section"] p').should(have.text('По запросу qwertyuiopljhgfdx bnmloiuyg ничего не найдено.'))
    ##browser.element('[class="card-section"] ul li:nth-child(1)').should(have.text('Убедитесь, что все слова написаны без ошибок.'))
