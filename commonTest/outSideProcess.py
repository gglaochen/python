"""
启用外部进程
"""
import subprocess

print('$ 请求外部进程 www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)