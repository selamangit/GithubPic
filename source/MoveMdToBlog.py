import os
import shutil
import re
from turtle import title

template = """---
title:{}
categories:{}
tag:{}
mathjax: true
---
"""

def get_md_file():
    Markdown_dir = r"D:\Project\Github.io\记事本\学习笔记"
    md_file_paths = list()
    if os.path.isdir(Markdown_dir):
        dir_list = os.listdir(Markdown_dir)
    for i in dir_list:
        if(os.path.isdir(os.path.join(Markdown_dir,i))):
            files = os.listdir(os.path.join(Markdown_dir,i))
            for j in files:
                md_file_path = os.path.join(os.path.join(Markdown_dir,i),j)
                md_file_paths.append(md_file_path)
    return md_file_paths

def add_title():
    md_file_paths = get_md_file()
    for i in md_file_paths:
        result = os.path.split(i)
        categories = i.split('\\')[-2]
        (filename,ext) = os.path.splitext(result[1])
        tag = ''
        title = ''
        searchObj = re.search(r'\[(.*)\](.*)', filename, re.M|re.I)
        if searchObj:
            tag = searchObj.group(1)
            title = searchObj.group(2)
        else:
            title = filename
            tag = ''

        with open(i,'r+',encoding='utf-8') as f:
            old = f.read()
            f.seek(0)
            f.write(template.format(' '+title,' '+categories,' '+tag))
            f.write(old)
            f.close()

def move_md():
    md_file_paths = get_md_file()   
    for i in md_file_paths:
        result = os.path.split(i)
        filename = i.split('\\')[-1]
        shutil.copyfile(i,r"D:\Project\Github.io\GithubBlog\source\_posts\%s"%filename)

if __name__ == '__main__':
    add_title()
    move_md()