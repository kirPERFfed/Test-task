from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://admin.develop.v3.iot.pn/login"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
# Проходим авторизацию
login_input = browser.find_element(By.XPATH, "//input[@data-test-login='login']")
login_input.send_keys("admin")
password_input = browser.find_element(By.XPATH, "//input[@data-test='password']")
password_input.send_keys("07x6eae0EceCwOQKK377Co6BzBFk98Ww")
button_login = browser.find_element(By.CSS_SELECTOR, "button[class*=mt-4]").click()
# Переходим в нужный раздел
menu = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class*=v-app-bar__nav-icon]"))).click()
button_datasets = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-test-menu='datasets']"))).click()
# проверка корректности перехода в нужный раздел
check = browser.find_element(By.CSS_SELECTOR, "h6[class*=text-capitalize]").text
check1 = 'Datasets'
assert check == check1, f'Тест не пройден, полученное значение {check}'
# Добавляем новое устройство
button_datasets_1 = browser.find_element(By.CSS_SELECTOR, "button[class*=d-flex]").click()
button_add = browser.find_element(By.CSS_SELECTOR, "div[data-test-dropdown='addNew']").click()

input_name = browser.find_element(By.CSS_SELECTOR, "input[data-test-type='deviceName']")
input_name.send_keys("Test 1")
input_schema_name = browser.find_element(By.CSS_SELECTOR, "input[data-test-schema='deviceSchema']")
input_schema_name.send_keys("SELENIUM test datase")
button_string = browser.find_element(By.CSS_SELECTOR, "div[data-test-schema='SELENIUM test dataset']").click()
input_string = browser.find_element(By.CSS_SELECTOR, "textarea[data-test='description']")
input_string.send_keys("My test dataset")
button_add = browser.find_element(By.CSS_SELECTOR, "button[data-test-action='deviceCreateOrEditAction']").click()

# Вносим изменения
button_properties = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-test-tabs='properties']"))).click()
# A
button_string = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span/div[2]/div[@role='listitem']")))
ActionChains(browser).move_to_element(button_string).perform()
button_string_menu = browser.find_element(By.CSS_SELECTOR,
                                          "[entity] span:nth-of-type(1) > div:nth-of-type(2) [slot]").click()
button_edit_property = browser.find_element(By.CSS_SELECTOR, "div[data-test-action='edit property']").click()

input_string = browser.find_element(By.XPATH, "//div[@class='v-text-field__slot']/input")
input_string.send_keys("10")
button_save = browser.find_element(By.CSS_SELECTOR,
                                   "button[class='v-btn v-btn--text theme--light v-size--default primary--text']").click()
# copy
button_string_1 = browser.find_element(By.XPATH, "//span/div[2]/div[@role='listitem']")
ActionChains(browser).move_to_element(button_string_1).perform()
button_string_menu = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[entity] span:nth-of-type(1) > div:nth-of-type(2) [slot]"))).click()
button_string_1 = browser.find_element(By.XPATH, "//div[@data-test-action='copy']").click()
# B
button_string_2 = browser.find_element(By.XPATH, "//span/div[3]/div[@role='listitem']")
ActionChains(browser).move_to_element(button_string_2).perform()
button_string_menu_2 = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span/div[3]/div/div[2]/button[@slot='activator']"))).click()
button_edit_property_2 = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR,
                                      "#app [role='menu']:nth-of-type(5) .theme--light div:nth-of-type(1) .v-list-item--dense"))).click()
input_string = browser.find_element(By.CSS_SELECTOR, ".v-text-field__slot [type]")
input_string.send_keys(Keys.CONTROL, 'v')
button_save = browser.find_element(By.CSS_SELECTOR, ".v-btn--text.primary--text").click()
# Проверка корректности сохранения данных
time.sleep(1)
check = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "[entity] div:nth-of-type(3) .text-truncate"))).text
check1 = 'B: A: 10'
if check == check1:
    print(f"Данные {check}, сохранены успешно")
else:
    print("Ошибка!")
#  закрытие окна и logout
button_exit = browser.find_element(By.CSS_SELECTOR, "button[data-test='closeActionCard']").click()
button_user_menu = browser.find_element(By.CSS_SELECTOR, "button[data-test='userMenu']").click()
button_logout = browser.find_element(By.CSS_SELECTOR, "div[data-test='logout']").click()

time.sleep(2)
browser.quit()
