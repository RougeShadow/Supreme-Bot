import selenium
from multiprocessing import Process, current_process
from selenium import webdriver
import select
from selenium.webdriver.support.ui import Select
import bs4
import requests
from selenium.webdriver.common.by import By
import webbrowser
import lxml
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
#each flag makes my program faster becausew there is less load for the cpu to deal with

headers = {"User-Agent": "Python"}
#who chrome thinks i am
browser = webdriver.Chrome(executable_path= "C:/Users/matth/Documents/year 12/Computing Y12/chromedriver_win32/chromedriver.exe")

res = requests.get('https://www.supremenewyork.com/shop/all', headers=headers)
page = bs4.BeautifulSoup(res.text, "lxml")
#i couldnt get it parse so i had to install the parser libary and put into LXML format so it was readable
article = page.findAll("div", class_='inner-article')
#The inner article holds the  names aswell as a bunch of useless informatioin
Links = []
Prodlist = []

def SupremeLinkGen(sectionLink,firstrun):

    res = requests.get(sectionLink, headers=headers)
    page = bs4.BeautifulSoup(res.text, "lxml")
    article = page.findAll("div", class_='inner-article')
    print(909090909909009)
    for i in article:
        children = i.findChildren("a" , recursive=True)
        counter = -1
        #we find the children of inner article so we get closer to just the link the children of inner article has the link aswell as a href and an image which we dont need
        children = str(children) # turns children into a string
        LinkBuild = "" #starts an empty sting
        #we start a new list to build a string of just the link without the useless information
        for i in range(28):
            #28 is how long the link string is
           counter = counter+1 #appends our own counter
           LinkBuild = LinkBuild +children[15+counter] # the link starts at the 15th index of the string

           if counter == 27:
               #we need the counter to know whemn to append it in and no further
            print("grabbed")
            Links.append(LinkBuild) #add the built link to the list
    print(909090909909009)
    with open("LINKS.txt","a") as Wrl:  #opens our links file
        print(firstrun)
        if firstrun == True:
            for i in Links:

                Wrl.write(i+"\n") #write the current link into the file
                print(i)
            print("First run")
            print(firstrun)
            return SupremeLinkGen(sectionLink, False) #starts the subroutine again with first run as false
            #fixed first subroutine not ending
    print("here1")
    Wrl.close()
    print('here2')
    with open("LINKS.txt","r") as Wrl:  #opens Links as reas only
        check = Wrl.readlines()  #cariable holds the lines and data on them
        print(check[0])
        print(Links[0]+"\n")
        if check[0] == Links[0]+"\n":  # compares the first old link with the first new link in the list and if they are the same
            print("no drop detected")
            SupremeLinkGen(sectionLink,False)  # starts the process over again as no drop was found
        print("here3")
        Del_List = [] # creates a list ready to fill with item
        if check[0] != Links[0]+"\n":
            print(Links[0]+"\n")
            print(check[0])
            print("drop detected")
            for i in range(len(Links)):
                if check[i] != Links[i]+"\n": #compares the current link with the old links
                    Links.append(Links[i]) #if they arent the same this is a new link add it to the list of valid new links
                    print(Links[i] + "\n")
                    print(check[i])
                    print("Reload")

                    print(1)
                else:
                    Del_List.append(i) # if they are the same put this in a list of old links
                    print("bang")
    Wrl.close()
    counter = 0
    for i in Del_List:
        print(Del_List)
        print(Del_List[counter])
        print(Links)
        Links.pop(int(Del_List[counter]))  # pops the link out of Del_List
        print("bang")
        print("val",Del_List[counter])
        print("precount",counter)
        counter =  +Del_List[counter]-counter # accoutnts for a shrink in the list that the pop created
        print("counter",counter)
    #shrunk as it popped

    print(Links)
    print("laaaaaa")
    return Links

def SupremeConnect(section):
    print(Links)
    Numb = len(Links)
    #for i in range(int((Numb/2))):
       # Links.pop(i)
    #print(Links)
    for i in range(len(Links)):
        print("Loading...")
        #we use the built links to find the product we are looking for
        connect = 'https://www.supremenewyork.com/shop'+str(Links[i])
        print(connect)
        res = requests.get(connect, headers=headers)
        prodpage = bs4.BeautifulSoup(res.text, "lxml")
        Product = prodpage.find("title")

        # do a while loop that breaks if < is found
        Product = str(Product)
        ProdBuild = ""

        X = True
        try:

            while X == True:
                for i in range(100000):

                    ProdBuild =  ProdBuild + Product[15+i]
                    #printed the same as the way i build links
                    if Product[15+i] == "<":
                        Prodlist.append(ProdBuild)
                        break
                        #tried to break it with X = false but it woudlnt do so since that doesnt break the for i in range  loop
                X = False
                #put it outside of column so the loop would properly break
        except:
            print("End")
            print(Prodlist)
            print(ProdBuild)
            break

    return Prodlist

