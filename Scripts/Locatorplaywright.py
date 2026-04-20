import time
import re

from playwright.sync_api import Page , expect
#get by alt text locator
#alt by text
#getByRole()
#getBylabel()
#getByPlaceholder()
#getByTitle()
#getByTestId()

def test_verify_pwlocators(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    #time.sleep(5)
    page.wait_for_timeout(5000)
    
    #page.get_by_alt_text()
    logo = page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()
    
    #page.get_by_text()
    expect(page.get_by_text("Welcome to our store")).to_be_visible()#full text
    expect(page.get_by_text("Welcome to")).to_be_visible()#partial text
    
    #page.get_by_role()
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    expect (page.get_by_role("heading", name="Register" , exact=True)).to_be_visible()

   #page.get_by_label()
    page.goto("https://demo.nopcommerce.com/login?returnUrl=%2F")   
    page.get_by_label("Email:").fill("test@example.com")
   
    page.get_by_label("Password:").fill("test123") 
    
    #page.get_by_placeholder()
    page.goto("https://demo.nopcommerce.com/search") 
    page.get_by_placeholder("Search store").fill("test")

    #page.get_by_title()
    page.goto("https://demo.nopcommerce.com/")
    expect(page.get_by_title("nopCommerce demo store")).to_have_text("nopCommerce demo store")
    
    #page.get_by_test_id()
    page.goto("https://demo.nopcommerce.com/")
    expect(page.get_by_test_id("newsletter-email")).to_have_text("test@example.com")
    
    