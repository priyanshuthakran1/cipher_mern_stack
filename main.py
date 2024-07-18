import subprocess
def clone_repo(repo_url):
    try:
        subprocess.run(['git', 'clone', repo_url], check=True)
        print(f"Repository '{repo_url}' cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository '{repo_url}': {e}")

def push(current_repo_path):
    subprocess.run(['git', 'remote', 'set-url', 'origin', current_repo_path], check=True)
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Update'])
    subprocess.run(['git', 'push', '-u', 'origin','main'])
    print("Repository pushed successfully.")


urls = ['https://github.com/priyanshuthakran1/Lecture-49-CipherSchools']
# for url in urls:
#     clone_repo(url)
current_repo_path = 'https://github.com/priyanshuthakran1/cipher_mern_stack.git'
push(current_repo_path)