'''
tag id
tag class
tag attribute
tag class attribute

'''


import pytest
from playwright.sync_api import Page , expect


def test_verify_csslocators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
   
   #tag id 
    page.locator("input#small-searchterms").fill("test")
    expect(search_box).to_have_value("test")
    
    page.wait_for_timeout(5000)
    
    #tag class
    
    page.locator("input.search-box-text").fill("test")
    page.wait_for_timeout(5000)
    
    #tag attribute   
    page.locator("input[type='text']").fill("test")
    #or
    page.locator("[name='q']").fill("test")
     
     #tag class attribute
    page.locator("input.search-box-text[value='search']").fill("test")
      #or
      
    page.locator(".search-box-text[value='search']").fill("test")