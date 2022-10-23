from tkinter import *
from django.http import response
import requests
from tkinter import messagebox
root = Tk()
root.title('News App')
root.geometry('1700x500')
def fetchcountrycode():
    countryName = country_text.get()
    response = requests.get("https://api.printful.com/countries")
    data = response.json()
    results = data["result"]
    cc = 'none'
    for r in results:
        if r['name'].lower() == countryName.lower():
            cc = r['code']

    if cc == 'none' :
        messagebox.showerror('Error :(', 'country is not found {}'.format(countryName))
    else:
        print(cc)
        fetchNews(cc)

def fetchNews(cc):
    url = "https://newsapi.org/v2/top-headlines?country="+ cc +"&apiKey=3ed8c02dfc00453fa5ec3d4960e8dfeb"
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    allTitles = ''
    for r in articles:
        allTitles = allTitles+r['title']+'\n'+'\n'
    news.config(text = allTitles)
country_text = StringVar()
country = Entry(root,textvariable = country_text)
country.pack()
searchButton = Button(root,text = "Get News",width=12, command= fetchcountrycode)
searchButton.pack()
news = Label(root,text = '',font = ('bold',11), )
news.pack()

root.mainloop()