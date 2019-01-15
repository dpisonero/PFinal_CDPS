# Script para modificar el haproxy.cfg

f = open("/etc/haproxy/haproxy.cfg", 'r+')

for line in f:
	if "errorfile 504 /etc/haproxy/errors/504.http" in line:
		f.write("\nfrontend lb\n\tbind *:80\n\tmode http\n\tdefault_backend webservers\n\nbackend webservers\n\tmode http\n\tbalance roundrobin\n\tserver s1 20.2.3.11:3000 check\n\tserver s2 20.2.3.12:3000 check\n\tserver s3 20.2.3.13:3000 check")

f.close()