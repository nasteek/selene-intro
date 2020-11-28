from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s


def test_search_and_link_size_on_result_page():
    # Arrange
    browser.open('https://www.ecosia.org/')

    # Act
    s('[name=q]').type('yashaka selene').press_enter()
    ss('.result').first.click()

    # Assert
    ss('[href="/yashaka/selene"').should(have.size(3))
