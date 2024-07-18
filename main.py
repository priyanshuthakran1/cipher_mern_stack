import subprocess
def clone_repo(repo_url):
    try:
        subprocess.run(['git', 'clone', repo_url], check=True)
        print(f"Repository '{repo_url}' cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository '{repo_url}': {e}")
def push(current_repo_path):
    try:
        # Set the remote URL
        subprocess.run(['git', 'remote', 'set-url', 'origin', current_repo_path], check=True)
        
        # Add changes to staging
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit the changes
        subprocess.run(['git', 'commit', '-m', 'Update'], check=True)
        
        # Push the changes to the remote repository
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
        
        print("Repository pushed successfully.")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


urls = ['https://github.com/priyanshuthakran1/Lecture-51-CipherSchools']
# for url in urls:
#     clone_repo(url)
current_repo_path = 'https://github.com/priyanshuthakran1/cipher_mern_stack.git'
push(current_repo_path)

