import os

env_path = '.env'
if os.path.exists(env_path):
    # Read with utf-16 to handle the current encoding
    with open(env_path, 'r', encoding='utf-16') as f:
        content = f.read()
    
    # Write back as utf-8
    with open(env_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully converted .env to UTF-8")
else:
    print(".env file not found")
