# Script de arranque del escenario

import subprocess

subprocess.call(["wget", "http://idefix.dit.upm.es/cdps/pfinal/pfinal.tgz"])
subprocess.call(["sudo", "vnx", "--unpack", "pfinal.tgz"])
subprocess.call(["/home/upm/Desktop/pfinal/bin/prepare-pfinal-vm"])

subprocess.call(["sudo", "vnx", "-f", "/home/upm/Desktop/pfinal/pfinal.xml", "--create"])