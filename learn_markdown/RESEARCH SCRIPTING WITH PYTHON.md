## What is Scripting?

Scripts are short sets of instructions designed to automate tasks or control the system.

USE CASES:
- Automation
- Control
- Integration
- Rapid Development


## What are the characteristics of scripting? 

- Generally uses interpreted and high-level languages so no compile step is needed
- Cross platform compatibility
- Focus on automation
- Designed to work with APIs
- Flexibility in the sense that scripts should be adaptable to different use cases
- Limited Functionality


## Give some examples of the types of things scripts would do

SYSTEM ADMINISTRATION:
- File management (copying, moving, renaming, deleting files and directories)
- User management of accounts
- System configuration (modifying system settings and configurations
- Backup and restoration - creating backups of system data and restoring them in the case of 
failure.


## Why is Python good for scripting?

- High level, interpreted language
- Fantastic readability
- Excellent attention to clarity of syntax
- People comfortable with it from a young age - e.g. community is important
- Often found in Linux installations automatically


## Example of a Python script

```
#!/usr/bin/python3

import os
os.chdir('/Users/kip/Downloads')

for file in os.listdir():
    if file.endswith('.txt'):
        file_name, file_ext = os.path.splitext(f)
        new_name = file_name + '.text'
        os.rename(f, new_name)

print('Files renamed!')
```

## Main differences between scripting and programming

### Programming:

- Building applications including OSes, games and full software
- High and low level languages used, with static typing, and compiled code
- Long development times

### Scripting

- Relatively-short in length with limited functionality
- Designed to automate tasks, saving time and effort
- Fast development times
- Generally interpreted languages, high-level and dynamic typing


## Is Python better for programming or scripting?

It can be used for both, but it's probably better for scripting due to its readability lending
to rapid development times. 


## Do Cloud/DevOps engineers usually do programming or scripting? Why?

The answer is usually scripting, due to the advantages of automation, of configuration management scripts
such as Ansible, Puppet and Terraform, and creating CI/CD pipelines. However, programming
knowledge may be beneficial for:
- understanding what is being built _in_ the CI/CD pipeline
- building custom tools or extending the functionality of existing tools
- data analysis and visualisation
- integrating AI and Machine Learning solutions


## Examples of the way we use scripts as Cloud/DevOps Engineers?

- Infrastructure automation, configuration and scaling
- Deployment automation in CI/CD pipelines
- Monitoring and alerting, including the rapid analysis of log files
- Security automation

- Bash: Writing shell scripts to automate tasks like file transfers, system backups, and user management.
- Python: Developing scripts to interact with APIs, parse logs, and automate complex tasks.
- Ruby: Using tools like Ruby on Rails for web development and automation.
- PowerShell: Automating Windows administration tasks and integrating with Azure.


### [ SAMPLE TABLE ]

| Name      |  Type     |  High or Low Level        |
|-----------|-----------|---------------------------|
| Python    |  Script   |   High                    |
| C++       |  Full     | Low                       |


