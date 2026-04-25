from playwright.sync_api import sync_playwright

class BrowserController:
    def __init__(self):
        self.pw = sync_playwright().start()

        # 🔥 FIREFOX FORCÉ
        self.browser = self.pw.firefox.launch(headless=False)

        self.context = self.browser.new_context()
        self.pages = []

    def open(self, url: str):
        page = self.context.new_page()
        page.goto(url)
        self.pages.append(page)
        return f"Ouvert sur Firefox: {url}"

    def find_tab(self, keyword: str):
        keyword = keyword.lower()

        for page in self.pages:
            try:
                if keyword in page.url.lower():
                    return page
            except:
                pass

        return None

    def close_tab(self, keyword: str):
        page = self.find_tab(keyword)

        if page:
            page.close()
            self.pages.remove(page)
            return f"Tab '{keyword}' fermé"

        return f"Aucun tab {keyword}"

    def close_all(self):
        for p in self.pages:
            p.close()
        self.pages = []
        return "Tous les onglets fermés"


# 🔥 INSTANCE EXPORTÉE
browser = BrowserController()