#!/usr/bin/python
#encoding=utf8

# 创建一个独立的 :virtualenv --no-site-packages venv
# 新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用source进入该环境：
# 了venv这个Python环境，可以用source进入该环境 : source venv/bin/activate

# 在venv环境下，用pip安装的包都被安装到venv这个环境下，
# 系统Python环境不受任何影响。也就是说，venv环境是专门针对myproject这个应用创建的。

# 退出当前的venv环境，使用deactivate命令：