import os

# Read WHO_TO_GREET from environment variable, default to 'GitHub Actions Student'
who_to_greet = os.environ.get('WHO_TO_GREET', 'GitHub Actions Student')

# Print greetings required by the lab prompt
print(f"Hello {who_to_greet}!")
print("This program is running inside GitHub Actions.")