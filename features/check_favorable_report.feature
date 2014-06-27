Feature: Check Favorable report

Background:
       Given I am logged in to perceptyx
       And I click on the "Favorability Report" link
       Then I am on the "Favorability Report" page


Scenario: I can check favorable report
          Given there is both a "Questions" and "Categories" tab in top left corner
          And there is a "No Comparison" and "Compared to 2011 Trend" tab in top right corner
          When I am on the "Questions" tab
          Then the Fav score for question 1 is "75.7%"
          And the Neutral score for question 1 is "16.5%"
          And the Unfav score for question 1 is "7.8%"
          And the Overall Average at the bottom has a Fav score of "68.0%"
          And the Overall Average neutral score is "20.6%"
          And the Overall Average Unfav score is "11.5%"
          When I go into the "Categories" tab
          Then the Fav score for Clarity of Direction is "71.0%"
          And the Neutral score for Clarity of Direction is "18.8%"
          And the Unfav score for Clarity of Direction is "10.2%"
          When I go into the "Compared to 2011 Trend" tab
          Then the Trend Fav score for Clarity of Direction is "65.0%"
          And the Trend Neutral score for Clarity of Direction is "20.9%"
          And the Trend Unfav score for Clarity of Direction is "14.1%"


        
