# my_variable = 42

# print ("my defined variable:",my_variable)

x = 20 # global variable

# def my_function():
#     x = 10 # Local variable.
#     print(x)

# # my_function()


server_name = "gsp"
port = 80
is_https_enabled = True
max_connections = 1000

# print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max connections: {max_connections}")

# update the configuration values
port = 443
is_https_enabled = False

# Print the updated configuration.
print(f"(Updated Port: {port}")
print(f"(Updated HTTPS enabled: {is_https_enabled})")
