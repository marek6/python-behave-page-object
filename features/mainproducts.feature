Feature: Products testing on main page

  Background:
    Given After valid login main products page is opened

  Scenario: Count products number on the page
    Then There are 6 products on main page

  Scenario: Adding product to cart
    When I open products details
    When I add product to cart
    Then Remove button appears, which means product is added to the cart
