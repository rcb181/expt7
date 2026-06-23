ansible all -i hosts.ini --list-hosts

ansible all -i hosts.ini -m ping

ansible-playbook -i hosts.ini play1.yml

chmod +x library/first_module.py

ansible-playbook -i hosts.ini secondpb.yml
