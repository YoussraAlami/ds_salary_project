# Data Science Salary Estimator: Project Overview

<ul dir="auto">
<li>Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.</li>
<li>Scraped over 1000 job descriptions from glassdoor using python and selenium</li>
<li>Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.</li>
<li>Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.</li>
</ul>

# Code and Resources Used
Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

# Web Scraping
 scrape 1000 job postings from glassdoor.com. With each job, we got the following:
<ul dir="auto">
<li>Job title</li>
<li>Salary Estimate</li>
<li>Job Description</li>
<li>Rating</li>
<li>Company</li>
<li>Location</li>
<li>Company Headquarters</li>
<li>Company Size</li>
<li>Company Founded Date</li>
<li>Type of Ownership</li>
<li>Industry</li>
<li>Sector</li>
<li>Revenue</li>
<li>Competitors</li>
</ul>

# Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
<ul dir="auto">
<li>Parsed numeric data out of salary</li>
<li>Made columns for employer provided salary and hourly wages</li>
<li>Removed rows without salary</li>
<li>Parsed rating out of company text</li>
<li>Made a new column for company state</li>
<li>Added a column for if the job was at the company’s headquarters</li>
<li>Transformed founded date into age of company</li>
<li>Made columns for if different skills were listed in the job description:
<ul dir="auto">
<li>Python</li>
<li>R</li>
<li>Excel</li>
<li>AWS</li>
<li>Spark</li>
</ul>
</li>
<li>Column for simplified job title and Seniority</li>
<li>Column for description length</li>
</ul>

# EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.
<img src="https://github.com/PlayingNumbers/ds_salary_proj/raw/master/salary_by_job_title.PNG" alt="alt text" title="Salary by Position" style="max-width: 100%;">
<img src="https://github.com/PlayingNumbers/ds_salary_proj/raw/master/positions_by_state.png" alt="alt text" title="Job Opportunities by State" style="max-width: 100%;">
<img src="https://github.com/PlayingNumbers/ds_salary_proj/raw/master/correlation_visual.png" alt="alt text" title="Correlations" style="max-width: 100%;">

# Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:
<ul dir="auto">
<li><strong>Multiple Linear Regression</strong> – Baseline for the model</li>
<li><strong>Lasso Regression</strong> – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.</li>
<li><strong>Random Forest</strong> – Again, with the sparsity associated with the data, I thought that this would be a good fit.</li>
</ul>

# Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets.
<ul dir="auto">
<li><strong>Random Forest</strong> : MAE = 11.22</li>
<li><strong>Linear Regression</strong>: MAE = 18.86</li>
<li><strong>Ridge Regression</strong>: MAE = 19.67</li>
</ul>
