Feature: Tests on description page

  Scenario: Description page and move to booking page

    Given user visits description page
    Then user can see "Rent & Availability" title
    And user can see pricing information and availability
    When user selects availability "Short let"
    And user clicks on Book now button
    Then user is on booking page
    And the property details are accurate
    And short let is preselected as a radio button
    And user closes down browser