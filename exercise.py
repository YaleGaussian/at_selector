# -*- coding: utf-8 -*-
"""
开始练习前：
  1) 下载最新版的练习文件到目录 tutorial
  2) 运行本地网站服务器（默认端口 8080）
  3) 运行 jupyter notebook （默认端口 8888）
"""
import os
import time
from subprocess import check_call, Popen


workDir = os.path.abspath('tutorial/')


def pullRepository():
    if not os.path.isdir(workDir):
        check_call([
            'git', 'clone',
            'https://github.com/YaleGaussian/at_selector',
            workDir,
        ])
    else:
        old = os.getcwd()
        os.chdir(workDir)
        try:
            check_call(['git', 'pull'])
        finally:
            os.chdir(old)


def runWebServer():
    return Popen(['python', '-m', 'SimpleHTTPServer'], cwd=workDir)


def runNotebookServer():
    return Popen(['jupyter', 'notebook'], cwd=workDir)


def serve():
    ps = []

    # 强制结束子进程
    def _clean():
        while ps:
            try:
                ps.pop(0).kill()
            except:
                pass

    try:
        ps.append(runWebServer())
        ps.append(runNotebookServer())
    except:
        _clean()
        raise

    # 任一子进程退出，将导致本程序终止。
    exit = 0
    try:
        while not exit:
            time.sleep(1)
            for p in ps:
                if p.poll():
                    exit = 1
                    break
    finally:
        _clean()


def main():
    pullRepository()
    os.chdir(workDir)
    serve()


if __name__ == '__main__':
    main()
