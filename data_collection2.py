# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:28:27 2023

@author: Dell
"""

import glassdoor_scraper2_weld as gs 
import pandas as pd 

path = "C:/Users/Dell/Documents/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)