import os
import random
import string
import subprocess
import logging

# 设置日志级别
logging.basicConfig(level=logging.INFO)

def run_command(command):
  result = subprocess.run(command, capture_output=True, text=True)
  if result.returncode != 0:
    logging.error(f"Command '{' '.join(command)}' failed with error:\n{result.stderr}")
    return False
  return True

# 确保 src 文件夹存在
if not os.path.exists('src'):
  os.makedirs('src')

# 设置 git 用户名和邮箱
if not run_command(['git', 'config', '--global', 'user.name', 'Your Name']):
  exit(1)
if not run_command(['git', 'config', '--global', 'user.email', 'youremail@example.com']):
  exit(1)

# 生成 50-150 个文件
for _ in range(random.randint(10, 500)):
  # 生成随机文件名
  filename = ''.join(random.choice(string.ascii_letters) for _ in range(10)) + '.txt'
  filepath = os.path.join('src', filename)

  # 创建并写入文件
  with open(filepath, 'w') as f:
    f.write('This is a randomly generated file.')

  # 添加文件到 git
  if not run_command(['git', 'add', filepath]):
    exit(1)

  # 生成随机 commit 信息
  commit_message = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

  # 提交文件
  if not run_command(['git', 'commit', '-m', commit_message]):
    exit(1)

# 所有文件都添加了 commit 后，提交更改
if not run_command(['git', 'push']):
  exit(1)

# 删除 src 文件夹中的所有文件
for filename in os.listdir('src'):
  filepath = os.path.join('src', filename)
  if os.path.isfile(filepath):
    os.remove(filepath)

# 添加所有更改
if not run_command(['git', 'add', '.']):
  exit(1)

# 添加 commit: refake
if not run_command(['git', 'commit', '-m', 'refake']):
  exit(1)

# 提交更改
if not run_command(['git', 'push']):
  exit(1)
