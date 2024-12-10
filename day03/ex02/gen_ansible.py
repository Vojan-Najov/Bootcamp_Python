import yaml


def main():
    todo_filename = '../materials/todo.yml'
    deploy_filename = 'deploy.yml'

    try:
        with open(todo_filename, 'r', encoding='UTF-8') as file:
            todo_list = yaml.load(file, Loader=yaml.Loader)
            install_packages = todo_list['server']['install_packages']
            install_packages.append('redis')
            exploit_files = todo_list['server']['exploit_files']
            bad_guys = todo_list['bad_guys']
    except Exception as e:
        print(e)
        exit()

    install_tasks = [
        {
            'name': f'Install package {pkg}',
            'ansible.builtin.yum': {
                'name': pkg,
                'state': 'present'
            }
        }
        for pkg in install_packages
    ]
    copy_tasks = [
        {
            'name': f'Copy exploit file {exploit_file}',
            'ansible.builtin.copy': {
                'src': exploit_file,
                'dest': '/home/user',
                'mode': '0644'
            }
        }
        for exploit_file in exploit_files
    ]
    run_tasks = [
        {
            'name': 'Download python-pip',
            'command': 'wget -O /home/user/get-pip.py' + \
                       ' https://bootstrap.pypa.io/get-pip.py'
        },
        {
            'name': 'Install python-pip',
            'command': 'python3 /home/user/get-pip.py'
        },

        {
            'name': 'Install bs4',
            'command': 'python3 -m pip install bs4'
        },
        {
            'name': 'Install python-redis',
            'command': 'python3 -m pip install redis'
        },
        {
            'name': 'Run explot on the server',
            'command': 'python3 /home/user/exploit.py',
        },
        {
            'name': 'Run consumer on server',
            'command': f'python3 /home/user/consumer.py -e {",".join(bad_guys)}',
        },
    ]

    playbook = [
        {
            'name': 'Python Bootcamp day03',
            'hosts': 'server',
            'become': True,
            'tasks': install_tasks + copy_tasks + run_tasks
        }
    ]

    with open(deploy_filename, 'w', encoding='UTF-8') as file:
        yaml.dump(playbook, file, default_flow_style=False, sort_keys=False)


if __name__ == '__main__':
    main()
