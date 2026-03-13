import subprocess
import os

# غير المسار ده على حسب مشروعك الفعلي
PROJECT_PATH = r"E:\mariam\first-app" 
COMMIT_MESSAGE = "Auto commit from DeepSeek"

def run_git(command):
    subprocess.run(command, cwd=PROJECT_PATH, shell=True)

# لو المجلد مش Git repo، نعمله init
if not os.path.exists(os.path.join(PROJECT_PATH, ".git")):
    run_git("git init")

# ضيف كل الملفات، commit، و push
run_git("git add .")
run_git(f'git commit -m "{COMMIT_MESSAGE}"')
run_git("git branch -M main")
run_git("git push -u origin main")

print("✅ تم الرفع على GitHub بنجاح!")