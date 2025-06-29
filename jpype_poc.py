import jpype

# 启动JVM（指定Java类路径）
jpype.startJVM(classpath=['.'])  # '.' 表示当前目录

# 导入Java类
HelloWorld = jpype.JClass("HelloWorld")

# 调用静态方法
print(HelloWorld.greetStatic("Python"))  # 输出: Hello, Python (Static)

# 创建实例并调用方法
hello_obj = HelloWorld()
print(hello_obj.greetInstance("World"))  # 输出: Hello, World (Instance)

# 关闭JVM
jpype.shutdownJVM()
