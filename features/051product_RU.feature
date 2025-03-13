Feature:
We test the read and update of a Product after the installation of a module.

Scenario:   Read a test product
    Given I am logged in as a user
    And I have successfully created a test product
    When I read a test product
    Then If the product can't be read, the module can't be installed

Scenario:   Update a test product
    Given I am logged in as a user
    And I have successfully created a test product
    When I update a test product
    Then If the product can't be updated, the module can't be installed
