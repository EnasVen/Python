from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.google.com.tw')
driver.quit()

# driver 的屬性
# current_url : 當前網址
# page_source : 讀取網頁原始碼
# text : 讀取元素內容
# size : 回傳元素大小

# driver 的方法
# get_window_position() : 取得視窗左上角位置
# set_window_position(x,y) : 設定視窗左上角座標
# maximize_window() : 最大化視窗
# get_window_size() : 取得視窗高度和寬度
# set_window_size(x,y) : 設定視窗高度和寬度
# click() : 點擊按鈕
# close() : 關閉瀏覽器
# get(url) : 連結網址
# refresh() : 重新整理
# back() : 回到上一頁
# forward() : 下一頁
# clear() : 清除輸入內容
# send_keys() : 以鍵盤輸入
# submit() : 提交
# quit() : 關閉瀏覽器並退出driver程序

# 尋找網頁元素
# find_element_by_id(id) : 以id查詢符合的元素
# find_element_by_class_name(name) : 以類別名稱查找符合的元素
# find_element_by_tag_name("tag name") : 以html標籤查找符合的元素
# find_element_by_name(name) : 以名稱屬性查詢符合的元素
# find_element_by_link_text(text) : 以連結文字查詢符合的元素
# find_element_by_partial_link_text("text") : 以部分連結文字查詢符合的元素
# find_element_by_css_selector(selector) : 以CSS選擇器查詢符合的元素
# find_element_by_xpath() : 以XML的路徑查詢

# login_form = driver.find_element_by_id('loginForm')

# 測試登入FB
from selenium import webdriver

url = 'https://www.facebook.com/'
email = 'prophet0630@livemail.tw'
password = 'Boxbox7966'
driver = webdriver.Chrome()

# 取消alert視窗
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()
driver.get(url)
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_xpath('//*[@id="u_0_d_Y7"]').click()
driver.quit()



