
Feature: Order Transaction
    Test related to order transactions

    Scenario Outline: Verify order success message shown in details page
        Given place the item order with <username> and <password>
        And the user is on landing page
        When I login to portal with <username> and <password>
        And navigate to orders page
        And select the order Id
        Then order message is successfully displayed
        Examples:
            | username           | password      |
            | rdtest01@gmail.com | PassworD@2025 |