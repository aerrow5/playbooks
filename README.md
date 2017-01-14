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

### Run playbook to only setup common tag on shell server
```
ansible-playbook site.yml --limit=shell --tags=common
```

### Setup plex (and update to latest version)
```
ansible-playbook site.yml --limit=plex
```
