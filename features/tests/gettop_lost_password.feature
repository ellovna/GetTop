Feature: User is able to reset a password

  Scenario: GetTop lost password reset
    Given Open GetTop page
    When Click the user icon
    And Click Lost your password link
    And User input a@random.com
    And Click Reset Password button
    Then Verify 'Invalid username or email.' text is present



