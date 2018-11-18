# my_django 目录结构
    django常用命令
    - django-admin startproject 项目名称 #创建django项目
    - python manage.py runserver 启动开发服务器   #启动服务器
    - python manage.py startapp app名称 #创建django APP
    - python manage.py migrate  #创建数据表并执行对应的SQL语句（将操作同步到数据库）
    - python manage.py makemigrations app名称 #通过运行makemigrations命令，相当于告诉Django你对模型有改动，并且你想把这些改动保存为一个“迁移(migration)”。
    - python manage.py sqlmigrate app名称 0001 #展示SQL语句
    
    django目录结构
    - my_django 外层的mysite/目录与Django无关，只是你项目的容器，可以任意命名
        - **myAPP** #利用Django创建的app 
            - migrations #用来初始化数据库，在执行python manage.py makemigrations 的时候会自动生成一个文件在这里
                - __init__.py #一个定义包的空文件。
            - __init__.py #一个定义包的空文件。
            - admin.py #Django自带了一个管理界面，这个文件可以注册model在界面中管理
            - apps.py #配置当前APP
            - models.py #在这个文件里面定义model类
            - tests.py #写测试代码
            - views.py #视图，Django映射urls.py里面的url的时候，在views.py里面查找对应的处理方法   
        - **myDango** #利用Django创建的project
            - __init__.py #一个定义包的空文件。
            - settings.py #项目的主配置文件，非常重要
            - urls.py #路由文件，所有的任务都是从这里开始分配，相当于Django驱动站点的内容表格，非常重要！
            - wsgi.py #一个基于WSGI的web服务器进入点，提供底层的网络通信功能，通常不用关心。           
        - **db.sqlite3** #    
        - **manage.py** #一个命令行工具，用于与Django进行不同方式的交互脚本，非常重要！
    