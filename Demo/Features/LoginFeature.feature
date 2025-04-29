@AUTORETRY_1
Feature: Saucedemo application scenarios

  Background: Logging to application
    Given User logged into Saucedemo application

@SORT_ITEM
  Scenario: Verify sorting order Z-A on All Items page
   When User sort products by name from Z to A
    Then User should see the items sorted in descending order

@SORT_PRICE
  Scenario: Verify price order high to low on All Items page
    When User sort products by price from high to low
    Then User should see the items sorted by descending price

  @CHECKOUT
  Scenario: Complete checkout with multiple items
    When User add multiple items to the cart and checkout
    Then User should complete the purchase successfully

@SCREENSHOT
  Scenario: Visual regression on All Items page
    Then User should capture a visual snapshot of the inventory page

