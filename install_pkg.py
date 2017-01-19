# -*- coding: utf-8 -*-
"""
使用 `conda install` 命令安装必要的扩展包:
  1) selenium
  2) jupyter
  3) git
"""
from subprocess import check_call


def main():
    check_call('pip install selenium', shell=1)
    check_call('conda install -y jupyter git', shell=1)


if __name__ == '__main__':
    main()
