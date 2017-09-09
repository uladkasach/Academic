///////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////
Begin Generating Full Dataset from Seperate Datasets
//////
//////

//////////////////////
// Extract and Name Relevant Data
//////////////////////
min_approved <- approved[1:20, c("loan_amnt", "issue_d", "emp_length", "zip_code", "addr_state", "dti")]
colnames(min_approved) <- c("loan_total", "date", "emp_length", "zipcode", "state", "dti")
----------------
min_rejected <- rejected[1:20, c("Amount.Requested", "Application.Date", "Employment.Length", "Zip.Code", "State", "Debt.To.Income.Ratio" )]
colnames(min_rejected) <- c("loan_total", "date", "emp_length", "zipcode", "state", "dti")

///////////////////
// Data Engineering
////////////////////

Convert dti format of rejected to approved format
------------------------
min_rejected$dti <- as.numeric(sub("%","",min_rejected$dti))


Determine month and year from various date formats given
------------
min_approved$month <- as.numeric(match(substr(min_approved$date, 0, 3), month.abb))
min_approved$year <- as.numeric(substr(min_approved$date,5,9))
-------------
min_rejected$month <- as.numeric(substr(min_rejected$date, 6, 7))
min_rejected$year <- as.numeric(substr(min_rejected$date, 0, 4))


Remove all rejected datas year 2012 and above
-------------
min_rejected = min_rejected[min_rejected$year < 2012, ]

Attach Approval Status to datas
--------------
min_approved$approved = 1;
min_rejected$approved = 0;

Concantenate Data
--------------
full <- rbind(min_approved, min_rejected)

Remove Unessesary Field
--------------
full$date = NULL

///////////////////////
// Save final data
///////////////////////
write.csv(full, file = "/var/www/git/R/Stat350/Project1/data/full_relevant_compiled.csv",row.names=FALSE, na="")


///////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////
Begin Generating Full Dataset from Seperate Datasets
//////
//////

//////////////////
Amount.Requested ~= loan_amnt
Application.Date ~= issue_d 
Employment.Length == emp_length
Zip.Code ~= zip_code 
State ~= addr_state
Debt.To.Income.Ratio ~= dti -vs- dti_joint
//////////////////


///////////////////////////////////////////////
// Create data sets
///////////////////////////////////////////////
set <- full_relevant_compiled[full_relevant_compiled$year == 2008, ]
//////////////////
// Clean DTI for set, (over 2000 is likely some kind of mistake and there is more than enough data to "trim" it off with. -1 may also be a mistake, as it is not present in accepted while 0 is still in both.) (Approved dti is [0,35), rejected is [-1, ~inf)
///////////////////
set <- set[set$dti < 2000 & set$dti > -1 & set$loan_total < 40000, ]
approved <- set[set$approved == 1, ]
rejected <- set[set$approved == 0, ]


///////////////////////////////////////////////
// Total Loan Ammount vs Acceptance
////////////////
1)
boxplot(set$loan_total~set$approved,  main="Loan Total vs Approval", 	xlab="Approved", ylab="Loan Total ($)")


2) Histogram 
h1 = hist(set$loan_total, main = 'Histogram of All Loan Requests', xlab = 'USD ($)')
h2 = hist(set$loan_total[set$approved == 1], main = 'Histogram of Accepted Loan Requests', xlab = 'USD ($)')
plot( h1, col=rgb(0,0,1,1/4), xlim=c(0,30000), main = 'Histograms of Loan Totals', xlab = 'USD ($)')  # first histogram
plot( h2, col=rgb(1,0,0,1/4), xlim=c(0,30000), add=T)  # second

3) Get ratio of accepted per interval
t_ltc = table(cut(set$loan_total, seq(0, 40000, 4000) ))
t_ltc_a = table(cut(set$loan_total[set$approved == 1], seq(0, 40000, 4000) ))
t_ratio = t_ltc_a/t_ltc
barplot(t_ratio, xlab = 'Loan Total in USD ($), $4000 intervals', ylab = 'Approved / All (%)', main = 'Ratio Approved per Loan Total Catagory')
-- Shows a more gausian distribution. Peak loan acceptance ratio at 10-12k.


///////////////////////////////////////////////
// DTI vs Acceptance
////////////////
2)
boxplot(set$dti[set$dti < 100]~set$approved[set$dti < 100],  main="Debt to Income", 	xlab="Approved", ylab="DTI %")
Analyzing the debt to income ratios for accepted and rejected loans, we notice that although the medians of both accepted and rejected dti are similar, the variance of rejected loans is much, much larger. In fact, the variance and range of accepted dti is very narrow and looks very symetric. 


boxplot(set$dti[set$dti < 100 & set$approved == 1],  main="Debt to Income", 	xlab="Approved", ylab="DTI %")

The question of whether the symetry of the variance is due to having less approved loans at the extreems of the variance range arises. Having a low dti is a good thing as it means that the aplicant has more disposable income, so it would not make sence that less applicants are accepted at lower dti ranges. However, it would make sence that less are accepted at higher dti ranges. A histogram will be able to enlighten us on the distribution of the accepted dti ranges.

