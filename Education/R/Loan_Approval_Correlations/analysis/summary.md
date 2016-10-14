Purpose : 
    Determine Corrolations of Loan_Total, DTI Ratio, Employment Length, Year, Month, State to Acceptance
 
Implementation :
    Before analyzing data, dti data is furthur cleaned. Rejected dti's include dti's > 2000 and < 0. The rejected loan_totals also include a few outliers beyond 40000. Because these are extreem outliers and the rejected dataset is large enough on its own, they were stripped from the data. Our dataset is reduced by 4.35%.
    
    We attempt to understand the data more fully by graphing the data's variance and then we analyze the acceptance ratio of data's catagories. The acceptance ratio is by definition of the general probability function, the probability that an application would be accepted given a certain value of data. Analyzing the acceptance ratio, thus, enables us to predict and correlate acceptance by that data's values.
    
Loan_Total -vs- Acceptance   
1)
    - First we employ a box plot to plot the loan total variance distribution for accepted and rejected applications. (Fig 1)
    - From this boxplot we can see that the variance of the rejected applications is much greater than the approved applications, and skewed towards the larger values. We also can note that the median accepted and rejected values are similar: this indicates that the median accepted value is likely a product of application distribution rather than an artificially driven value.
  
2)
    - Next we create a histogram comparing the full loan_total distribution with the approved loan_total distribution. (Fig 2). While it tells us how small the percentage of approved loans is and that it gets smaller and smaller as loan value increases, a graph displaying the ratio of accepted per applied loans per loan_total distribution would tell us more. To create a graph relating the ratio of accepted loans per loan applications and loan_totals applied for we first catagorize the infinite loan_totals dataset. Then, we are able to calculate the total frequency of accepted loans and loan applications in each loan_total catagory, create ratios, and display the result in a bargraph (Fig 3). 
    - The distribution shows a smooth gausian curve, skewed to the left with a mean between 8 and 12 thousand with a 13% acceptance ratio - yet with a sudden overwelming peak around the 20k amount with a 18.7% acceptance ratio.
    

DTI -vs- Acceptance
1) 
    - Using a boxplot, we analyse the variance of accepted and rejected applications (Fig 4). 
    - From this plot we see again that the variance of the rejected applications is much greater than the approved applications, and that again the rejected applications are skewed towards larger values. We also notice that there is a very large symetry to the accepted DTI ratio. (Fig 5)
    
2)
    - We create a histogram that displays the distribution of all applicants with DTI's below 30% (the cutoff for approved applications) as well as the distribution of all approved applications. (fig 6)
    - From this histogram we can see that the approved applications display an excellent gaussian distribution. We can also see that, not regarding the 0-2% range, the DTI for all applications shares this distribution. Possible reason for the extreemly large volume of 0-2% DTI applications could include borrowers with no credit history attempting to open their first line, and thus being declined, or errors in the collected data. 
  
    -As done before, we can graph and relate the ratio of accepted loans per total loan applications and the DTI catagories. We implement the same method as used in relating Loan_Totals to the Acceptance Ratio and create the graph shown in (Fig 7). 
    - The result is a clear gaussian distribution, demonstrating that the largest acceptance rates (~17.5%) occur between [10, 25)% DTI. [0-5)% and [25-30)% DTI have slim, but real chances. [30,inf) has zero chance of being accepted. 
    - There is a strong correlation between DTI and acceptance
    
    
Employment Length vs Acceptance
1)
    - For relating employment length and acceptance rate we will not be able to use a box plot, because both employment length and acceptance are catagorical data types. However, we will be able to use a bar graph. We may attempt to view how the magnitudes of total, accepted, and rejected applications compare in a bar graph (Fig 8). This, however, is not a very informative approach. 
    - Like usual, we relate the acceptance ratio to the catagories of employment length. (Fig 9) Instantly we see a very informative data representation : we can clearly see how applicants with less than one year of employment have slim chances of getting approved, and that this chance rises untill about 4 years of employment, after which point the acceptance ratio levels off at around 25%.
    - There is a strong correlation between employment length and acceptance.
    
Year vs Acceptance    
1)
    - Year vs Acceptance is not analyzed for absolute magnitudes, as we would receive the same level of information as the approach rendered for employment length. Instead we skip straight to relating the acceptance ratio to the catagories of years. (Fig 10)
    - We see, as we could have assumed, that the acceptance ratios do not vary much depending on the year the applicant applied. Surprisingly, however, is that even applicants durring the financial crisis year 2008 had almost the same chances (within 1%) as applicants in the years 2010 and 2011. 
    - Any given year there is about 10% chance of being accepted, just for applying.
    - There is little to no corellation between year and acceptance

Month vs Acceptance
    - Again, we skip straight to approval ratios for analyzing the Month's effect on acceptance. (Fig 11)
    - Interestingly, it appears that there is a small correlation between the month that the application is processed and the chance that the application is approved. For example, applications submitted in May have a 3% greater chance to be submitted than the two months before and two months after May. However, this may be due to discrepencies in how the month data was generated. Additonally, 3% chance is small enough to be a fluke, and is nothing that promotes and exceptionally strong relationship.

State vs Acceptance
    - (Fig 12) demonstrates the relationship between the state that the applicant resides in and the acceptance ratio of an application. 
    - The approval ratio bar graph quickly shows that there is a definitly discrepencies between the acceptance ratios of different states. For example, the district of columbia (DC) has an approval ratio of 18.93%, while IN only has an acceptance ratio of 3.69.

----------
-- Interesting to see if there is a reason the acceptance ratios vary per state. Are applicants from IN higher DTI, Higher loan amount, lower emp_length?
----------

Relating Multiple Variables to Acceptance
    - Higher DTI and Loan Amounts = Higher Acceptance
    - Higher Emp Lneght and Loan Amount - higher acceptance