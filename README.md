# Infrastructure Setup Using Ansible and SmartOS

```
ssh-agent bash
ssh-add ~/.ssh/id_rsa
```

```
ansible-playbook -i production site.yml --tags update_packages
```

```
ansible-playbook -i production shell.yml --extra-vars "provision_mode=true"
```

Image UUID from https://docs.joyent.com/public-cloud/instances/infrastructure/images/smartos/minimal
