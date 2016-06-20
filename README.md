# Infrastructure Setup Using Ansible and SmartOS


### Updating Packages on subsonic group
```
ansible-playbook -i production update_packages.yml --limit=subsonic 
```

### Run playbook to provision owncloud server and configure
```
ansible-playbook -i production site.yml --limit=owncloud --extra-vars "provision_mode=true"
```
