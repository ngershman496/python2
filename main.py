# Implement the ‘selenium’ module
# Ask the user for a website url (limit format to ‘www.<url>.com’)
# Use selenium to launch the firefox browser
# Navigate to the input url

from selenium import webdriver

def geturl():
    valid = False
    while valid == False:
        domain = input("Enter the desired site (www.<site>.com): ")
        print()
        if "www." in domain and ".com" in domain:
            return "https://" + domain
        else:
            valid = False

def view(url):
    browser = webdriver.Firefox()
    browser.get(url)
    resp = 0
    while resp == 0:
        resp = input("Press '1' to close ")

if __name__ == "__main__":
    print("geckodriver.exe is needed to run this program.\n"+
          "This can be downloaded at 'https://github.com/mozilla/geckodriver/releases'\n+"
          "Please download for your current OS")
    url = geturl()
    view(url)

