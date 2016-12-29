# Infrastructure Setup Using Ansible and SmartOS

### Create new Virtual Machine called "shell"
```
ansible-playbook -i production provision_vm.yml --limit=shell
```
### Run playbook to setup shell server
```
ansible-playbook -i production site.yml --limit=shell
```

### Updating Packages on shell
```
ansible-playbook -i production update_packages.yml --limit=shell
```

### Run playbook to setup shell server
```
ansible-playbook -i production site.yml --limit=shell --tags=common
```


