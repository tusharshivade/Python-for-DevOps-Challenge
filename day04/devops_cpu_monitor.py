# DevOps Resource Monitor

cpu_usage = 85
memory_usage = 70

cpu_limit = 80
memory_limit = 80

print("CPU Usage:", cpu_usage)
print("Memory Usage:", memory_usage)

# Checking if limits are exceeded
if cpu_usage > cpu_limit:
    print("Warning: CPU usage is high!")

if memory_usage > memory_limit:
    print("Warning: Memory usage is high!")

# Combined check
if cpu_usage > cpu_limit and memory_usage > memory_limit:
    print("Critical: Both CPU and Memory are high!")
