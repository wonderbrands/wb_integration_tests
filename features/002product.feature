Feature:
We test the creation of a Product after the installation of a module.


Scenario:   Create a test product
            Given I am logged in as a user
            When I create a test product
            Then If the product can't be created, the module can't be installed