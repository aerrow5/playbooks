# Infrastructure Setup Using Ansible and SmartOS

### Create new Virtual Machine called "shell"
```
ansible-playbook -i production provision_vm.yml --limit=shell
```
### Updating Packages on subsonic group
```
ansible-playbook -i production update_packages.yml --limit=subsonic 
```

### Run playbook to provision owncloud server
```
ansible-playbook -i production provision_vm.yml --limit=owncloud
```

### Run playbook to setup shell server
```
ansible-playbook -i production site.yml --limit=shell
```

### Get version of openssl on every server
```
ansible all -a "openssl version" -i production
```
