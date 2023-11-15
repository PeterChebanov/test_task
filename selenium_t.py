from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://demoqa.com/webtables ')


row_element_xpath = '//*[@role="rowgroup"]' # find a list of elements in DOM, each represents a single row in table
first_column_in_a_raw = '//div[@role="gridcell"][1]' # represents 1st column in a row. We can reach any desired column,
                                                     # in the row by changing [number] parameter in the end of xpath

first_colum_list = [] # here we will collect value of each first column if the value exists

for row in (WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, row_element_xpath))).
        find_elements(By.XPATH, first_column_in_a_raw)): # looping over each first column in a row

    if row.text.isspace():
        break # assuming empty fields are not allowed
    else:
        first_colum_list.append(row.text) # collecting value of each not empty entry in 1st column

print(len(first_colum_list)) # the length of the list is an amount of not empty entries the table currently has
print(first_colum_list) # list of values collected
