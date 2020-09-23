Feature: Login to portal

  Background:
    Given Login page is opened

  Scenario: Invalid login
    When I enter invalid login and password and click login button
    Then A popup should appears

  Scenario: Valid login
    When I enter valid login and password and click login button
    Then I should be logged into portal

