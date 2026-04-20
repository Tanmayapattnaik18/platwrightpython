
import pytest
from playwright.sync_api import Page , expect

def test_verify_xpathlocators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    
    #tag
    page.locator("//input").fill("test")
    expect(page.locator("//input")).to_have_value("test")
    
    page.wait_for_timeout(5000)
    
    #tag attribute
    page.locator("//input[@id='small-searchterms']").fill("test")
    expect(page.locator("//input[@id='small-searchterms']")).to_have_value("test")
    
    page.wait_for_timeout(5000)
    
    #tag class attribute
    page.locator("//input[@class='search-box-text']").fill("test")
    expect(page.locator("//input[@class='search-box-text']")).to_have_value("test")
    
    #absolute xpath
    page.locator("/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/form/input").fill("test")
    expect(page.locator("/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/form/input")).to_have_value("test")
    
    #relative xpath
    page.locator("//form/input").fill("test")
    expect(page.locator("//form/input")).to_have_value("test")      
    
    #contains
    products = page.locator("//h2//a[contains(@href, '/books')]")
    products_count = products.count()
    print("products_count:", products_count)
    expect(products).to_have_count(products_count)


    print("First computer product:", products.first.text_content())
    print("Last computer product:", products.last.text_content())
    print("N-th computer product:", products.nth(3).text_content())    
    