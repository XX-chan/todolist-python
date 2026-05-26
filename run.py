from app import create_app

# 开发环境启动入口

# 创建Flask app
app=create_app()


# 只有被自己运行时才启动服务器
if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])