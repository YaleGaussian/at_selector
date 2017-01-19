本文档旨在帮助 "python 自动化测试" 初学者练习如何定位各种元素。

# 搭建练习环境（首次使用）

## 准备一台 Windows 7 64 位电脑或者虚拟机

## 安装浏览器及驱动
### 安装 Chrome 和 Firefox 浏览器

### 安装浏览器驱动
* Chrome, https://sites.google.com/a/chromium.org/chromedriver/downloads
* Firefox, https://github.com/mozilla/geckodriver/releases

### 设置环境变量
必须把浏览器驱动文件 chromedriver.exe 和 geckodriver.exe 所在目录加入 Path
环境变量。

## 安装 Miniconda python 2.7
下载地址 http://conda.pydata.org/miniconda.html

## 在开始菜单找到 conda prompt，单击它打开 conda 命令窗口

## 在 conda 命令窗口依次输入下列命令
* 安装 selenium 包
```
conda install selenium
```

* 安装 jupyter 包
```
conda install jupyter
```

* 创建工作目录 tutorial 文件夹
```
mkdir tutorial
cd tutorial
```

* 启动 jupyter (按 Ctrl + c 关闭)
```
jupyter notebook
```

## 测试环境是否就绪
下载 test-env.ipynb 到工作目录，刷新 jupyter 列表后打开 test-env.ipynb，按其说明进行环境测试。

在线浏览 http://nbviewer.jupyter.org/github/YaleGaussian/at_selector/blob/master/test-env.ipynb
