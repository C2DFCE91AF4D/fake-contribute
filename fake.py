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

# 生成 10-30 个文件
for _ in range(random.randint(10, 100)):
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
  subprocess.run(['git', 'add', '.'])
  subprocess.run(['git', 'commit', '-m', commit_message])