1) Accepted DTI
hist(set$dti[set$dti < 100 & set$approved == 1], main = 'Histogram of Approved DTI', xlab = 'DTI')
This distribution shows us that a dti < 22% has ~equal odds of being accepted, while this acceptance rate tapers down towards higher dti with an apparent cutoff at 30%.

--!!!-- DTI vs interest rates on approved loans
2) Total DTI
hist(set$dti[set$dti < 30], main = 'Histogram of All DTI below 30%', xlab = 'DTI')

3) all together now
h1 = hist(set$dti[set$dti < 30], main = 'Histogram of All DTI below 30%', xlab = 'DTI')
h2 = hist(set$dti[set$dti < 30 & set$approved == 1], main = 'Histogram of Approved DTI', xlab = 'DTI')
plot( h1, col=rgb(0,0,1,1/4), main = 'Histograms of All -vs- Approved DTI, in Approval Range', xlab = 'USD ($)')  # first histogram
plot( h2, col=rgb(1,0,0,1/4), add=T)  # second

4) Ratio
t_dti_cat = table(cut(set$dti[set$dti<100], seq(0, 50, 5) ))
t_dti_cat_a = table(cut(set$dti[set$dti<100 & set$approved == 1], seq(0, 50, 5) ))
t_dti_ratio = t_dti_cat_a/t_dti_cat
barplot(t_dti_ratio, xlab = 'DTI Ratio (%), 5% intervals',  ylab = 'Approved / All (%)', main = 'Approval Ratio per DTI Catagory')

5) Loan Total vs DTI Approved and ALL
plot(set$loan_total[set$approved == 1], set$dti[set$approved == 1], xlab = 'Loan Total ($)', ylab = 'DTI (%)')
plot(set$loan_total[set$loan_total < 28000 & set$dti < 30], set$dti[set$loan_total < 28000 & set$dti < 30], xlab = 'Loan Total ($)', ylab = 'DTI (%)')
-- Easily seen that there is a purposeful selection of dti/loan total. Higher loan total, lower dti

///////////////////////////////////////////////
// Employment Length vs Acceptance
////////////////
0) Bar Graph of Employment Length vs Acceptance

emp_length_factored <- factor(set$emp_length, levels = c("< 1 year", "1 year",  "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "8 years", "9 years", "10+ years"))
emp_length_factored_approved <- factor(set$emp_length[set$approved == 1], levels = c("< 1 year", "1 year",  "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "8 years", "9 years", "10+ years"))
emp_length_factored_rejected <- factor(set$emp_length[set$approved == 0], levels = c("< 1 year", "1 year",  "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "8 years", "9 years", "10+ years"))
result = rbind(table(emp_length_factored), table(emp_length_factored_approved), table(emp_length_factored_rejected))
barplot(result, main="Employment Length vs Acceptance", xlab="Employment Length (Years)", col=c("darkblue","darkgreen","red"), legend = c("All", "Accepted", "Rejected"), beside=TRUE)
--- Does not say anything particularly significant.


2)
t_elf = table(emp_length_factored)
t_elf_a = table(emp_length_factored_approved)
ratio_t_elf = t_elf_a/t_elf
barplot(ratio_t_elf, xlab = 'Employment Length (Years)', ylab = 'Approved / All (%)', main ='Ratio Approved per Employment Length')



1) box plot of employement lengths vs acceptance*rejection

set$emp_length_factored <- factor(set$emp_length, levels = c("< 1 year", "1 year",  "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "8 years", "9 years", "10+ years"))
b2 = boxplot(set$loan_total[set$approved == 1 & set$loan_total < 25000]~set$emp_length_factored[set$approved == 1 & set$loan_total < 25000],  main="Loan Total vs Emp Length for Accepted", 	xlab="EmpLength", ylab="Loan Total $")
b3 = boxplot(set$loan_total[set$approved == 0  & set$loan_total < 25000]~set$emp_length_factored[set$approved == 0 & set$loan_total < 25000],  main="Loan Total vs Emp Length for Rejected", 	xlab="EmpLength",  ylab="Loan Total $")

-- Interestingly, it appears that there is more of a downward limit associated with employment length: although rejections have no minimum, on many employement periods there is a minimum loan ammount that they will approve.

///////////////////////////////////////////////
// Year vs Acceptance
////////////////
t_year = table(set$year)
t_year_a = table(set$year[set$approved == 1])
t_year_ratio = t_year_a/t_year
barplot(t_year_ratio, xlab = 'Year', ylab = 'Approved / All (%)', main = 'Ratio Approved per Year')

///////////////////////////////////////////////
// Month vs Acceptance
////////////////
t_month = table(set$month)
t_month_a = table(set$month[set$approved == 1])
t_month_ratio = t_month_a/t_month
barplot(t_month_ratio, xlab = 'Month', ylab = 'Approved / All (%)', main = 'Ratio Approved per Month')

barplot(t_month, xlab = 'Month', ylab = 'Frequency', main = 'Frequency of Applications / Month')

///////////////////////////////////////////////
// State vs Acceptance
////////////////
t_state = table(set$state)
t_state_a = table(set$state[set$approved == 1])
t_state_ratio = t_state_a/t_state
barplot(t_state_ratio, xlab = 'State', ylab = 'Approved / All (%)', main = 'Ratio Approved per State')