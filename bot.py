# #first version of bot
#
# import time
# import psycopg2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException, WebDriverException
#
# DB_PARAMS = {
#     'dbname': 'your_db',
#     'user': 'your_user',
#     'password': 'your_password',
#     'host': 'localhost',
#     'port': 5432
# }
#
# REG_DATA = {
#     'first_name': 'LogAspergerus',
#     'last_name': 'Regus',
#     'email': 'testuser@example.com',
#     'password': 'SecurePass123!',
#     'birth_day': '10',
#     'birth_month': 'May',
#     'birth_year': '1995',
#     'gender': '2'
# }
#
# def save_result_to_db(email, status, error_message=None):
#     try:
#         conn = psycopg2.connect(**DB_PARAMS)
#         cur = conn.cursor()
#         cur.execute(
#             "INSERT INTO registration_logs (email, status, error) VALUES (%s, %s, %s)",
#             (email, status, error_message)
#         )
#         conn.commit()
#         cur.close()
#         conn.close()
#     except Exception as db_err:
#         print("Ошибка при записи в БД:", db_err)
#
# def register_on_facebook():
#     options = Options()
#     options.add_argument('--headless')  # Без GUI
#     options.add_argument('--disable-gpu')
#     driver = webdriver.Chrome(options=options)
#
#     try:
#         driver.get("https://www.facebook.com/")
#
#         time.sleep(3)
#
#         driver.find_element(By.XPATH, "//a[text()='Создать новый аккаунт']").click()
#         time.sleep(2)
#
#         driver.find_element(By.NAME, "firstname").send_keys(REG_DATA['first_name'])
#         driver.find_element(By.NAME, "lastname").send_keys(REG_DATA['last_name'])
#         driver.find_element(By.NAME, "reg_email__").send_keys(REG_DATA['email'])
#         driver.find_element(By.NAME, "reg_email_confirmation__").send_keys(REG_DATA['email'])
#         driver.find_element(By.NAME, "reg_passwd__").send_keys(REG_DATA['password'])
#
#         driver.find_element(By.ID, "day").send_keys(REG_DATA['birth_day'])
#         driver.find_element(By.ID, "month").send_keys(REG_DATA['birth_month'])
#         driver.find_element(By.ID, "year").send_keys(REG_DATA['birth_year'])
#
#         driver.find_element(By.XPATH, f"//input[@name='sex' and @value='{REG_DATA['gender']}']").click()
#
#         driver.find_element(By.NAME, "websubmit").click()
#
#         time.sleep(10)
#
#         if "confirmemail" in driver.current_url:
#             save_result_to_db(REG_DATA['email'], "успешно")
#             print("Регистрация прошла успешно.")
#         else:
#             save_result_to_db(REG_DATA['email'], "ошибка", "Не удалось завершить регистрацию")
#             print("Регистрация не завершена.")
#
#     except (NoSuchElementException, WebDriverException) as e:
#         save_result_to_db(REG_DATA['email'], "ошибка", str(e))
#         print("Ошибка во время регистрации:", e)
#
#     finally:
#         driver.quit()
#
# if __name__ == "__main__":
#     register_on_facebook()
