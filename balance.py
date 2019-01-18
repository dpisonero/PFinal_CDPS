# Configuración del balanceador de carga

from subprocess import call

call(["sudo", "scp", "/home/upm/Desktop/loop.py", "root@lb:/root"])

call("sudo lxc-attach --clear-env -n lb -- apt update", shell=True)

call("sudo lxc-attach --clear-env -n lb -- apt -y install haproxy", shell=True)

call("sudo lxc-attach --clear-env -n lb -- python3 /root/loop.py", shell=True)

call("sudo lxc-attach --clear-env -n lb -- service haproxy stop", shell=True)
call("sudo lxc-attach --clear-env -n lb -- service haproxy start", shell=True)