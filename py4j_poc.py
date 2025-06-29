from py4j.java_gateway import JavaGateway

# 连接Java网关
gateway = JavaGateway()
hello_app = gateway.entry_point  # 获取Java对象

# 调用Java方法
result = hello_app.greet("Python")
print(result)  # 输出: Hello, Python from Py4J!
