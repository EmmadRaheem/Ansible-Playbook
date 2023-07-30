Fetch AWS EC2 Instances Information using Ansible.

Many tools are available in the market, from Terraform, AWS CloudFormation, Chef, Puppet, and Salt Stack. There are some differences between each tool. Some are configuration management tools (Ansible, Chef, Saltstack), and others are purely provisioning tools (Terraform, Cloud Formation). One must choose their judgment based on factors like ease of learning and adoption.

All these modules help us accomplish various tasks in AWS cloud resources, including creation, deletion, management, and assessment. Our objective is to fetch EC2 Instance details using Ansible. Ansible has a module named 'amazon.aws.ec2_instance'.

To run the script, you only need the Boto3 module in Python, Ansible-Playbook and Ansible-Vault to save the AWS credentials securely.

The content of the secret.yml file to save the AWS credentials is
aws_access_key_id: <paste_your_access_key> 
aws_secret_access_key: <paste_your_secret_key>

Encrypt the contents of the file using the command;
ansible-vault encrypt secrets.yml. 
Remember this password and use it while you are starting the playbook. You use a startup argument for Ansible to ask you for the password.
ansible-playbook <filename.yml> --ask-vault-pass

This playbook can get all the running AWS EC2 instance details. The playbook is divided into two blocks. The 1st block extracts the information and stores it in a variable. The 2nd block display/print the information on the screen.

vim <filename.yml>
---
- name: Instance Details
  hosts: all
  gather_facts: false
  vars_files:
    - secrets.yml
  tasks:
  - name: Getting EC2 instance details 
    amazon.aws.ec2_instance:  
      region: "us-east-1"
      filters: 
        instance-state-name: "running" 
    register: ec2_details
   - name: Display the instance ID and tags
    debug:
      var: item
    loop: "{{ ec2_details.instances }}"
