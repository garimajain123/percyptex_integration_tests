Feature: Fill Survey

Background:
       Given I am filling survey

Scenario: I can fill survey
         When I select "Englishgarimajain" as my perfered language
         And I click on the "Proceed" button
         And I am on the "Employee Survey" page
         And I started filling 1st page of the survey
         And I click on the "Next Page" button
         And I fill the 2nd page
         And I click on the "Next Page" button
         And I fill the 3rd page
         And I click on the "Next Page" button
         And I fill the 4th page
         And I click on the "Next Page" button
         And I fill the 5th page
         And I click on the "Submit" button
         Then I should see the "Englishgarimajain" page
         And my total counts in the survey should get updated
        