def ProdInspect(Prodlist1,item1,Links1,CardNumber,cvv,exp,email,password):
    print(browser.current_url)
    print(2)
    #seemed like it was fine so we added the 2 for error checking
    print(Prodlist1)

    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')
    #connect = "https://chrome.google.com/sync"
    #browser.get(connect)
    #browser.find_element_by_id("identifierId").send_keys(email)
    #browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div").click()
    #X = True
    #while X == True:
    #    try:
    #        browser.find_element_by_name("password").send_keys(password)
    #        X = False
    #    except:
    #        print("loading")
    #browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div").click()
    #browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div").click()
    #use enter if it doesnt work

    #
    for i in range(len(Prodlist1)):
        print(Prodlist1[i])
        print(" "+item1+"<")
        #the problem was that i copied and pasted the item lacked the < character all the ones in the list had
        #Then it required a fingerspace because thats what everysingle one in the list had had

        if Prodlist1[i] == " "+item1+"<":
            print("Loading...")
            print("code 1111")
            connect = 'https://www.supremenewyork.com/shop' + str(Links1[i])
            print(connect)
            res = requests.get(connect, headers=headers)
            prodpage = bs4.BeautifulSoup(res.text, "lxml")
            browser.get(connect)
            browser.find_element_by_name("commit").click()
            button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/a[2]')))
            button.click()
            #this was one because it takes a second to become clickable
            print(1)
            print(browser.current_url)
            print(1)
            browser.find_element_by_id("cnb").send_keys(CardNumber)
            dropdown = Select(browser.find_element_by_name("credit_card[month]"))
            dropdown.select_by_value(exp[0] + exp[1])
            dropdown = Select(browser.find_element_by_name("credit_card[year]"))
            dropdown.select_by_value("20" + exp[3] + exp[4])
            browser.find_element_by_name("credit_card[ovv]").send_keys(cvv)

            browser.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p/label").click()
            browser.find_element_by_name("commit").click()
            # wasnt sure if it worked so i used this
            Success = browser.find_element_by_tag_name("p")
            check = Success.text
            print(check)


#def sup_checkout(CardNumber,Expiry):
 #       print(browser.current_url)
  #      print(1)
   #     browser.find_element_by_id("cnb").send_keys(CardNumber)
    #    dropdown = Select(browser.find_element_by_name("credit_card[month]"))
     #   dropdown.select_by_value(exp[0]+exp[1])
      #  dropdown = Select(browser.find_element_by_name("credit_card[year]"))
       # dropdown.select_by_value("20"+exp[3] + exp[4])
        #browser.find_element_by_name("credit_card[ovv]").send_keys(cvv)

        #browser.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p/label").click()
        #browser.find_element_by_name("commit").click()
        #wasnt sure if it worked so i used this
        #Success = browser.find_element_by_tag_name("p")
        #check = Success.text
        #print(check)


    #I had to select the box and then use the select libary to select what is visible
def Starti():
    input("start")
    if Choice == "supreme":

        section_c = input("type the section your looking for like jacket please type this in lower case")
        category_Link = 'https://www.supremenewyork.com/shop/all/'+section_c
        Links.append(SupremeLinkGen(category_Link,True))
        SupremeConnect(section_c)
        for i in range(2):
          process1 = Process(target=ProdInspect,args=(Prodlist,item,Links,cn,cvv,exp,email,password))
          #process2 = Process(target=sup_checkout,args=(cn,exp))
          processes1.append(process1)
          #processes2.append(process2)
          process1.start()
          #for process1 in processes1:
           #   process1.join()
          #print("first process complete")
          #process2.start()
          #for process2 in processes2:
           #   process2.join()
         # print("second process complete")


if __name__ == '__main__':
    email = input("Email:")
    password = input("Password:")
    processes1 = []
    processes2 = []
    Choice = "supreme"
    item = input("Enter an item such as Raglan Court Jacket - Black")
    cn = input("Card Number")
    exp = input("expiration date")
    cvv = input("CVV:")
    TaskN = 50
    Starti()


# Big Letter Track Jacket - Dark Orange<
#4751 4203 9868 4808
#had to use hex editor to take out the cdc as browsers look for that in the code to see if it is automated
#MAKE IT INT O TABS NOT SEPERATE WINDOWS
#current time with 2 windows running 20 seconds
#Technical Field Jacket - Black
#Hooded Facemask Parka - Tigerstripe Camo