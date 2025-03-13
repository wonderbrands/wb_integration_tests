Feature:
We test the creation of a Sale after the installation of a module.


Scenario:   Create a sale order in the form of a quotation
            Given I am logged in as a user
            And I´ve successfully created a test partner
            When I create a test sale order
            