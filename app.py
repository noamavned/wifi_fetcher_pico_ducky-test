import subprocess


def print_data(name, pas):
    print(f'Name: {name}\nPassword: {pas}')


def get_pass_win(name):
    if not name:
        return None
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8')
    output = output.splitlines()
    for j in output:
        if j.startswith('    Key Content'):
            k = j.split(':')[1][1::]
            return k


try:
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8')
    # print(output)
    output = output.splitlines()
    state = False
    for i in output:
        if i.startswith("    State"):
            if i.find("dis") == -1:
                state = True
                break
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8')
    output = output.splitlines()[::-1]
    name = None
    for i in output:
        if i.startswith('    All User Profile'):
            j = i.split(':')[1][1::]
            name = j
    if state:
        print('Connected')
        print_data(name, get_pass_win(name))
    elif name != None:
        print('Last connected to')
        print_data(name, get_pass_win(name))
    else:
        print('Disconnected')
except Exception as e:
    print(e)