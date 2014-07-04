Feature: Check Gap report

Background:
       Given I am logged in to perceptyx 
       And I click on the "Gap Report" link 
       Then I am on the "Gap Report" page


Scenario: I can check gap report
          Given there is both "Questions" and "Categories" tab in top left corner
          And there is both "No Comparison" and "Compared to 2011 Trend" tab in top right corner
          When I am on the "Questions" tab
          Then the Evaluation Score for question 2 is "3.37"
          And the Importance Score for question 2 is "3.85"
          And the Gap Score for question 2 is "0.48"
          And the Weighted Gap Score for question 2 is "9.24"
          And the Evaluation Score for question 10 is "3.63"
          And the Importance Score for question 10 is "4.00"
          And the Gap Score for question 10 is "0.37"
          And the Weighted Gap Score for question 10 is "7.40"
          When I go into "Categories" tab
          Then the Evaluation score for Clarity of Direction is "3.80"
          And the Importance score for Clarity of Direction is "4.06"
          And the Gap Score for Clarity of Direction is "0.26"
          And the Weighted Gap Score for Clarity of Direction is "5.28"
          And the Evaluation score for My Manager is "3.97"
          And the Importance score for My Manager is "4.39"
          And the Gap Score for My Manager is "0.42"
          And the Weighted Gap Score for My Manager is "9.22" 
          When I go into "Questions" tab
          And I go into "Compared to 2011 Trend" tab
          Then the Evaluation Score for question 6 is "3.65"
          And the Evaluation Trend Score for question 6 is "+0.06"
          And the Importance Score for question 6 is "3.62"
          And the Importance Trend Score for question 6 is "-0.10"
          And the Gap Score for question 6 is "-0.03"
          And the Gap Trend Score for question 6 is "-0.16"
          And the Weighted Gap Score for question 6 is "-0.54"
          And the Weighted Gap Trend Score for question 6 is "-2.96"
          When I go into "Categories" tab
          Then the Evaluation Score for question 4 is "3.66"
          And the Evaluation Trend Score for question 4 is "+0.19"
          And the Importance Score for question 4 is "4.49"
          And the Importance Trend Score for question 4 is  "+0.03"
          And the Gap Score for question 4 is "0.83"
          And the Gap Trend Score for question 4 is "-0.16"
          And the Weighted Gap Score for question 4 is "18.63"
          And the Weighted Gap Trend Score for question 4 is "-3.45"
          Now I go to "Logout"

Scenario: I can check gap report for China
          And I click on the "Filter Data" link


