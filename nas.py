# Script para la configuración del sistema de ficheros
# replicado en NAS1, NAS2, NAS3 donde se guardan las imágenes

from subprocess import call

# Añadimos los nas al cluster
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 20.2.4.21", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 20.2.4.22", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 20.2.4.23", shell=True)

# Comprobamos el estado
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer status", shell=True)

# Creamos el volumen con los tres servidores
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume create nas replica 3 20.2.4.21:/nas 20.2.4.22:/nas 20.2.4.23:/nas force", shell=True)

# Arrancamos, comprobamos y ajustamos el temporizador
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume start nas", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume info", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume set nas network.ping-timeout 5", shell=True)

# Montamos el directorio nas de los servidores sobre el cluster que acabamos de configurar
call("sudo lxc-attach --clear-env -n s1 -- mkdir /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s1 -- mount -t glusterfs 20.2.4.21:/nas /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- mkdir /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- mount -t glusterfs 20.2.4.21:/nas /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- mkdir /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- mount -t glusterfs 20.2.4.21:/nas /mnt/nas", shell=True)