import subprocess
import os
import getpass
import shutil

def get_repo_name(url):
    # 我們首先用 ':' 來分割 URL 並取最後一部分
    repo_with_extension = url.split(':')[-1]
    
    # 然後用 '/' 來分割 URL 並取最後一部分
    repo_with_extension = repo_with_extension.split('/')[-1]

    # 最後用 '.' 來分割並取第一部分以取得 repo 名稱
    repo_name = repo_with_extension.split('.')[0]
    
    return repo_name

def repo_to_text(
    repo_url: str,
):
    repo_name = get_repo_name(repo_url)

    # Your GitHub repo's local path
    root_path = f'/Users/{getpass.getuser()}/Desktop/refer/'
    repo_path = root_path + repo_name
    output_file = os.path.join(root_path, f"{repo_name}.txt")

    # If the repo already exists, pull the latest version, else clone the repo
    if os.path.exists(repo_path):
        try:
            subprocess.run(['git', '-C', repo_path, 'pull'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error in git pull: {e}")
    else:
        try:
            subprocess.run(['git', 'clone', f"{repo_url}", repo_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error in git clone: {e}")


    # Here we simply treat all files as text files for simplicity
    # If your repo contains non-text files (e.g., images or binary files), more sophisticated filtering might be required
    all_files = []
    for root, dirs, files in os.walk(repo_path):
        all_files.extend(os.path.join(root, file) for file in files)

    print('all_files' , all_files)
    with open(output_file, "w") as f:
        for file_path in all_files:
            try:
                with open(file_path, "r") as file:
                    f.write(f"--- Content of {file_path} ---\n")
                    f.write(file.read())
                    f.write("\n\n")
            except Exception as e:
                print(f'Write txt error: {e}')
                print(f'Error path: {file_path}')

    # Move the text file to the Downloads folder
    shutil.move(output_file, f'/Users/{getpass.getuser()}/Downloads/{repo_name}.txt')

if __name__ == "__main__":
    repo_to_text(
        repo_url="https://github.com/SamuelCheng123/Myfirst.git"
    )
