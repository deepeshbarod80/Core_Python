# Python List Functions & Methods Reference for DevOps & Development

# List Creation & Initialization
list()               # Create empty list or convert iterable
[]                   # Empty list literal
[x for x in range()] # List comprehension
list(range(n))       # Create numbered list

# Adding Elements
append()             # Add single element to end
extend()             # Add multiple elements from iterable
insert()             # Insert element at specific index
+                    # Concatenate lists

# Removing Elements
remove()             # Remove first occurrence of value
pop()                # Remove and return element (default: last)
clear()              # Remove all elements
del list[index]      # Delete element at index
del list[start:end]  # Delete slice

# Searching & Finding
index()              # Find index of first occurrence
count()              # Count occurrences of value
in                   # Check if element exists
not in               # Check if element doesn't exist

# Sorting & Ordering
sort()               # Sort list in place
sorted()             # Return new sorted list
reverse()            # Reverse list in place
reversed()           # Return reverse iterator

# List Information
len()                # Get list length
max()                # Get maximum value
min()                # Get minimum value
sum()                # Sum numeric elements
any()                # True if any element is truthy
all()                # True if all elements are truthy

# List Copying
copy()               # Shallow copy
list.copy()          # Shallow copy method
list[:]              # Slice copy
copy.deepcopy()      # Deep copy (import copy)

# DevOps Specific Use Cases

# Configuration Management
config_files = ['nginx.conf', 'app.yaml', 'docker-compose.yml']
config_files.append('secrets.env')
config_files.extend(['monitoring.yml', 'logging.conf'])

# Server Management
servers = ['web-01', 'web-02', 'db-01']
if 'web-03' not in servers:
    servers.append('web-03')

# Log Processing
log_levels = ['DEBUG', 'INFO', 'WARN', 'ERROR']
error_logs = [log for log in logs if 'ERROR' in log]

# Deployment Environments
environments = ['dev', 'staging', 'prod']
environments.sort()  # Alphabetical order

# Port Management
used_ports = [80, 443, 8080, 3000]
available_ports = [p for p in range(8000, 9000) if p not in used_ports]

# Service Dependencies
services = ['database', 'cache', 'api', 'frontend']
services.reverse()  # Shutdown order

# Container Management
containers = ['app-1', 'app-2', 'nginx', 'redis']
running_containers = containers.copy()
running_containers.remove('redis')

# Monitoring Metrics
cpu_usage = [45.2, 67.8, 23.1, 89.5]
avg_cpu = sum(cpu_usage) / len(cpu_usage)
max_cpu = max(cpu_usage)

# File Processing
config_files = ['app.json', 'db.yaml', 'cache.conf']
json_files = [f for f in config_files if f.endswith('.json')]

# Network Subnets
subnets = ['10.0.1.0/24', '10.0.2.0/24', '10.0.3.0/24']
public_subnets = subnets[:2]  # First two subnets

# Build Artifacts
artifacts = ['app.jar', 'config.zip', 'docs.tar.gz']
artifacts.sort(key=lambda x: x.split('.')[-1])  # Sort by extension

# Advanced List Operations for DevOps

# Batch Operations
def batch_process(items, batch_size=10):
    return [items[i:i+batch_size] for i in range(0, len(items), batch_size)]

# Filter and Transform
def filter_active_services(services):
    return [s for s in services if s.get('status') == 'active']

# Merge Configurations
def merge_configs(base_config, override_config):
    merged = base_config.copy()
    merged.extend(override_config)
    return merged

# List Utilities for Development

# Data Validation
def validate_list(data, required_fields):
    return all(field in data for field in required_fields)

# List Flattening
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

# Remove Duplicates (preserve order)
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# List Comparison
def list_diff(list1, list2):
    return list(set(list1) - set(list2))

# Functional Programming with Lists
map()                # Apply function to all elements
filter()             # Filter elements by condition
zip()                # Combine multiple lists
enumerate()          # Get index and value pairs
itertools.chain()    # Flatten multiple iterables
itertools.groupby()  # Group consecutive elements

# List Performance Tips
# - Use list comprehensions for filtering/mapping
# - Use extend() instead of += for multiple additions
# - Use collections.deque for frequent insertions at beginning
# - Use bisect module for sorted list operations