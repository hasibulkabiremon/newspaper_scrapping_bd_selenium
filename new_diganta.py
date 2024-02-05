from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

class CategoryGUI:
    def __init__(self, master, categories):
        self.master = master
        self.categories = categories
        self.create_widgets()

    def create_widgets(self):
        # Create a canvas to hold the labels
        canvas = tk.Canvas(self.master, bg="white")
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        # Create a frame inside the canvas
        frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=frame, anchor=tk.NW)

        # Add labels to the frame
        for x in self.categories:
            label = tk.Label(frame, text=x['text'], cursor="hand2", fg="blue")
            label.bind("<Button-1>", lambda event, link=x['link']: self.open_link(link))
            label.pack(pady=5)

        # Add a scrollbar to the canvas
        scrollbar = tk.Scrollbar(self.master, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.config(yscrollcommand=scrollbar.set)

        # Configure the canvas to update scroll region when labels are added
        frame.bind("<Configure>", lambda event, canvas=canvas: self.on_frame_configure(canvas))

    def on_frame_configure(self, canvas):
        # Update scroll region to fit the frame size
        canvas.configure(scrollregion=canvas.bbox("all"))

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
    category_driver.get("https://www.dailynayadiganta.com/")

    category_elements = category_driver.find_elements(By.XPATH, "//a[@class='dropdown-toggle' or @data-toggle]")
    print(len(category_elements))

    # Extracting text and link for each category
    categories = [{'text': x.get_attribute('text'), 'link': x.get_attribute('href')} for x in category_elements]

    category_driver.close()

    root = tk.Tk()
    root.title("Clickable Categories")

    app = CategoryGUI(root, categories)

    root.mainloop()

def headline(headlineLink):
    headline_driver = webdriver.Firefox()
    headline_driver.get(headlineLink)
    print(headlineLink)
    head_xpath = "//*[@class='row news-list']/div[2]/a"
    headline_element = headline_driver.find_elements(By.XPATH, head_xpath)
    
    headlines = [{'text': h.get_attribute('text'), 'link': h.get_attribute('href')} for h in headline_element]

    headline_driver.close()

    root = tk.Tk()
    root.title("Clickable Headlines")

    app = HeadLineGUI(root, headlines)
    root.mainloop()

def news_Details(newsLink):
    news_driver = webdriver.Firefox()
    news_driver.get(newsLink)
    news_author = news_driver.find_element(By.XPATH, "//ul[@class='list-inline']/li[1]").text
    news_time = news_driver.find_element(By.XPATH,"//ul[@class='list-inline']/li[2]").text
    news_text = news_driver.find_element(By.XPATH,"//*[@class='news-content']").text
    print(news_author, news_time, news_text)

    news_driver.close()
    root = tk.Tk()
    root.title("News Details")
    app = NewsDetailsGui(root,news_author,news_time,news_text)
    root.mainloop()

if __name__ == "__main__":
    main()

