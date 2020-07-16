# オペレーティングシステムに依存した機能を使うための標準ライブラリ
import os
# システムに関する処理をまとめたライブラリ"sys"をインポート
import sys
# seleniumの読み込み
from selenium import webdriver
# オプションを使えるようにする
from selenium.webdriver.chrome.options import Options
# wait.until()関数の読み込み
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
# Select関数の読み込み
from selenium.webdriver.support.select import Select
# time関数の読み込み
import time


# 実行ファイルのあるディレクトリに新しい画像を作る
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/daily.png")

# Chromedriverをセットする
driver = webdriver.Chrome('./chromedriver.exe')
# スクショしたいURL
url = 'http://192.168.1.23:60001/sessions/new'
driver.get(url)


# IDの要素を指定
elem_id = driver.find_element_by_id('login_uid')
# IDを入力
elem_id.send_keys('root')
# パスワードの要素を指定
elem_password = driver.find_element_by_id('login_pwd')
elem_password.send_keys('root')

# ログインボタンの要素を指定
elem_login_btn = driver.find_element_by_name("commit")
# ログインボタンをクリック
elem_login_btn.click()

# キャンセルボタンの要素を指定
elem_cancel_btn = driver.find_element_by_id('cancel')
elem_cancel_btn.click()

# メディア管理の+ボタンの要素を指定
elem_media_expand = driver.find_element_by_id('main-node-8-e')
elem_media_expand.click()

wait = WebDriverWait(driver, 10)
# ATARA-MCCの+ボタンの要素を指定
element = wait.until(expected_conditions.visibility_of_element_located((By.ID, "main-node-8-aw_master_accounts_1-e")))
element.click()


wait = WebDriverWait(driver, 10)
# アカウントID：2535320560ボタンの要素を指定
element = wait.until(expected_conditions.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '2535320560')))
element.click()


wait = WebDriverWait(driver, 10)
# 標準レポートボタンの要素を指定
element = wait.until(expected_conditions.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '標準レポート')))
element.click()


wait = WebDriverWait(driver, 10)
# 先月の要素を指定
element = wait.until(expected_conditions.visibility_of_element_located((By.ID, 'reports-list_core-sub_period-period_between')))
# セレクトタグから先月を指定
text = "先月"
select = Select(element)
# 先月を選択
select.select_by_visible_text(text)


# ページサイズを取得する
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# ウィンドウのサイズを設定する
driver.set_window_size(w,h)

# スクショを撮る
driver.save_screenshot(filename)


# JSの処理が終わるまで5秒待つ
time.sleep(5)


wait = WebDriverWait(driver, 10)
# 条件詳細を開くボタンの要素を指定
element = wait.until(expected_conditions.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '条件詳細を開く')))
element.click()

wait = WebDriverWait(driver, 10)
# xxx別の要素を指定
element = wait.until(expected_conditions.visibility_of_element_located((By.ID, 'reports-list_core-control_dimension-aspect')))
# セレクトタグからキャンペーン別を指定
text = "キャンペーン別"
select = Select(element)
# キャンペーン別を選択
select.select_by_visible_text(text)



wait = WebDriverWait(driver, 10)
# 再表示ボタンの要素を指定
element = wait.until(expected_conditions.visibility_of_element_located((By.ID, 'reports-list_core-control-submit')))
element.click()


# JSの処理が終わるまで5秒待つ
time.sleep(5)

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/campaign.png")
driver.save_screenshot(filename)

# ブラウザを閉じる
# driver.quit()
