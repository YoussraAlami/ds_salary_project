from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
import numpy as np


def get_javascript_jobs(keyword, num_jobs,verbose, path, slp_time):
    """ scrape jobs of javascript developer from glassdoor"""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=path, options = options)
    driver.set_window_size(1120, 1000)
    
    url ="https://www.glassdoor.com/Job/javascript-jobs-SRCH_KO0,10_IP30.htm"
    driver.get(url)
    
    A, B, C, D, E, F, G, H, I, J, K, L, M, O = ([] for i in range(14))
    
    
    dic = {"Job Title":A,
            "Salary Estimate":B,
            "Job Description":C ,
            "Rating":D,
            "Company Name":E, 
            "Location":F,
            "Headquarters":G, 
            "Size":H,
            "Founded":I,
            "Type of ownership":J,  
            "Industry":K,
            "Sector":L,
            "Revenue":M,
            "Competitors":O}
    
    while True:
        print(dic)
        time.sleep(slp_time)
        # try:
        #     driver.find_element_by_class_name("selected").click()
        # except ElementClickInterceptedException:
        #     pass

        # time.sleep(.1)
        
        try:
            driver.find_element_by_class_name("SVGInline-svg modal_closeIcon-svg").click()  #clicking to the X.
            print(' x out worked')
        except NoSuchElementException:
            print(' x out failed') 
            pass
        #Going through each job in this page
        job_buttons = driver.find_elements_by_class_name("react-job-listing css-1kjejvf eigr9kq3")  #jl for Job Listing. These are the buttons we're going to click.
        for job_button in job_buttons:  

            print("Progress: {}".format("" + str(len(dic)) + "/" + str(num_jobs)))
            #if len(dic) >= num_jobs:
                #break

            job_button.click()  #You might 
            time.sleep(5)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    company_name = driver.find_element_by_xpath('.//*[@id="MainCol"]/div[1]/ul/li/div/div/a/div[1]/div[1]/div[2]').text #done
                    location = driver.find_element_by_xpath('.//*[@id="MainCol"]/div[1]/ul/li/div/div/a/div[1]/div[3]').text #done
                    job_title = driver.find_element_by_xpath('.//*[contains(@id, "job-title")]').text #done
                    job_description = driver.find_element_by_xpath('.//*[@id="JobDesc"]/div/div/div/p').text #done
                    collected_successfully = True
                except:
                    time.sleep(5)

            try:
                salary_estimate = driver.find_element_by_xpath('.//*[@id="MainCol"]/div[1]/ul/li/div/div/a/div[1]/div[4]').text #done
            except NoSuchElementException:
                salary_estimate = np.nan #You need to set a "not found value. It's important."
        
            try:
                rating = driver.find_element_by_xpath('.//*[@id="MainCol"]/div[1]/ul/li/div/div/a/div[1]/div[1]/div[2]/span[2]').text#done
            except NoSuchElementException:
                rating = np.nan #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            try:
                driver.find_element_by_xpath('.//*[@id="EmpBasicInfo"]/div[1]/h2').click()

                # try:
                #     headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
                # except NoSuchElementException:
                #     headquarters = np.nan

                try:
                    size = driver.find_element_by_xpath('.//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[1]').text
                except NoSuchElementException:
                    size = np.nan

                try:
                    founded = driver.find_element_by_xpath('.//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[1]').text
                except NoSuchElementException:
                    founded = np.nan

                try:
                    type_of_ownership = driver.find_element_by_xpath('.//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[1]').text
                except NoSuchElementException:
                    type_of_ownership = np.nan

                try:
                    industry = driver.find_element_by_xpath('.//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[1]').text
                except NoSuchElementException:
                    industry = np.nan

                try:
                    sector = driver.find_element_by_xpath('.//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[1]').text
                except NoSuchElementException:
                    sector = np.nan

                try:
                    revenue = driver.find_element_by_xpath('.//*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[1]').text
                except NoSuchElementException:
                    revenue = np.nan

                # try:
                #     competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                # except NoSuchElementException:
                #     competitors = np.nan

            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                headquarters = np.nan
                size = np.nan
                founded = np.nan
                type_of_ownership = np.nan
                industry = np.nan
                sector = np.nan
                revenue = np.nan
                competitors = np.nan

                
            if verbose:
                print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            A.append(job_title)
            B.append(salary_estimate)
            C.append(job_description)
            D.append(rating)
            E.append(company_name)
            F.append(location)
            G.append(headquarters)
            H.append(size)
            I.append(founded)
            J.append(type_of_ownership)
            K.append(industry)
            L.append(sector)
            M.append(revenue)
            O.append(competitors)
            
            
        break


    return dic  #This line converts the dictionary object into a pandas DataFrame.

path = "C:/Users/Dell/Documents/ds_salary_project/chromedriver"
dic = get_javascript_jobs("javascript", 30, True, path,15 )
javascript_file1 = pd.DataFrame(dic)
javascript_file1.to_csv("javascript_file20.csv",index = False)