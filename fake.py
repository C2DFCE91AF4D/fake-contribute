import os
import random
import string
import subprocess

# 确保 src 文件夹存在
if not os.path.exists('src'):
  os.makedirs('src')

# 设置 git 用户名和邮箱
subprocess.run(['git', 'config', '--global', 'user.name', 'liyangxia'])
subprocess.run(['git', 'config', '--global', 'user.email', '126838514+liyangxia@users.noreply.github.com'])

# 生成 50-150 个文件
for _ in range(random.randint(10, 10)):
  # 生成随机文件名
  filename = ''.join(random.choice(string.ascii_letters) for _ in range(10)) + '.txt'
  filepath = os.path.join('src', filename)

  # 创建并写入文件
  with open(filepath, 'w') as f:
    f.write('This is a randomly generated file.')

  # 添加文件到 git
  subprocess.run(['git', 'add', filepath])

  # 生成随机 commit 信息
  commit_message = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

  # 提交文件
  subprocess.run(['git', 'commit', '-m', commit_message])

# 所有文件都添加了 commit 后，提交更改
subprocess.run(['git', 'push'])

# 删除 src 文件夹中的所有文件
for filename in os.listdir('src'):
  filepath = os.path.join('src', filename)
  if os.path.isfile(filepath):
    os.remove(filepath)
