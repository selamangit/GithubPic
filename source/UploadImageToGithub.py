import os
import re
import os.path as path
import subprocess
import time 
import shutil


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    stamp = ("".join(time_stamp.split()[0].split("-"))+"".join(time_stamp.split()[1].split(":"))).replace('.', '')
    return stamp

def runcmd(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    command_output = process.stdout.read().decode('utf-8')
    return command_output

def get_md_file():
    Markdown_dir = r"D:\Project\Github.io\记事本\学习笔记"
    md_file_paths = list()
    if path.isdir(Markdown_dir):
        dir_list = os.listdir(Markdown_dir)
    for i in dir_list:
        if(path.isdir(os.path.join(Markdown_dir,i))):
            files = os.listdir(os.path.join(Markdown_dir,i))
            for j in files:
                md_file_path = os.path.join(os.path.join(Markdown_dir,i),j)
                md_file_paths.append(md_file_path)
    return md_file_paths

def sub_image_path():
    md_file_paths = get_md_file()
    for i in md_file_paths:
        contents = []
        print(i)
        with open (i , 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                # 能完整匹配出img路径的匹配对象
                searchObj = re.search(r'<img src\s?=\s?"(.*?)".*>', line, re.M|re.I)
                searchObj1 = re.search(r'!\[.*\]\((.*)\)',line, re.M|re.I)
                abspath = None
                if searchObj:
                    if(os.path.isabs(searchObj.group(1))):
                        abspath = searchObj.group(1)
                        if(os.path.exists(abspath)):
                            print(abspath)

                            time_stamp = get_time_stamp()
                            shutil.copyfile(abspath,"./temp_images/%s.png"%time_stamp)
                            image = "./temp_images/%s.png"%time_stamp
                            command = " picgo u %s"%image
                            url = runcmd(command)
                            searchObj = re.search('(http.*?png)',url)

                            result = re.sub(r'(!\[.*\]\()(.*?)(\))',r"\1%s\3"%searchObj.group(0),line)
                            contents.append(result)
                    elif(re.match(r'^https?:/{2}\w.+$', searchObj.group(1))):
                        print("这是超链接")
                        contents.append(line)
                    else:
                        abspath = os.path.join(os.path.dirname(i),searchObj.group(1))
                        if(os.path.exists(abspath)):
                            print(abspath)

                            time_stamp = get_time_stamp()
                            shutil.copyfile(abspath,"./temp_images/%s.png"%time_stamp)
                            image = "./temp_images/%s.png"%time_stamp
                            command = " picgo u %s"%image
                            url = runcmd(command)
                            searchObj = re.search('(http.*?png)',url)
                            result = re.sub(r'(img src\s?=\s?")(.*?)(")',r"\1%s\3"%searchObj.group(0),line)
                            contents.append(result)
                elif searchObj1:
                    if(os.path.isabs(searchObj1.group(1))):
                        abspath = searchObj1.group(1)
                        if(os.path.exists(abspath)):
                            print(abspath)

                            time_stamp = get_time_stamp()
                            shutil.copyfile(abspath,"./temp_images/%s.png"%time_stamp)
                            image = "./temp_images/%s.png"%time_stamp
                            command = " picgo u %s"%image
                            url = runcmd(command)
                            searchObj = re.search('(http.*?png)',url)

                            result = re.sub(r'(!\[.*\]\()(.*?)(\))',r"\1%s\3"%searchObj.group(0),line)
                            contents.append(result)
                    elif(re.match(r'^https?:/{2}\w.+$', searchObj1.group(1))):
                        contents.append(line)
                        print("这是超链接")
                    else:
                        abspath = os.path.join(os.path.dirname(i),searchObj1.group(1))
                        if(os.path.exists(abspath)):
                            print(abspath)
                            time_stamp = get_time_stamp()
                            shutil.copyfile(abspath,"./temp_images/%s.png"%time_stamp)
                            image = "./temp_images/%s.png"%time_stamp
                            command = " picgo u %s"%image
                            url = runcmd(command)
                            searchObj = re.search('(http.*?png)',url)

                            result = re.sub(r'(!\[.*\]\()(.*?)(\))',r"\1%s\3"%searchObj.group(0),line)
                            contents.append(result)
                else:
                    contents.append(line)
            f.close()
        with open(i , 'w+', encoding='utf-8') as f:
            for j in contents:
                f.write(j)
            f.close()
        contents.clear()
if __name__ == '__main__':
    sub_image_path()