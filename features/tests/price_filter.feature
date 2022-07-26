Feature: Price Filter Slider

  Scenario: Price Filter Slider handle position resents
    Given Open GetTop page
    When Click on IPHONE button
    And Slide Left Filter Button
    And Slide Right Filter Button
    And Click on Filter Button
    And Click on closing X from Active filters Min
    And Click on closing X from Active filters Max
    Then Verify that Price Filter Slider handle position resents

