# Infrastructure Setup Using Ansible and SmartOS

### Create new Virtual Machine called "shell"
```
ansible-playbook provision_vm.yml --limit=shell
```
### Run playbook to setup shell server
```
ansible-playbook site.yml --limit=shell
```

### Updating Packages on shell
```
ansible-playbook update_packages.yml --limit=shell
```

### Update packages on all servers
```
ansible-playbook site.yml --tags=update_packages
```
