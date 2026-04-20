from playwright.sync_api import Page , expect


def test_verifyPageUrl(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    myurl=page.url
    print("Url is ",myurl)
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/")
   
   
    
def test_verifyTitle(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    title = page.title()
    print("Title is ",title)

    expect(page).to_have_title("Automation Testing Practice") 