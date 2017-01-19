## 搭建练习环境（首次使用）

1. 准备一台 Windows 7 64 位电脑或者虚拟机

2. 安装浏览器及驱动
  1. 安装 Chrome 和 Firefox 浏览器

  2. 安装浏览器驱动
    * Chrome, https://sites.google.com/a/chromium.org/chromedriver/downloads
    * Firefox, https://github.com/mozilla/geckodriver/releases

  3. 设置环境变量
    必须把浏览器驱动文件 chromedriver.exe 和 geckodriver.exe 所在目录加入 Path 环境变量。

3. 安装 Miniconda python 2.7
  下载地址 http://conda.pydata.org/miniconda.html

4. 安装其他软件包
  下载 https://github.com/YaleGaussian/at_selector/raw/master/init.bat 到当前目录，
  在开始菜单找到 conda prompt（命令窗口），打开后输入下列命令
```
init.bat
```
