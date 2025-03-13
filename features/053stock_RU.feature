Feature:
We test the read and update of stock operations after the installation of a module.

Scenario:   Read a test stock location
    Given I am logged in as a user
    And I have successfully created a test stock location
    When I read a test stock location
    Then If the stock location can't be read, the module can't be installed

Scenario:   Update data from the stock location
    Given I am logged in as a user
    And I have successfully created a test stock location
    When I update a test stock location
    Then If the stock location can't be updated, the module can't be installed

Scenario:   Read a test stock location product qty
    Given I am logged in as a user
    And I have successfully created a test stock location
    And I have successfully created a test product
    When I read the quantity of a product in a test stock location
    Then If the qty can't be read, the module can't be installed

Scenario:   Update qty of the product from the stock location
    Given I am logged in as a user
    And I have successfully created a test stock location
    And I have successfully created a test product
    When I update the quantity of a product in a test stock location
    Then If the qty can't be updated, the module can't be installed

Scenario:   Read a test stock transfer
    Given I am logged in as a user
    And I have successfully created a test stock transfer
    When I read a test stock transfer
    Then If the stock transfer can't be read, the module can't be installed

Scenario:   Update data from the stock transfer
    Given I am logged in as a user
    And I have successfully created a test stock transfer
    When I update a test stock transfer
    Then If the stock transfer can't be updated, the module can't be installed