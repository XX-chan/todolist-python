# Flask-Todo 任务管理系统
基于 Flask、SQLite 和 JavaScript 开发的个人任务管理 Web 应用，用于练习用户认证、任务管理、数据库操作及前后端 API 交互。

## 项目功能

- 用户认证：支持用户登录，使用 Session 管理登录状态。
- 任务管理：支持任务的新增、查看、编辑、删除。
- 任务状态管理：支持标记任务完成状态。
- 数据持久化：使用 SQLite 存储用户和任务相关数据。
- 前后端交互：使用 JavaScript Fetch API 与 Flask 后端接口交互。用户可以登录- 系统并管理自己的待办事项，包括新增，删除，查看和完成任务。


## 技术栈
- 后端：Python、Flask
- 数据库：SQLite
- 前端：HTML、CSS、JavaScript
- 接口交互：Fetch API
- 开发环境：Python 虚拟环境


## 项目结构

```text
todolist-python/
├── app/                    # Flask 应用代码
│   └── __init__.py         # 应用初始化与应用工厂
├── data/                   # SQLite 数据库文件
│   ├── todos.db            # 任务数据
│   └── users.db            # 用户数据
├── notes/                  # 项目开发记录
│   └── TodoList-SQL V1版本记录.md
├── config.py               # 应用配置
├── run.py                  # 本地开发启动入口
├── wsgi.py                 # WSGI 应用入口
├── requirement.txt         # Python 依赖清单
├── .gitignore              # Git 忽略规则
└── README.md               # 项目说明文档
```


## 本地运行
1、克隆项目
```
git clone https://github.com/XX-chan/todolist-python.git
cd todolist-python
```

2、创建并启动虚拟环境

Linux/ WSL:
```
python3 -m venv venv
source venv/bin/activate
```

Windows:
```
python -m venv venv
venv\Scripts\activate
```

3、安装依赖
```
pip install -r requirements.txt
```

4、配置环境变量
在项目根目录创建`.env`文件，并设置应用所需的SECRET_KEY。

5、启动应用
```
venv/bin/python3 run.py
```

## 项目实践
通过该项目联系Flask Web应用开发，实践用户登录状态管理、数据库增删改查、接口交互及应用配置等基础开发流程。

## 测试账号

项目暂未实现用户注册功能，可使用以下测试账号体验：

- 用户名：`XX`
- 密码：`123`

启动项目后，访问 `http://127.0.0.1:5000`，使用上述账号登录。

注意：该账号仅用于本地项目体验，请勿用于生产环境。