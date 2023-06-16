from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import csv

import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.set_window_size(1120, 1000)


def handle_popup():
    try:
        popup = driver.find_element("xpath","//*[@id='MainCol']/div[1]/ul/li[1]")
        if(popup):
            popup.click()
            time.sleep(2)
            driver.find_element("xpath",'//*[@id="JAModal"]/div/div[2]/span').click()  
            time.sleep(2)
    except:
        print("")
        
        
def get_jobs(country_code, country_name, job, num_of_jobs=1):
    search_text = f'{country_name}-${job}'
    start_pos = len(country_name) + 1
    end_pos = len(search_text)
    
    url = f'https://www.glassdoor.com/Job/{country_name}-{job}-jobs-SRCH_IL.0,2_I{country_code}_KO{start_pos},{end_pos}.htm?includeNoSalaryJobs=false'
    driver.get(url)

    time.sleep(10)
    jobs = []

    job = 1
    while job <= num_of_jobs :
        handle_popup()
             
        try:
            job_buttons = driver.find_elements(By.XPATH, '//*[@id="MainCol"]/div[1]/ul/li')
            
            try:
                job_buttons[0].click()
                time.sleep(5)
                handle_popup()
            except:
                print("first not found")
                
    
            for job_button in job_buttons:
                if(job >=num_of_jobs):
                    break
                job+=1
                
                try:        
                    job_button.click()
                    time.sleep(5)
                    print(f'Job Number: {job}')
                    
                except:
                    print("Failed to click on job button")
                    time.sleep(7)
                    continue
                    
                try:
                    job_title = driver.find_element(By.CSS_SELECTOR, 'div[data-test="jobTitle"]').text
                    print(f'Job title: {job_title}')
                except:
                    job_title = -1
                    print("Job title not found")
                    
                
                try:
                    employer_name = driver.find_element(By.CSS_SELECTOR, 'div[data-test="employerName"]').text
                except:
                    employer_name = -1
                    print("employer_name not found")
    
                try:
                    location = driver.find_element(By.CSS_SELECTOR, 'div[data-test="location"]').text
                except:
                    location = -1
                    print("location not found")
                                
    
                try:
                    Rating = driver.find_element(By.CSS_SELECTOR, 'span[data-test="detailRating"]').text
                    # print(f'Rating: {Rating}')
                except:
                    Rating = -1
                # handle_popup()
                ###Salary
                try:
                    salary = driver.find_element(By.CSS_SELECTOR, 'span[data-test="detailSalary"]').text
                    print(f'Salary: {salary}')
                except:
                    salary = -1
                    print("Salary not found")

                ###Company size
                try:
                    company_size = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
                    # print(f'company size: {company_size}')
                    
                except:
                    company_size = -1
                    # print("Comapny size not found")

                ###founded year
                try:
                    founded_year = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
                    # print(f'founded : {founded_year}')
                except:
                        founded_year = -1


                    # Show more button
                try:
                    showmorebutton = driver.find_element(By.XPATH, '//*[@id="JobDescriptionContainer"]/div[2]')
                    showmorebutton.click()

                except:
                    showmorebutton = -1
                
                try: 
                    description = driver.find_element(By.XPATH, '//div[@class="jobDescriptionContent desc"]').text
                    # print(f'description : {description}')

                except:
                    description = -1

                    
                    
                ##Comapny Revenue
                try:
                        Company_Revenue = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[2]').text
                        # print(f'Revenue : {Company_Revenue}')

                except:
                    Company_Revenue=-1

                ##industry
                try:
                        Industry = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
                        # print(f'Industry : {Industry}')

                except:
                    Industry=-1
                ##Company Type
                try:
                    Company_Type = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
                    # print(f'Company Type : {Company_Type}')

                except:
                    Company_Type=-1

                ## Company Sector
                try:
                    Company_Sector = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
                    # print(f'Company Sector : {Company_Sector}')

                except:
                    Company_Sector =-1
            
                try:
                    carrier_opportunities = driver.find_element(By.XPATH, '//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[3]').text
                except:
                    carrier_opportunities =-1
 
                try:
                    comp_and_benefits = driver.find_element(By.XPATH, '//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[6]').text
                except:
                    comp_and_benefits =-1
 
                try:
                    culuture_and_values = driver.find_element(By.XPATH, '//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[9]').text
                except:
                    culuture_and_values =-1

                try:
                    senior_management = driver.find_element(By.XPATH, '//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[12]').text
                except:
                    senior_management =-1
 

                try:
                    life_balance = driver.find_element(By.XPATH, '//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div/ul/span[15]').text
                except:
                    life_balance =-1
 
 
                try:
                    btn_1 = driver.find_element(By.XPATH, '//*[@id="JDCol"]//button[@type="button" and contains(text(), "Retry your search")]')

                    if btn_1:
                        btn_1.click()
                        time.sleep(10)
                        print("**************FOUND BTN1*******")
                except:
                    btn_1 = -1
 
                try:
                    btn_2 = driver.find_element(By.XPATH, "//div[@id='JDCol']//button[@type='button' and contains(text(), 'Retry your search')]")

                    if btn_2:
                        btn_2.click()
                        time.sleep(10)
                        print("**************FOUND BTN2*******")
                except:
                    btn_2 = -1
                try:
                    btn_3 = driver.find_element(By.XPATH, "//*[@type='button' and contains(text(), 'Retry your search')]")
                    if btn_3:
                        btn_3.click()
                        time.sleep(7)
                    print("**************FOUND BTN3*******")
                except:
                    btn_3 = -1                                                                                                                                                                           
                jobs.append({
                    "Job Title": job_title,
                    "Glassdoor Location": country_name,
                    "Employer Name": employer_name,
                    "Location": location,
                    "Rating": Rating,
                    "Salary": salary,
                    "Carrier Opportunities": carrier_opportunities,
                    "Culure And Values": culuture_and_values,
                    "Senior Management": senior_management,
                    "Comp And Benefits": comp_and_benefits,
                    "Life Balance": life_balance,
                    "Company Size": company_size,
                    "Found year": founded_year,
                    "Description": description,
                    "Company Revenue": Company_Revenue,
                    "Industry": Industry,
                    "Company Type": Company_Type,
                    "Company Sector": Company_Sector
                })

                # handle_popup()
            try:
                next_page_btn = driver.find_element(By.XPATH,'//*[@id="MainCol"]/div[2]/div/div[1]/button[7]')
                if next_page_btn.get_property('disabled') == True:
                    print("Last Page")
                    break
                next_page_btn.click()
                time.sleep(7)
                
                print("$$$$$$4This is the next page!!@!@@!@")
            except e:
                print("Next button not found",e)
                break
                
        except Exception as e :
            print(e)
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_of_jobs, len(jobs)))
            break

    return jobs


