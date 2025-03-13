Feature:
We test the read and update of a Partner module after the installation of a module.

Scenario:   Read a test partner
    Given I am logged in as a user
    And I have successfully created a test partner
    When I read a test partner
    Then If the partner can't be read, the module can't be installed

Scenario:   Update a test partner
    Given I am logged in as a user
    And I have successfully created a test partner
    When I update a test partner
    Then If the partner can't be updated, the module can't be installed
