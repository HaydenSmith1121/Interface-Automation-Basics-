host = 'http://172.31.52.55:38000/'
login_path_1 = 'api2/auth-token/'
info_path_2 = 'api2/account/info/'
add_select_path_3_4 = 'api2/repos/'


def modify_delete_add_path_5_6_7_8(num, id, file='130.txt'):
    if num == 5:
        path = f'api2/repos/{id}/?op=rename'
        return host + path
    elif num == 6:
        path = f'api2/repos/{id}/'
        return host + path
    elif num == 7 or num == 8:
        path = f'api2/repos/{id}/file/?p=/{file}&reloaddir=true'
        return host + path
