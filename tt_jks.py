# -*- coding:utf-8 -*-
# @Time    : 2019/2/28 15:36
# @Author  : yuanjing liu
# @Email   : lauyuanjing@163.com
# @File    : tt_jks.py
# @Software: PyCharm

from flask import Flask
app = Flask(__name__)

@app.route("/test_jenkins/")
def avs_info():
    return " hello jenkins "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


