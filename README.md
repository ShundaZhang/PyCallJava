## README in English:

---

It is feasible to call Java library functions in Python. Common methods include using the **JPype** or **Py4J** libraries. Below are examples of both approaches:

---

### Method 1: Using JPype (Recommended)  
**Principle**: Starts a JVM within the Python process to directly call Java classes.

#### Steps:  
1. **Install JPype**:  
   ```bash
   pip install JPype1
   ```

2. **Write Java class** (Save as `HelloWorld.java`):  
   ```java
   public class HelloWorld {
       // Static method
       public static String greetStatic(String name) {
           return "Hello, " + name + " (Static)";
       }
       
       // Instance method
       public String greetInstance(String name) {
           return "Hello, " + name + " (Instance)";
       }
   }
   ```

3. **Compile Java class**:  
   ```bash
   javac HelloWorld.java
   ```

4. **Python calling code**:  
   ```python
   import jpype

   # Start JVM (specify Java classpath)
   jpype.startJVM(classpath=['.'])  # '.' represents current directory

   # Import Java class
   HelloWorld = jpype.JClass("HelloWorld")

   # Call static method
   print(HelloWorld.greetStatic("Python"))  # Output: Hello, Python (Static)

   # Create instance and call method
   hello_obj = HelloWorld()
   print(hello_obj.greetInstance("World"))  # Output: Hello, World (Instance)

   # Shutdown JVM
   jpype.shutdownJVM()
   ```

---

### Method 2: Using Py4J  
**Principle**: Java side starts a gateway service, Python calls via TCP connection.

#### Steps:  
1. **Install Py4J**:  
   ```bash
   pip install py4j
   ```

2. **Write Java gateway program** (Save as `HelloWorldServer.java`):  
   ```java
   import py4j.GatewayServer;

   public class HelloWorldServer {
       public String greet(String name) {
           return "Hello, " + name + " from Py4J!";
       }
       
       public static void main(String[] args) {
           GatewayServer server = new GatewayServer(new HelloWorldServer());
           server.start();
           System.out.println("Gateway Server Started");
       }
   }
   ```

3. **Compile and run Java program** (Ensure `py4j.jar` is in classpath):  
   ```bash
   javac -cp py4j0.10.9.9.jar HelloWorldServer.java  # Version must match
   jar cf HelloWorldServer.jar HelloWorldServer.class
   java -cp .:py4j0.10.9.9.jar HelloWorldServer
   ```

4. **Python calling code**:  
   ```python
   from py4j.java_gateway import JavaGateway

   # Connect to Java gateway
   gateway = JavaGateway()
   hello_app = gateway.entry_point  # Get Java object

   # Call Java method
   result = hello_app.greet("Python")
   print(result)  # Output: Hello, Python from Py4J!
   ```

---

### Key Differences:  
| **Feature**       | **JPype**                          | **Py4J**                     |
|-------------------|------------------------------------|------------------------------|
| **Communication** | In-process calls                   | TCP (cross-process)          |
| **Performance**   | Higher (no network overhead)       | Lower (network latency)      |
| **Deployment**    | Simple (Python only)               | Requires separate Java server|
| **Use Case**      | Tightly integrated lightweight calls | Distributed/microservices    |

Choose the appropriate method based on requirements. For simple integration, **JPype** is recommended; for distributed scenarios, consider **Py4J**.

---

## README in Chinese:

---

在Python中调用Java库的函数，常用的方法有使用**JPype**或**Py4J**库。下面分别提供两种方法的示例：

---

### 方法1：使用 JPype（推荐）
**原理**：在Python进程中启动JVM，直接调用Java类。

#### 步骤：
1. **安装JPype**：
   ```bash
   pip install JPype1
   ```

2. **编写Java类**（保存为 `HelloWorld.java`）：
   ```java
   public class HelloWorld {
       // 静态方法
       public static String greetStatic(String name) {
           return "Hello, " + name + " (Static)";
       }
       
       // 实例方法
       public String greetInstance(String name) {
           return "Hello, " + name + " (Instance)";
       }
   }
   ```

3. **编译Java类**：
   ```bash
   javac HelloWorld.java
   ```

4. **Python调用代码**：
   ```python
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
   ```

---

### 方法2：使用 Py4J
**原理**：Java端启动网关服务，Python通过TCP连接调用。

#### 步骤：
1. **安装Py4J**：
   ```bash
   pip install py4j
   ```

2. **编写Java网关程序**（保存为 `HelloWorldServer.java`）：
   ```java
   import py4j.GatewayServer;

   public class HelloWorldServer {
       public String greet(String name) {
           return "Hello, " + name + " from Py4J!";
       }
       
       public static void main(String[] args) {
           GatewayServer server = new GatewayServer(new HelloWorldServer());
           server.start();
           System.out.println("Gateway Server Started");
       }
   }
   ```

3. **编译并运行Java程序**（确保 `py4j.jar` 在类路径中）：
   ```bash
   javac -cp py4j0.10.9.9.jar HelloWorldServer.java  # 版本号需匹配
   jar cf HelloWorldServer.jar HelloWorldServer.class
   java -cp .:py4j0.10.9.9.jar HelloWorldServer
   ```

4. **Python调用代码**：
   ```python
   from py4j.java_gateway import JavaGateway

   # 连接Java网关
   gateway = JavaGateway()
   hello_app = gateway.entry_point  # 获取Java对象

   # 调用Java方法
   result = hello_app.greet("Python")
   print(result)  # 输出: Hello, Python from Py4J!
   ```

---

### 关键区别：
| **特性**       | **JPype**                          | **Py4J**                     |
|----------------|-----------------------------------|------------------------------|
| **通信方式**   | 同一进程内调用                   | TCP通信（跨进程）           |
| **性能**       | 更高（无网络开销）               | 较低（网络延迟）           |
| **部署复杂度** | 简单（只需Python环境）           | 需单独启动Java服务         |
| **适用场景**   | 紧密集成的轻量级调用             | 独立进程/微服务架构        |

根据需求选择合适的方式。对于简单集成推荐使用 **JPype**，分布式场景可选 **Py4J**。
