# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 22:30:14 2019

@author: Sandeep Patel
"""

from bs4 import BeautifulSoup
import requests
import git
import os

DIR_PATH = r"C:\Users\Robodia\Desktop\aws\testgit"
if not os.path.exists(DIR_PATH):
    os.makedirs(DIR_PATH)

def page_scraped(dir_path):
    """
    args: dir_path for diecactry path witch store scraped file.
    veriables:
        page_link scrape link
        file_path File Path
    Scaped content from given url and store file in given path.
    """  
    page_link = "http://hck.re/tHEZGP"
    file_path = r"\scraped.txt"
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.text, "html.parser")
    with open(dir_path + file_path, 'tw') as file:
        file.write(page_content.get_text())    
    return True
            
def urls_scraped():
    """
    args: None
    veriables:
    page_link scrape link
    Scaped urls and store in list.
    return: urls list
    """ 
    urls = []
    page_link = "http://hck.re/crowdstrike"
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.text, "html.parser")
    a = page_content.find_all('td')
    for i in a:
        if 'http' in i.contents[0].strip():
            urls.append((i.contents[0].strip()))
    return urls


def git_pull_push(path, url):
    """
    args: path for git clone and url for repo url.
    
    
    """
    repo = git_clone(path, url)
    page_scraped(path)
    repo.git.checkout('HEAD', b='mostwanted')
    repo.git.for_each_ref()
    repo.index.add([path +r"\scraped.txt"])
    repo.index.commit('This commit form Sandeep Patel (mostwanted)')
    result = repo.git.push("origin", 'mostwanted')
    os.popen("rm -rf {}".format(DIR_PATH))  #Remove all the files 
    if result == '':
        return True
    return False
    

def git_clone(path, url):
    """
    args: path for git clone and url for repo url.
   
    Download the clone in given path
    
    return: repo object
    """
    repo = git.Repo.clone_from(url, path, branch='master')
    return repo
     
paths = urls_scraped()
for j in paths:
    git_pull_push(DIR_PATH, j)
