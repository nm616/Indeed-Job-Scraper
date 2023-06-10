import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
actions = ActionChains(driver)

terms_list = [
    'helpdesk',
    'help desk',
    'desktop support',
    'IT Support',
    'Technical Service Representative',
    'Technical Support',
    'IT Field Technician',
    'Field Technician',
    'Application Support',
    'CSR',
    'Customer Support Representative',
]

where_list = [
    '49525',
    'remote',
]

driver.get('https://www.indeed.com')
input("Please sign in then press any key to continue: ")

for location_index in range(len(where_list)):
    for term_index in range(len(terms_list)):
            try:
                keep_going = True
                driver.get('https://www.indeed.com')
                time.sleep(2)

                what = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
                what.click()
                what.clear()
                what.send_keys(terms_list[term_index])

                where = driver.find_element(By.XPATH, '//*[@id="text-input-where"]')
                actions.click(where).double_click(where).perform()
                where.send_keys(Keys.BACKSPACE)
                where.send_keys(where_list[location_index])

                submit = driver.find_element(By.XPATH, '//*[@id="jobsearch"]/button')
                submit.click()
                time.sleep(2)

                date_posted = driver.find_element(By.XPATH, '//*[@id="filter-dateposted"]')
                date_posted.click()
                last_day = driver.find_element(By.XPATH, '//*[@id="filter-dateposted-menu"]/li[1]/a')
                last_day.click()
                time.sleep(2)

                experience_level = driver.find_element(By.XPATH, '//*[@id="filter-explvl"]')
                experience_level.click()
                entry_level = driver.find_element(By.XPATH, '//*[@id="filter-explvl-menu"]/li[1]/a')
                entry_level.click()
                time.sleep(2)

                if where_list[location_index] != 'remote':
                    radius = driver.find_element(By.XPATH, '//*[@id="filter-radius"]')
                    radius.click()
                    miles = driver.find_element(By.XPATH, '//*[@id="filter-radius-menu"]/li[5]/a')
                    miles.click()
                    time.sleep(2)
                else:
                    remote = driver.find_element(By.XPATH, '//*[@id="filter-remotejob"]')
                    remote.click()
                    remote2 = driver.find_element(By.XPATH, '//*[@id="filter-remotejob-menu"]/li/a')
                    remote2.click()
                    time.sleep(2)
                while keep_going:
                    buttons = driver.find_elements(By.XPATH, '//button[starts-with(@id, "jobActionButton-")]')
                    for button in buttons:
                        time.sleep(1)
                        button.click()
                        save_job = driver.find_element(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul/li[1]/div/div[2]/div[2]/div/button[1]')
                        if save_job.text == 'Save job':
                            save_job.click()
                    try:
                        next_page = driver.find_element(By.XPATH, '//*[@data-testid="pagination-page-next"]')
                        if next_page:
                            keep_going = True
                            next_page.click()
                        else:
                            keep_going = False
                    except:
                        keep_going = False
            except:
                print('No Results')



