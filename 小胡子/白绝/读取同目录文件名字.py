import os

# 获取当前脚本文件名
script_name = os.path.basename(__file__)

# 获取当前目录所有文件名（排除目录和脚本自身）
files = [f for f in os.listdir('.') 
         if os.path.isfile(f) 
         and f != '1.txt' 
         and f != script_name]

# 写入到1.txt
with open('1.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(files))

print(f"已保存 {len(files)} 个文件名到 1.txt")
print(f"已排除脚本文件: {script_name}")