# Infrastructure Setup Using Ansible and SmartOS

```
ssh-agent bash
ssh-add ~/.ssh/id_rsa
```

ansible-playbook -i production site.yml --tags update_packages
