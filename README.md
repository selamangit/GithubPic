# GithubPic
用于存放博客图片
- [x] 本地存储的图片上传
## source
* `source/MoveMdToBlog.py`
* `source/UploadImageToGithub.py`

`UploadImageToGithub.py`：主要使用正则表达式能过滤超链，处理本地图片并上传  
`MoveMdToBlog`：在配置好typora上传规则之后后面更新笔记就只需要使用这个即可

>~~`MoveMdToBlog`还需要过滤掉已经处理过的title~~  
考虑更改title