def save_to_csv(csv_file_path,jobs):
    headers = list(jobs[0].keys())

    with open(csv_file_path, "w", newline="",encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for item in jobs:
            writer.writerow(item)   

def get_data_science_jobs(country_code, num_of_jobs=10):
    jobs = []
    job_names = [
        # 'data analyst',
        # 'data scientist',
        # 'machine learning engineer',
        'data engineer'
    ]
    for country_name, code in country_code.items():
        for jon_name in job_names:
            country_jobs = get_jobs(country_code=code, country_name=country_name, job=jon_name, num_of_jobs=num_of_jobs)
            try:
                save_to_csv(f'{country_name}_data_engineer.csv',country_jobs)
            except Exception as e:
                print("failed to save country to csv",)
            jobs.extend(country_jobs)
    
    return jobs

country_code = {
    "california": "S2280",
    "new-york": "C1132348",
    "san-jose": "C1147436",
    "los-angeles": "C1146821",
    "atlanta": "C1155583",
    "houston": "C1140171",
    "washington": "C1138213",
    "seattle": "C1150505",
    # "australia": "N16"
    # "us": "N1",
    "canada": "N3",
    "ireland": "N70",
    # "australia": "N16"
}

data_science_jobs = get_data_science_jobs(country_code=country_code, num_of_jobs=820)

save_to_csv(csv_file_path="data.csv", jobs=data_science_jobs)