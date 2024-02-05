import tkinter as tk
from tkinter import ttk
import subprocess

def call_prothom_alo():
    subprocess.run(["python", "prothom_alo.py"])

def call_ittefaq():
    subprocess.run(["python", "ittefaq.py"])

def call_kaler_kontho():
    subprocess.run(["python", "kalerKontho.py"])

def call_news_bangladesh_protidin():
    subprocess.run(["python", "news_bangladesh_protidin.py"])

def call_news_new_diganta():
    newspaper_url = "https://www.dailynayadiganta.com/"
    category_xpath = "//a[@class='dropdown-toggle' or @data-toggle]"
    headline_xpath = "//*[@class='row news-list']/div[2]/a"
    news_author_xpath = "//ul[@class='list-inline']/li[1]"
    news_time_xpath = "//ul[@class='list-inline']/li[2]"
    news_text_xpath = "//*[@class='news-content']"
    subprocess.run(["python", "paper.py",newspaper_url,category_xpath,headline_xpath,news_author_xpath,news_time_xpath,news_text_xpath])


def call_news_amar_songbad():
    newspaper_url = "https://www.amarsangbad.com/"
    category_xpath = "//ul[contains(@class,'nav') ]/li/a"
    headline_xpath = "//div[contains(@class,'category-lead-news')]/a[1]"
    news_author_xpath = "//div[@class='post-text']/p"
    news_time_xpath = "//div[@class='post-text']/p[2]"
    news_text_xpath = "//*[@class='content-details']"
    subprocess.run(["python", "paper.py",newspaper_url,category_xpath,headline_xpath,news_author_xpath,news_time_xpath,news_text_xpath])

# Create the main window
root = tk.Tk()
root.title("News Source Caller")

# Create buttons to call each news source
prothom_alo_button = ttk.Button(root, text="Prothom Alo", command=call_prothom_alo)
prothom_alo_button.pack(pady=10)

ittefaq_button = ttk.Button(root, text="Ittefaq", command=call_ittefaq)
ittefaq_button.pack(pady=10)

kaler_kontho_button = ttk.Button(root, text="Kaler Kontho", command=call_kaler_kontho)
kaler_kontho_button.pack(pady=10)

protidin_button = ttk.Button(root, text="News Bangladesh Protidin", command=call_news_bangladesh_protidin)
protidin_button.pack(pady=10)

protidin_button = ttk.Button(root, text="নয়া দিগন্ত", command=call_news_new_diganta)
protidin_button.pack(pady=10)

protidin_button = ttk.Button(root, text="আমার সংবাদ", command=call_news_amar_songbad)
protidin_button.pack(pady=10)





# Run the GUI
root.mainloop()


