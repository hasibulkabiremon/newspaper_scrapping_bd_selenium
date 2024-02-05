from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import messagebox

class CategoryGUI:
    def __init__(self, master, categories):
        self.master = master
        self.categories = categories
        self.create_widgets()

    def create_widgets(self):
        for x in self.categories:
            label = tk.Label(self.master, text=x['text'], cursor="hand2", fg="blue")
            label.bind("<Button-1>", lambda event, link=x['link']: self.open_link(link))
            label.pack(pady=5)

    def open_link(self, link):
        # messagebox.showinfo("Link Clicked", f"You clicked on: {link}")
        headline(link)

class HeadLineGUI:
    def __init__(self, master, categories):
        self.master = master
        self.categories = categories
        self.create_widgets()

    def create_widgets(self):
        for x in self.categories:
            label = tk.Label(self.master, text=x['text'], cursor="hand2", fg="blue")
            label.bind("<Button-1>", lambda event, link=x['link']: self.open_link(link))
            label.pack(pady=5)

    def open_link(self, link):
        # messagebox.showinfo("Link Clicked", f"You clicked on: {link}")
        news_Details(link)

class NewsDetailsGui:
    def __init__(self, master, author, date, news):
        self.master = master
        self.author = author
        self.date = date
        self.news = news
        self.create_widgets()

    def create_widgets(self):
        text = "Author: "+self.author + "\n" + self.date + "\n" + self.news
        label = tk.Label(self.master, text=text)
        label.pack(pady=5)
    

def main():
    category_driver = webdriver.Firefox()
    category_driver.minimize_window()
    category_driver.get("https://www.prothomalo.com/")

    category_elements = category_driver.find_elements(By.XPATH, "//li[@class='menu-item _1G1J7']/div/a")
    
    # Extracting text and link for each category
    categories = [{'text': x.text, 'link': x.get_attribute('href')} for x in category_elements]

    category_driver.close()

    root = tk.Tk()
    root.title("Clickable Categories")

    app = CategoryGUI(root, categories)

    root.mainloop()

def headline(headlineLink):
    headline_driver = webdriver.Firefox()
    headline_driver.get(headlineLink)
    print(headlineLink)
    headline_element = headline_driver.find_elements(By.XPATH,"//div[@class='Ib8Zz']/div/a")
    
    headlines = [{'text': h.get_attribute('aria-label'), 'link': h.get_attribute('href')} for h in headline_element]

    headline_driver.close()

    root = tk.Tk()
    root.title("Clickable Headlines")

    app = HeadLineGUI(root, headlines)
    root.mainloop()

def news_Details(newsLink):
    news_driver = webdriver.Firefox()
    news_driver.get(newsLink)
    news_author = news_driver.find_element(By.XPATH, "//span[@class='contributor-name _8TSJC ']").text
    news_time = news_driver.find_element(By.XPATH,"//div[@class='xuoYp']/time/span").text
    news_text = news_driver.find_element(By.XPATH,"//div[@class='story-element story-element-text']/div").text
    print(news_author, news_time, news_text)

    news_driver.close()
    root = tk.Tk()
    root.title("News Details")
    app = NewsDetailsGui(root,news_author,news_time,news_text)
    root.mainloop()

if __name__ == "__main__":
    main()

