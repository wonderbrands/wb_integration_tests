Feature:
We test the creation of a Partner module after the installation of a module.


Scenario:   Create a test partner
            Given I am logged in as a user
            When I create a partner
            Then if the partner can't be created, the module can't be installed