Feature:
We test the read and update of a sale after the installation of a module.

Scenario:   Read a test sale
    Given I am logged in as a user
    And I have successfully created a test sale
    When I read a test sale
    Then If the sale can't be read, the module can't be installed

Scenario:   Update data from the test sale
    Given I am logged in as a user
    And I have successfully created a test sale
    When I update a test sale
    Then If the sale can't be updated, the module can't be installed

Scenario:   Confirm a test sale
    Given I am logged in as a user
    And I have successfully created a test sale
    When I confirm a test sale
    Then If the sale can't be confirmed, the module can't be installed

Scenario:   Cancel a test sale
    Given I am logged in as a user
    And I have successfully created a test sale
    When I cancel a test sale
    Then If the sale can't be cancelled, the module can't be installed

Scenario:   Set test sale to draft (quotation)
    Given I am logged in as a user
    And I have successfully created a test sale
    When I set test sale to draft (quotation)
    Then If the sale can't be set to draft (quotation), the module can't be installed

    