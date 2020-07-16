# seleniumの読み込み
from selenium import webdriver
# Chromeが自動で立ち上がる
browser = webdriver.Chrome('chromedriver.exe')
# ログイン練習サイトにアクセス
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
# IDの要素を指定
elem_username = browser.find_element_by_id('username')
# IDを入力
elem_username.send_keys('fickle')
# パスワードの要素を指定
elem_password = browser.find_element_by_id('password')
# パスワードを入力
elem_password.send_keys('makelove')
# ログインボタンの要素を指定
elem_login_btn = browser.find_element_by_id('login-btn')
# ログインボタンをクリック
elem_login_btn.click()
# ブラウザを閉じる
browser.quit()
