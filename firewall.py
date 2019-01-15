import subprocess

subprocess.call(["sudo", "scp", "/home/upm/Downloads/fw.fw", "root@fw:/root"])
subprocess.call(["sudo", "lxc-attach", "--clear-env", "-n", "fw", "--", "rm", "/root/fw.fwb"])
subprocess.call(["sudo", "scp", "/home/upm/Downloads/fw.fwb", "root@fw:/root"])
subprocess.call(["sudo", "lxc-attach", "--clear-env", "-n", "fw", "--", "chmod", "777", "/root/fw.fw"])
subprocess.call(["sudo", "lxc-attach", "--clear-env", "-n", "fw", "--", "/root/fw.fw"])