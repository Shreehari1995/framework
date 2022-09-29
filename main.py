from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep

driver = Chrome(r"C:\Users\Shreehari\Desktop\chromedriver.exe")
driver.get("https://www.flipkart.com/")

wait = WebDriverWait(driver, 20)


def wait_till_element_visible(loc, xpath):
    wait.until(visibility_of_element_located((xpath, loc)))


wait_till_element_visible("//button[text()='✕']", "xpath")
driver.find_element("xpath", "//button[text()='✕']").click()
sleep(5)
driver.close()












# s = "aabbbkkajkjnkj@@#&&^$$#ccssaaa"
#
#
# n = 0
# m = "n"
# s1 = ""
# for i in s:
#     if i == m:
#         continue
#     else:
#         c = 0
#         m = i
#         for j in s[n:]:
#             if i == j:
#                 c += 1
#             else:
#                 break
#         n += c
#         s1 += str(c) + i
# print(s1)
#
#
#
#
#
#
# l = [1, 2, 3]
# if l.append(4):
#     print("hi")
# else:
#     print("hello")
# print(l.append(5))
