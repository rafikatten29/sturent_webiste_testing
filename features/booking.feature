Feature: Tests on booking page


  Background:

    Given user is on booking page

  Scenario Outline: User enters valid data

    #Given user selects "<availability>" radio button
    And user chooses "<move_in_date>" as move in date
    And user chooses "<move_out_date>" as move out date
    And user chooses "<title>" as title
    And user enters "<first_name>" as first name
    And user enters "<last_name>" as last name
    And user enters "<email>" as email
    And user enters "<phone_num>" as phone number
    And user chooses "<nationality>" as nationality
    And user chooses "<country>" as country
    And user enters "<property_num>" as property number
    And user enters "<street>" as street
    And user enters "<city>" as city
    And user enters "<postcode>" as postcode
    Then user closes down browser

    Examples:
    | availability | move_in_date | move_out_date | title | first_name | last_name | email | phone_num | nationality | country | property_num | street | city | postcode |
    | short let | 08-01-2022 | 08-05-2022 | Mr | Peter | Pan | p@p.com | 12345678901 | British | United Kingdom | 50 | Tenter | London | N6 4AS |
    | short let | 08-10-2022 | 08-15-2022 | Mrs | Petra | Pie | p@p.com | 12345678901 | Austrian | Austria | 67 | Gall | Vienna | 123456 |