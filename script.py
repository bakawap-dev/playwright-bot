from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Chạy ẩn (bắt buộc)
        page = browser.new_page()
        
        page.goto("https://funlink.io/PF8n8vb")  # Thay link bạn muốn tự động hóa
        page.wait_for_timeout(5000)  # Chờ 5s
        print("Title:", page.title())  # In tiêu đề trang
        
        browser.close()

if __name__ == "__main__":
    run()
