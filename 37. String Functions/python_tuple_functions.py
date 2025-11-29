# Python Tuple Functions & Methods Reference for DevOps & Development

# Tuple Creation & Initialization
tuple()              # Create empty tuple or convert iterable
()                   # Empty tuple literal
(item,)              # Single item tuple (comma required)
tuple(iterable)      # Convert iterable to tuple
tuple(zip(a, b))     # Create tuple pairs

# Tuple Methods (Limited - Immutable)
count()              # Count occurrences of value
index()              # Find index of first occurrence

# Tuple Operations
+                    # Concatenate tuples
*                    # Repeat tuple
in                   # Check if element exists
not in               # Check if element doesn't exist
len()                # Get tuple length
max()                # Get maximum value
min()                # Get minimum value
sum()                # Sum numeric elements
any()                # True if any element is truthy
all()                # True if all elements are truthy

# Tuple Unpacking
a, b, c = (1, 2, 3)  # Basic unpacking
a, *rest, c = tuple  # Extended unpacking
*start, b, c = tuple # Extended unpacking

# Named Tuples (collections.namedtuple)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
Server = namedtuple('Server', ['name', 'ip', 'port'])

# DevOps Specific Use Cases

# Server Configuration
server_config = ('web-server-01', '192.168.1.100', 80, 'nginx')
name, ip, port, service = server_config

# Database Connection
db_connection = ('localhost', 5432, 'mydb', 'user', 'password')
host, port, database, username, password = db_connection

# Environment Settings
env_config = ('production', 'us-east-1', 't3.large', 2)
environment, region, instance_type, count = env_config

# Network Configuration
network_tuple = ('10.0.1.0', '255.255.255.0', '10.0.1.1')
network, netmask, gateway = network_tuple

# Service Endpoints
api_endpoint = ('api.example.com', 443, '/v1/health', 'https')
domain, port, path, protocol = api_endpoint

# Monitoring Thresholds
cpu_thresholds = (70, 85, 95)  # warning, critical, emergency
memory_thresholds = (80, 90, 95)

# Version Information
version_info = (2, 1, 3, 'stable')
major, minor, patch, stage = version_info

# Coordinate Systems (for geographic deployments)
datacenter_location = (40.7128, -74.0060)  # NYC coordinates
latitude, longitude = datacenter_location

# Named Tuples for DevOps

# Server Definition
Server = namedtuple('Server', ['hostname', 'ip', 'role', 'environment'])
web_server = Server('web-01', '10.0.1.10', 'web', 'production')

# Database Configuration
DBConfig = namedtuple('DBConfig', ['host', 'port', 'name', 'user'])
db_config = DBConfig('db.example.com', 5432, 'app_db', 'app_user')

# Service Health
HealthCheck = namedtuple('HealthCheck', ['service', 'status', 'response_time'])
health = HealthCheck('api', 'healthy', 0.045)

# Deployment Info
Deployment = namedtuple('Deployment', ['version', 'timestamp', 'environment', 'rollback'])
deploy = Deployment('v2.1.0', '2024-01-15T10:30:00Z', 'prod', 'v2.0.9')

# Network Interface
Interface = namedtuple('Interface', ['name', 'ip', 'netmask', 'status'])
eth0 = Interface('eth0', '192.168.1.100', '255.255.255.0', 'up')

# Container Configuration
Container = namedtuple('Container', ['name', 'image', 'port', 'volume'])
app_container = Container('myapp', 'myapp:latest', 8080, '/data')

# Load Balancer Target
Target = namedtuple('Target', ['instance_id', 'ip', 'port', 'health'])
target = Target('i-1234567890abcdef0', '10.0.1.50', 80, 'healthy')

# SSL Certificate
Certificate = namedtuple('Certificate', ['domain', 'issuer', 'expiry', 'valid'])
cert = Certificate('example.com', 'Let\'s Encrypt', '2024-12-31', True)

# Development Use Cases

# Function Return Values
def get_user_info():
    return ('john_doe', 'john@example.com', 'admin')

username, email, role = get_user_info()

# Configuration Tuples
database_settings = (
    ('host', 'localhost'),
    ('port', 5432),
    ('database', 'myapp'),
    ('user', 'appuser')
)

# Immutable Constants
HTTP_STATUS_CODES = (
    (200, 'OK'),
    (404, 'Not Found'),
    (500, 'Internal Server Error')
)

# Coordinate Pairs
points = [(0, 0), (1, 1), (2, 4), (3, 9)]

# Key-Value Pairs
config_pairs = [
    ('debug', True),
    ('max_connections', 100),
    ('timeout', 30)
]

# Tuple Utilities for DevOps

# Convert list to tuple for immutability
def freeze_config(config_list):
    return tuple(config_list)

# Tuple comparison for versioning
def compare_versions(v1, v2):
    return v1 > v2  # Tuples compare element by element

# Create configuration from tuple
def create_config_dict(config_tuple):
    return dict(config_tuple)

# Batch tuple operations
def process_server_batch(servers):
    return [Server(*server_data) for server_data in servers]

# Advanced Tuple Operations

# Tuple slicing
config_subset = server_config[1:3]  # Get IP and port

# Tuple membership testing
if 'nginx' in server_config:
    print("Nginx server found")

# Tuple iteration
for item in server_config:
    print(f"Config item: {item}")

# Tuple enumeration
for index, value in enumerate(server_config):
    print(f"Position {index}: {value}")

# Tuple sorting (creates list)
sorted_thresholds = sorted(cpu_thresholds)

# Tuple Performance Benefits
# - Immutable (thread-safe)
# - Hashable (can be dict keys)
# - Memory efficient
# - Faster than lists for read operations
# - Perfect for configuration data
# - Ideal for function return values

# Common Patterns

# Swap variables using tuple
a, b = b, a

# Multiple assignment
x, y, z = get_coordinates()

# Ignore values with underscore
name, _, port = server_info

# Tuple as dictionary key
server_cache = {
    ('web-01', 'production'): 'active',
    ('db-01', 'production'): 'maintenance'
}

# Return multiple values from function
def get_system_info():
    return ('Linux', '5.4.0', '64-bit', 16)  # OS, kernel, arch, RAM