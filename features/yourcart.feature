Feature: Your cart testing

  Scenario: After add product to cart, open cart and verify if product is added correctly
    Given User is logged into portal
    And Product is added to the cart from main products list
    When I open cart
    Then There is added product
    And There is continue shopping button
