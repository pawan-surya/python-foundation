# print system info os processer and ram 
import platform
import psutil
print("System Information:")
print("System:", platform.system())
print("Node Name:", platform.node())
print("Release:", platform.release())
print("Version:", platform.version())
print("Machine:", platform.machine())
print("Processor:", platform.processor())
print("Platform:", platform.platform())
print("RAM Info:", psutil.virtual_memory())
print("Total RAM:", round(psutil.virtual_memory().total / (1024.0 **3)), "GB")
print("Available RAM:", round(psutil.virtual_memory().available / (1024.0 **3)), "GB")
print("Used RAM:", round(psutil.virtual_memory().used / (1024.0 **3)), "GB")
print("Total Cores:", psutil.cpu_count(logical=True))