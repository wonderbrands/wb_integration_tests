Feature:
We test the creation of a stock transfer after the installation of a module.

Scenario:   Create a test stock location
            Given I am logged in as a user
            When I create a test stock location
            Then If the stock location can't be created, the module can't be installed

Scenario:   Add product qty to test stock location
            Given I am logged in as a user
            And I have successfully created a test product
            And I have successfully created a test stock location
            When I add product qty to test stock location
            Then If the product qty can't be added to the stock location, the module can't be installed

Scenario:   Create a test stock transfer
            Given I am logged in as a user
            And I have successfully created a test stock location
            And I have successfully created a test product
            And I have successfully added product qty to test stock location
            And I have successfully created a test partner
            And I have successfully created a test sale order
            When I create a test stock transfer
            Then If the stock transfer can't be created, the module can't be installed