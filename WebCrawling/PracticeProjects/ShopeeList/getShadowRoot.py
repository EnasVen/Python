import time


from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver



def run_chrome():
    # 建立 Chrome 設定
    options = selenium.webdriver.ChromeOptions()
    # 以無頭模式執行（不顯示視窗，於背景運作）
    # options.add_argument('--headless')
    # 以指定的視窗大小啟動瀏覽器
    # options.add_argument('--window-size=1920x980')
    # 以最大化視窗方式啟動瀏覽器
    options.add_argument('--start-maximized')
    # 以全螢幕方式啟動瀏覽器
    # options.add_argument('--kiosk')
    # 移除［Chrome 目前受到自動測試軟體控制］提示資訊列
    options.add_experimental_option('excludeSwitches', ['enable-automation'])



    # 以指定的設定啟動 Chrome
    browser = selenium.webdriver.Chrome(chrome_options=options)

    # 設定瀏覽器視窗在螢幕畫面上的位置
    # browser.set_window_position(0,0)
    # 設定瀏覽器視窗大小
    # browser.set_window_size(1920, 980)

    # 開啟網址
    browser.get('https://shopee.tw')

    # 視窗最大化
    browser.maximize_window()

    # 關閉ALERT
    # 嘗試取得商城活動提示的關閉按鈕（必須網頁全部渲染完成，元素已經存在才能取到） div.home-popup__content
    shadow_host = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'shopee-banner-popup-stateful'))
    )
    shadow_root = shadow_host.shadow_root
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'div.shopee-popup__close-btn')
    shadow_content.click()

    # 截圖網頁可視區域
    # browser.save_screenshot('shopee.png')
    time.sleep(20)
    # 關閉瀏覽器
    browser.quit()


if __name__ == '__main__':
    run_chrome()