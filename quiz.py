# Script para poner en marcha el servicio quiz en los servidores

from subprocess import call

# Instalamos nodejs y npm en los servidores
call("sudo lxc-attach --clear-env -n s1 -- apt -y install nodejs", shell=True)
call("sudo lxc-attach --clear-env -n s1 -- apt -y install npm", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- apt -y install nodejs", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- apt -y install npm", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- apt -y install nodejs", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- apt -y install npm", shell=True)

# Clonamos el repositorio
call("sudo lxc-attach --clear-env -n s1 -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2019.git; cd /root/quiz_2019; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31:3306/quiz; npm run-script migrate_cdps; npm run-script seed_cdps; ./node_modules/forever/bin/forever start ./bin/www\"", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2019.git; cd /root/quiz_2019; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www\"", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2019.git; cd /root/quiz_2019; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www\"", shell=True)

# Hacemos el enlace simbólico con el directorio asociado al cluster
call("sudo lxc-attach --clear-env -n s1 -- bash -c \"cd /root/quiz_2019/public; ln -s /mnt/nas uploads \"", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- bash -c \"cd /root/quiz_2019/public; ln -s /mnt/nas uploads \"", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- bash -c \"cd /root/quiz_2019/public; ln -s /mnt/nas uploads \"", shell=True)