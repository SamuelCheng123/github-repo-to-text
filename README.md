# github-repo-to-text
這是一個簡單的將 github repo clone 到本地端並將 repo 內的所有檔案包含檔案路徑存到一個大的 txt 檔案的簡單範例
配置好 python 檔案之後可以將 python 檔案加入 zsh 指令以方便使用
(python 檔案內的 `root_path` 要改成 clone 下來的 repo 想要存放的目錄)

## 設定 zsh
如果你使用的是 zsh，輸入以下命令：
    `code ~/.zshrc` 

接下來在 zshrc 當中添加指令名稱和 python 檔案的存放位置位置

```
function gitrepotxt() {
python3 /Users/{yourusername}/Desktop/Github/repo-to-text.py "$@"
}
```

這樣就完成了，以後可以直接在 zsh 當中輸入想要讀取的 github repo url
ex.
```
gitrepotxt git@github.com:SamuelCheng123/Myfirst.git
gitrepotxt https://github.com/SamuelCheng123/Myfirst.git
```
txt 檔案就會自動出現在下載目錄
clone 下來的 repo 會自動出現在之前在 python 檔案中設定的 `root_path` 目錄
如果 `root_path` 目錄 repo 已經存在，則會把原本的 repo 使用 `git pull` 更新成最新版本之後再轉換成文字檔
