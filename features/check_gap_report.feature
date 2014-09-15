Feature: Check Gap report

Background:
       Given I am logged into perceptyx 
       And I click on "Gap Report" link
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
           Given I go to filter pop-up
           And I applied a filter on Country "China"
           And I submit the filter data
           And the filter count is "71"
           And I am on the "Gap" report page
           And there is both "Questions" and "Categories" tab in top left corner
           And there is both "No Comparison" and "Compared to:" tab in top right corner
           When I am on the "Questions" tab
           And the Evaluation Score for question 3 is "3.92"
           And the Importance Score for question 3 is "4.13"
           And the Gap Score for question 3 is "0.21"
           And the Weighted Gap Score for question 3 is "4.34"
           And the Evaluation Score for question 8 is "4.15"
           And the Importance Score for question 8 is "3.85"
           And the Gap Score for question 8 is "-0.30"
           And the Weighted Gap Score for question 8 is "-5.78"
           When I go into "Categories" tab
           Then the Evaluation Score for values is "4.18"
           And the Importance Score for values is "4.05"
           And the Gap Score for values is "-0.13"
           And the Weighted Gap Score for values is "-2.63"
           And the Evaluation Score for Involvement and Empowerment is "4.02"
           And the Importance Score for Involvement and Empowerment is "4.18"
           And the Gap Score for Involvement and Empowerment is "0.16"
           And the Weighted Gap Score for Involvement and Empowerment is "3.34"
           When I go into "Questions" tab
           And I go into "Compared to" tab
           And I apply compared to as "2011 Trend"
           Then the Evaluation Score for question 6 to compare trend is "4.14"
           And the Evaluation Trend Score for question 6 to compare trend is "+0.51"
           And the Importance Score for question 6 to compare trend is "3.87"
           And the Importance Trend Score for question 6 to compare trend is "+0.26"
           And the Gap Score for question 6 to compare trend is "-0.27"
           And the Gap Trend Score for question 6 to compare trend is "-0.25"
           And the Weighted Gap Score for question 6 to compare trend is "-5.22"
           And the Weighted Gap Trend Score for question 6 to compare trend is "-4.86"
           When I apply compared to as "remainder"
           Then the Evaluation Score for question 6 to compare reminder is "4.14"
           And the Evaluation Trend Score for question 6 to compare reminder is "+0.51"
           And the Importance Score for question 6 to compare reminder is "3.87"
           And the Importance Trend Score for question 6 to compare reminder is "+0.26"
           And the Gap Score for question 6 to compare reminder is "-0.27"
           And the Gap Trend Score for question 6 to compare reminder is "-0.25"
           And the Weighted Gap Score for question 6 to compare reminder is "-5.22"
           And the Weighted Gap Trend Score for question 6 to compare reminder is "-4.86"
           When I apply compared to as "org"
           Then the Evaluation Score for question 6 to compare organization is "4.14"
           And the Evaluation Trend Score for question 6 to compare organization is "+0.49"
           And the Importance Score for question 6 to compare organization is "3.87"
           And the Importance Trend Score for question 6 to compare organization is "+0.25"
           And the Gap Score for question 6 to compare organization is "-0.27"
           And the Gap Trend Score for question 6 to compare organization is "-0.24"
           And the Weighted Gap Score for question 6 to compare organization is "-5.22"
           And the Weighted Gap Trend Score for question 6 to compare organization is "-4.68"
           When I go into "Categories" tab
           And I apply compared to as "2011 Trend"
           Then the Evaluation Score for Work Life Balance to compare trend is "4.11"
           And the Evaluation Trend Score for Work Life Balance to compare trend is "+0.01"
           And the Importance Score for Work Life Balance to compare trend is "4.29"
           And the Importance Trend Score for Work Life Balance to compare trend is "-0.05"
           And the Gap Score for Work Life Balance to compare trend is "0.18"
           And the Gap Trend Score for Work Life Balance to compare trend is "-0.06"
           And the Weighted Gap Score for Work Life Balance to compare trend is "3.86"
           And the Weighted Gap Trend Score for Work Life Balance to compare trend is "-1.35"
           When I apply compared to as "remainder"
           Then the Evaluation Score for Work Life Balance to compare reminder is "4.11"
           And the Evaluation Trend Score for Work Life Balance to compare reminder is "+0.47"
           And the Importance Score for Work Life Balance to compare reminder is "4.29"
           And the Importance Trend Score for Work Life Balance to compare reminder is "-0.21"
           And the Gap Score for Work Life Balance to compare reminder is "0.18"
           And the Gap Trend Score for Work Life Balance to compare reminder is "-0.68"
           And the Weighted Gap Score for Work Life Balance to compare reminder is "3.86"
           And the Weighted Gap Trend Score for Work Life Balance to compare reminder is "-15.49"
           When I apply compared to as "org"
           Then the Evaluation Score for Work Life Balance to compare organization is "4.11"
           And the Evaluation Trend Score for Work Life Balance to compare organization is "+0.45"
           And the Importance Score for Work Life Balance to compare organization is "4.29"
           And the Importance Trend Score for Work Life Balance to compare organization is "-0.20"
           And the Gap Score for Work Life Balance to compare organization is "0.18"
           And the Gap Trend Score for Work Life Balance to compare organization is "-0.65"
           And the Weighted Gap Score for Work Life Balance to compare organization is "3.86"
           And the Weighted Gap Trend Score for Work Life Balance to compare organization is "-14.77"
           Now I go to "Logout"
