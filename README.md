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
