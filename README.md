# github-repo-to-text
這是一個簡單的將 github repo clone 到本地端並將 repo 內的所有檔案包含檔案路徑存到一個大的 txt 檔案的簡單範例
配置好 python 檔案之後可以將 python 檔案加入 zsh 指令以方便使用

## 設定 zsh
如果你使用的是 zsh，輸入以下命令：
    `code ~/.zshrc` 

接下來在 zshrc 當中添加指令名稱和 python 檔案的存放位置位置

```
function repotxt() {
python3 /Users/{yourusername}/Desktop/Github/repo-to-text.py "$@"
}
```

這樣就完成了，以後可以直接在 zsh 當中輸入
```
repotxt git@github.com:SamuelCheng123/Myfirst.git
```
txt 檔案就會自動出現在下載目錄
