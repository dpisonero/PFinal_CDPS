# Este script borra la interfaz gráfica fw.fwb de la máquina fw,
# mete el script del fw bien confifurado (almacenado en Descargas), 
# y la nueva interfaz gráfica fw.fwb en fw (aunque no es necesario),
# cambia los permisos del scipt fw.fw para poder ejecutarlo, y lo ejecuta.

import subprocess

subprocess.call(["sudo", "scp", "/home/upm/Downloads/fw.fw", "root@fw:/root"])
subprocess.call(["sudo", "lxc-attach", "--clear-env", "-n", "fw", "--", "rm", "/root/fw.fwb"])
subprocess.call(["sudo", "scp", "/home/upm/Downloads/fw.fwb", "root@fw:/root"])
subprocess.call(["sudo", "lxc-attach", "--clear-env", "-n", "fw", "--", "chmod", "777", "/root/fw.fw"])
subprocess.call(["sudo", "lxc-attach", "--clear-env", "-n", "fw", "--", "/root/fw.fw"])