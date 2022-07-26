Feature: Price Filter Slider
#
#  Scenario: Price Filter Slider handle position resents
#    Given Open GetTop page
#    When Click on IPHONE button
#    And Slide Left Filter Button
#    And Slide Right Filter Button
#    And Click on Filter Button
#    And Click on closing X from Active filters Min
#    And Click on closing X from Active filters Max
#    Then Verify that Price Filter Slider handle position resents

    Scenario: Price Filter Slider handle position resents Mobile Version
      Given Open GetTop page
      When Click on Menu Button
      And Click on IPHONE btn
      And Click on Filter
      And Slide Left Filter
      And Slide Right Filter
      And Click on Filter Btn
      And Click on X from Active filters Min
      And Click on X from Active filters Max
      Then Verify that Mobile Price Filter Slider handle position resents
