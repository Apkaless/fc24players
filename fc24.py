import cloudscraper
import time
import json
from bs4 import BeautifulSoup
import sqlite3
import os
import subprocess
from urllib.request import urlretrieve
import colorama





def banner():


    print(f'''{green}


 _______   ______     ___    _  _    
|   ____| /      |   |__ \  | || |   
|  |__   |  ,----'      ) | | || |_  
|   __|  |  |          / /  |__   _| 
|  |     |  `----.    / /_     | |   
|__|      \______|   |____|    |_|   
                                     



          
{yellow}[!] {green}Creator     {res}==> {green}Sabah

{yellow}[!] {green}Instagram   {res}==> {green}Apkaless
          
{yellow}[!] {green}Github      {res}==> {green}https://github.com/apkaless
        
{yellow}[!] {green}Nationality {res}==> {green}IRAQ{res}

                 
''')
    


def cls():

    try:
        os.system('cls')
    except:
        os.system('clear')

def install_packages():

    packages = ['cloudscraper', 'bs4', 'colorama']

    for package in packages:
        subprocess.check_output('pip install %s --quiet' %(package), shell=True)
    
    else:

        cls()

def download():

    url = 'https://github.com/Apkaless/fc24players/raw/main/fc24players.db'

    filename = 'fc24players.db'

    return urlretrieve(url, filename)

def showPlayers(attackers, midfielders):

    attackers_players = attackers

    midfielders_players = midfielders

    attackers = []

    midfielders = []



    for attacker in attackers_players:

        attackers.append(attacker)


    for midfielder in midfielders_players:

        midfielders.append(midfielder)
    
    return attackers, midfielders


def display_players(ptupl):

    c = 0

    print('[Attackers]:\n')

    for attacker in ptupl[0]:

        c += 1

        print(f'''[{c}] {attacker}''')

    else:
        c = 0

    print(f'\n=====================================\n\n[Midfielders]:\n')

    for midfielder in ptupl[1]:

        c += 1

        print(f'[{c}] {midfielder}')

    else:
        c = 0

def check_connection():

    try:
        ses = cloudscraper.create_scraper()

        ses.get('https://google.com')

    except:
        print('Your Internet Isn\'t Stable (Bad Network)')

def attackers(conn):

    cr = conn.cursor()

    attackers = cr.execute('SELECT * FROM attackers')

    for attack in enumerate(attackers.fetchall(), start=1):

        attacker = attack[1][0]

        attacker_id = attack[1][1]

        attackers_players[attacker] = attacker_id

    conn.commit()

def midfielders(conn):

    cr = conn.cursor()

    midfielders = cr.execute('SELECT * FROM midfielders')

    for midfield in enumerate(midfielders.fetchall(), start=1):

        midfielder = midfield[1][0]

        midfielder_id = midfield[1][1]

        midfielders_players[midfielder] = midfielder_id

    conn.commit()


def update():

    os.chdir('..')
    print(os.getcwd())
    time.sleep(5)
    subprocess.check_output('rmdir -rf fc24players', shell=True)

    subprocess.check_output('git clone https://github.com/Apkaless/fc24players.git')

    os.chdir("fc24players")

    subprocess.check_output('python fc24.py')

def check_account(email, password, platform):

    with cloudscraper.create_scraper(debug=False) as sess:

        login_data = {
        'email': f'{email}',
        'regionCode': 'null',
        'phoneNumber': '',
        'password': f'{password}',
        '_eventId': 'submit',
        'cid': 'null',
        'showAgeUp': 'true',
        'thirdPartyCaptchaResponse': '',
        'loginMethod': 'emailPassword',
        '_rememberMe': 'on',
        'rememberMe': 'on'
        }

        auth_params = {

            'accessToken': '',
            'client_id': 'FC24_JS_WEB_APP',
            'display': 'web2/login',
            'hide_create': 'true',
            'locale': 'en_US',
            'prompt': 'login',
            'redirect_uri': 'https://www.ea.com/en-gb/ea-sports-fc/ultimate-team/web-app/auth.html',
            'release_type': 'prod',
            'response_type': 'token',
            'scope': 'basic.identity offline signin basic.entitlement basic.persona'
        }

        all_urls = {

        'auth_url': 'https://accounts.ea.com/connect/auth',
        'ea_hostname_url': 'https://signin.ea.com',
        'webapp_url': 'https://www.ea.com/en-gb/ea-sports-fc/ultimate-team/web-app/',
        'account_info_url': 'https://utas.mob.v2.fut.ea.com/ut/game/fc24/v2/user/accountinfo',
        'sid_url': 'https://utas.mob.v2.fut.ea.com/ut/auth',
        'market': 'https://utas.mob.v2.fut.ea.com/ut/game/fc24/transfermarket',
        'pdid': 'https://gateway.ea.com/proxy/identity/pids/me'

        }

        auth_req = sess.get(all_urls['auth_url'], params=auth_params, allow_redirects=False)

        next_url_req = sess.get(auth_req.headers['location'], allow_redirects=False)

        login_page_url = next_url_req.headers['location']

        jsid = next_url_req.cookies['JSESSIONID']

        signin_cookie = next_url_req.cookies['signin-cookie']

        headers['Cookie'] = f'JSESSIONID={jsid}; signin-cookie={signin_cookie}'

        full_webapp_url = all_urls['ea_hostname_url'] + login_page_url

        login_webapp = sess.get(full_webapp_url, headers=headers, allow_redirects=False)

        if login_webapp.status_code == 200:

            login_req = sess.post(login_webapp.url, data=login_data, headers=headers, allow_redirects=False)

            next_url = sess.get(all_urls['ea_hostname_url'] + login_req.headers['location'], headers=headers)

            soup = BeautifulSoup(next_url.text, 'html.parser')

            page_title = soup.find('title').get_text()

            page_title = page_title.strip()

            if 'Two Factor' in page_title:

                with open('user_credentials.json', 'w', encoding='utf8') as f:

                    data = {
                        'email': f'{email}',
                        'password': f'{password}',
                        'platform': f'{platform}'
                    }

                    f.write(json.dumps(data))

                    f.close()

                print(f'\n\n{blue}[+] {green}Your Credentials Are Saved To: {res}user_credentials.json')

                input(f'\n\n{yellow}[!] {res}Press {blue}ENTER {res}To Go Back To The Main Menu ')

            else:
                print(f'\n{red}[x] Your Credentials Are Incorrect, Please Check Your Information And Try Again !!')

                input(f'\n\n{yellow}[!] {res}Press {blue}ENTER {res}To Go Back To The Main Menu ')

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}               

pheaders = {

    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Host': 'gateway.ea.com'

}

def hunt(pid, mxprice, mnprice,email, password, platform, targeted_player):


    with cloudscraper.create_scraper(debug=False) as sess:

        login_data = {
        'email': f'{email}',
        'regionCode': 'null',
        'phoneNumber': '',
        'password': f'{password}',
        '_eventId': 'submit',
        'cid': 'null',
        'showAgeUp': 'true',
        'thirdPartyCaptchaResponse': '',
        'loginMethod': 'emailPassword',
        '_rememberMe': 'on',
        'rememberMe': 'on'
        }

        sendCode_Data = {
            'codeType': 'APP',
            'maskedDestination': '',
            '_codeType': 'APP',
            '_eventId': 'submit'
        }

        send_login_code_data = {

            'oneTimeCode': '',
            '_trustThisDevice': 'on',
            'trustThisDevice': 'on',
            '_eventId': 'submit'
        }

        fid_params = {

            'hide_create': 'true',
            'display': 'web2/login',
            'scope': 'basic.identity offline signin basic.entitlement basic.persona',
            'release_type': 'prod',
            'response_type': 'token',
            'redirect_uri': 'https://www.ea.com/en-gb/ea-sports-fc/ultimate-team/web-app/auth.html',
            'accessToken': '',
            'locale': 'en_US',
            'prompt': 'login',
            'client_id': 'FC24_JS_WEB_APP',
            'fid': 'null'
        }

        auth_params = {

            'accessToken': '',
            'client_id': 'FC24_JS_WEB_APP',
            'display': 'web2/login',
            'hide_create': 'true',
            'locale': 'en_US',
            'prompt': 'login',
            'redirect_uri': 'https://www.ea.com/en-gb/ea-sports-fc/ultimate-team/web-app/auth.html',
            'release_type': 'prod',
            'response_type': 'token',
            'scope': 'basic.identity offline signin basic.entitlement basic.persona'
        }

        accountInfo_data = {
            'client_id': 'FUTWEB_BK_OL_SERVER',
            'redirect_uri': 'nucleus:rest',
            'response_type': 'code',
            'access_token': '',
            'release_type': 'prod',
            'client_sequence': 'shard5'
        }

        accountInfo_data_2 = {
            'filterConsoleLogin': 'true',
            'sku': 'FUT24WEB',
            'returningUserGameYear': '2023',
            'clientVersion': '1'
        }

        session_id_data = {

                'clientVersion': '1',
                'ds': "46d651ddcea4921510566bbd837767532087ad9f76ca8bab891a9b5fbe92c26a/17ac",
                'gameSku': f"{platform}",
                'identification': {'authCode': '', 'redirectUrl': 'nucleus:rest'},
                'isReadOnly': 'false',
                'locale': "en-US",
                'method': "authcode",
                'nucleusPersonaId': '',
                'priorityLevel': '4',
                'sku': "FUT24WEB"
        }


        search_data = {
            'num': '21',
            'start': '0',
            'type': 'player',
            'maskedDefId': f'{pid}',
            'minb': f'{mnprice}',
            'maxb': f'{mxprice}'
        }

        all_urls = {

        'auth_url': 'https://accounts.ea.com/connect/auth',
        'ea_hostname_url': 'https://signin.ea.com',
        'webapp_url': 'https://www.ea.com/en-gb/ea-sports-fc/ultimate-team/web-app/',
        'account_info_url': 'https://utas.mob.v2.fut.ea.com/ut/game/fc24/v2/user/accountinfo',
        'sid_url': 'https://utas.mob.v2.fut.ea.com/ut/auth',
        'market': 'https://utas.mob.v2.fut.ea.com/ut/game/fc24/transfermarket',
        'pdid': 'https://gateway.ea.com/proxy/identity/pids/me'

        }

        auth_req = sess.get(all_urls['auth_url'], params=auth_params, allow_redirects=False)

        next_url_req = sess.get(auth_req.headers['location'], allow_redirects=False)

        login_page_url = next_url_req.headers['location']

        jsid = next_url_req.cookies['JSESSIONID']

        signin_cookie = next_url_req.cookies['signin-cookie']

        headers['Cookie'] = f'JSESSIONID={jsid}; signin-cookie={signin_cookie}'

        full_webapp_url = all_urls['ea_hostname_url'] + login_page_url

        login_webapp = sess.get(full_webapp_url, headers=headers, allow_redirects=False)

        if login_webapp.status_code == 200:

            login_req = sess.post(login_webapp.url, data=login_data, headers=headers, allow_redirects=False)

            next_url = sess.get(all_urls['ea_hostname_url'] + login_req.headers['location'], headers=headers)

            twoFA = sess.post(next_url.url, data=sendCode_Data, headers=headers)

            if twoFA.status_code == 200:

                sixDigitCode = input('Enter 6 digit code From Authenticator App: ')

                send_login_code_data['oneTimeCode'] = sixDigitCode

                sendCode_req = sess.post(twoFA.url, data=send_login_code_data, headers=headers, allow_redirects=False)

                _nx_mpcid = sendCode_req.cookies['_nx_mpcid']

                osc = sendCode_req.cookies['osc']

                headers['Cookie'] = f'JSESSIONID={jsid}; signin-cookie={signin_cookie}; _nx_mpcid={_nx_mpcid}; osc={osc}'

                auth_params['fid'] = auth_req.headers['location'].split('?')[1].split('=')[1]

                fid_auth = sess.get(all_urls['auth_url'], params=auth_params, headers=headers, allow_redirects=False)

                remid = fid_auth.cookies['remid']

                sid = fid_auth.cookies['sid']

                webapp_page = fid_auth.headers['location']

                headers['Cookie'] = f'JSESSIONID={jsid}; signin-cookie={signin_cookie}; _nx_mpcid={_nx_mpcid}; osc={osc}; sid={sid}; remid={remid}'

                webapp_page_req = sess.get(webapp_page, headers=headers, allow_redirects=False)

                token_info = {
                    'access_token': f'{webapp_page.split("#")[1].split("=")[1].split("&")[0]}',
                    'token_type': 'Bearer',
                    'expires_in': f'{webapp_page.split("#")[1].split("&")[2].split("=")[1]}'
                }

                req = sess.get(all_urls['webapp_url'], headers=headers)

                accountInfo_data['access_token'] = f"{token_info['access_token']}"

                fetch_accountInfo_code = sess.get(all_urls['auth_url'], params=accountInfo_data, headers=headers)

                code = json.loads(str(fetch_accountInfo_code.text))['code']

                fetch_accountInfo_accessToken = sess.get('https://accounts.ea.com/connect/auth?response_type=token&redirect_uri=nucleus%3Arest&prompt=none&client_id=ORIGIN_JS_SDK', headers=headers)

                accessT = json.loads(str(fetch_accountInfo_accessToken.text))['access_token']

                pheaders['Authorization'] = f'Bearer {accessT}'

                fetch_accountInfo_pdid = sess.get(all_urls['pdid'], headers=pheaders)

                pdidNumber = json.loads(str(fetch_accountInfo_pdid.text))['pid']['pidId']

                accdateCreated = json.loads(str(fetch_accountInfo_pdid.text))['pid']['dateCreated']

                accstatus = json.loads(str(fetch_accountInfo_pdid.text))['pid']['status']

                accemailstatus = json.loads(str(fetch_accountInfo_pdid.text))['pid']['emailStatus']

                headers['Nucleus-Access-Code'] = f'{code}'

                headers['Nucleus-Redirect-Url'] = 'nucleus:rest'

                headers['Host'] = 'utas.mob.v2.fut.ea.com'

                headers['Easw-Session-Data-Nucleus-Id'] = f'{pdidNumber}'

                headers['X-Ut-Phishing-Token'] = '0'

                fetch_accountInfo = sess.get(all_urls['account_info_url'], params=accountInfo_data_2, headers=headers)

                accName = json.loads(str(fetch_accountInfo.text))['userAccountInfo']['personas'][0]['personaName']

                personaID = json.loads(str(fetch_accountInfo.text))['userAccountInfo']['personas'][0]['personaId']

                userClubName = json.loads(str(fetch_accountInfo.text))['userAccountInfo']['personas'][0]['userClubList'][0]['clubName']

                accountInfo_data['client_sequence'] = 'ut-auth'

                fetch_2nd_code = sess.get(all_urls['auth_url'], params=accountInfo_data, headers=headers)

                second_code = json.loads(str(fetch_2nd_code.text))['code']

                session_id_data['identification']['authCode'] = second_code

                session_id_data['nucleusPersonaId'] = personaID

                sid_req = sess.post(all_urls['sid_url'], headers=headers, json=session_id_data)

                sid = json.loads(str(sid_req.text))['sid']

                headers['X-Ut-Sid'] = sid

                cls()

                print(f'''
{green}[+] {blue}Account Name: {res}{accName}\n
{green}[+] {blue}Club Name: {res}{userClubName}\n
{green}[+] {blue}Account Creation Date: {res}{accdateCreated}\n
{green}[+] {blue}Account State: {green}{accstatus}\n
{green}[+] {blue}Email State: {res}{accemailstatus}\n

    ''')

                input(f'\n{yellow}[!] {res}Press {blue}Enter {res}To Keep Going With {red}Hunting {res}')

                cls()

                print(f'{yellow}[!] The Hunter IS Running...\n\n[*] Please Leave The Hunter Doing His Work\n\n[*] When The Hunter Finish His Work The Transaction Details Will Be Printed On The Screen !!\n')

                counter = 15
                s = 1 
                while counter > 0:

                    try:

                        if counter == 1:

                            print(f'[!] Stage {s} Completed !, Please Wait 1 Minute To Start Stage {s + 1} ...\n')
                            time.sleep(60)
                            counter = 15
                            cls()
                            s = s + 1

                            print(f'[!] Stage {s} Started !\n')
                            continue

                        counter = counter - 1

                        try:

                            check = sess.get(all_urls['market'], params=search_data, headers=headers)

                            state = json.loads(check.text)['auctionInfo'][0]['tradeState']

                            buynowprice = json.loads(check.text)['auctionInfo'][0]['buyNowPrice']

                            if state == 'active':

                                buynowprice = int(buynowprice)

                                mxprice = int(mxprice)

                                if buynowprice <= mxprice:

                                    buynowprice = str(buynowprice)

                                    tradeID = json.loads(check.text)['auctionInfo'][0]['tradeId']

                                    player = f'https://utas.mob.v2.fut.ea.com/ut/game/fc24/trade/{tradeID}/bid'

                                    data = {
                                        'bid': f'{buynowprice}'
                                    }

                                    buy = sess.put(player, json=data, headers=headers)

                                    cls()

                                    print(f'\n\n[+] The Player Has Been Paurchased:\n\n\t\tPlayer Name: {targeted_player}\n\n\t\tPrice: {buynowprice}\n\n\t\tStage: {s}')
                                    
                                    input('\n\n[!] Press ENTER To Go Back To The Main Menu ')

                                    break

                                else:

                                    time.sleep(3)
                                    continue
                            else: # the player is not listed yet so keep search for him
                                time.sleep(3)
                                continue

                        except:
                            time.sleep(3)
                            continue

                    except KeyboardInterrupt:

                        break


if __name__ == '__main__':

    # install database file from github

    cls()
    colorama.init(convert=True)
    red = colorama.Fore.RED
    yellow = colorama.Fore.YELLOW
    blue = colorama.Fore.BLUE
    green = colorama.Fore.GREEN
    res = colorama.Fore.RESET

    print(f'{yellow}[+] {res}Please Wait While Installing The Players Database')

    install_packages()

    try:
        os.remove('fc24players.db')
        fc = download()


    except Exception as e:
        pass

    while True:

        cls()

        banner()

        attackers_players = {

        }


        midfielders_players = {

        }

        database = sqlite3.connect('fc24players.db')

        attackers(database)

        midfielders(database)

        avail_players = showPlayers(attackers_players, midfielders_players)

        action = input(f'''\n\n{yellow}[!] {res}Choose Action: 
                    
                    {green}({res}1{green}) {red}> {res}Hunt A Player
                    
                    {green}({res}2{green}) {red}> {res}Show The Available Players

                    {green}({res}3{green}) {red}> {res}Login (With EA Account)

                    {green}({res}4{green}) {red}> {res}UPDATE 
                              

{yellow}[!] {res}Enter The Action Number: ''')
        
        if action == '1':

            cls()

            try:

                with open('user_credentials.json', 'r', encoding='utf8') as f:

                    data = json.loads(f.read())

                    email = data['email']

                    password = data['password']

                    platform = data['platform']


                print(f'''{yellow}[*] Note:{res}
            The Player Must Be In The Players List
                    
{yellow}[*] Note:{res}
            Press ENTER To Go Back To The Main Menu''')
                player = input(f'\n\n{yellow}[!] {res}Type The Player Name You Want To Hunt {blue}(ex "Messi") {res}: ')

                if player == '':
                    continue

                player = player.title()

                if player in attackers_players:

                    print(f'\n\n{yellow}[!] {res}The Player Is {green}Available {res}For Hunt !')

                    mnprice = input(f'\n\n{yellow}[!] {res}Enter The {blue}Minimum {res}Price {green}$ {res}You Want To Purchase For: ')

                    mxprice = input(f'\n\n{yellow}[!] {res}Enter The {blue}Max {res}Price {green}$ {res}You Want To Purchase For: ')

                    pid = attackers_players[player]

                    cls()

                    print(f'{yellow}[*] Please Note: {res}The {blue}2FA {res}Must Be Enabled On Your {blue}EA Account {res}Otherwise The Tool Not Going To Work !!\n')

                    print(f'{yellow}={res}'*15, f'''\n\n{green}Player: {res}{player}\n\n{green}Minimum Price: {res}{mnprice}\n\n{green}Maximum Price: {res}{mxprice}\n\n''', f'{yellow}={res}'*15, '\n')

                    hunt(pid, mxprice, mnprice, email, password, platform, player)

                    continue

            except Exception as e:
                cls()
                print(e)
                print(f'\n{yellow}[!] {res}You Are {red}Not Logged In !!, {res}Please Log In With Your EA Account And Try Again.\n')

                input(f'\n\n{yellow}[!] {res}Press {blue}ENTER {res}To Go Back To The Main Menu ')

            else:

                print(f'\n{yellow}[!] {res}The Player Isn\'t Available For Now !!\n')
                time.sleep(3)
                continue

        elif action == '2':

            cls()

            display_players(avail_players)

            back = input('\n\n[!] Press ENTER To Go Back To The Main Menu ')

            continue

        elif action == '3':

            cls()

            try:

                with open('user_credentials.json', 'r', encoding='utf8') as f:

                    data = json.loads(f.read())

                    f.close()

                    print(f'''\n[!] You Already Logged In With These Credentials:\n
Email: {data['email']}\n\nPassword: {data['password']}\n''')
                    
                    action = input('''\n\n[!] Choose Action:
                        
                    [1] Log Out
                    
                    [2] Go Back

                                  
[!] Type Action Number: ''')

                    if action == '1':

                        os.remove('user_credentials.json')

                        cls()

                        print('\n[!] You Have Been Logged Out !')

                        input('\n\n[!] Press ENTER To Go Back To The Main Menu')
                    
                    else:
                        continue

            except Exception as e:

                print(f'{yellow}[*] {red}Please Note: {res}The 2FA Must Be Enabled By {green}Authenticator App {res}(Not By Email Or Phone Number) On Your EA Account Otherwise The Tool Not Going To Work !!\n')

                while True:

                    platform = input(f'\n{yellow}[!] {res}Select Your Platform:\n\n\t{green}({res}1{green}) {red}> {res}PC [STEAM]\n\n\t{green}({res}2{green}) {red}> {res}PC [EPIC GAMES]\n\n\t{green}({res}3{green}) {red}> {res}PS5\n\n\t{green}({res}4{green}) {red}> {res}PS4\n\n{yellow}[!] {res}Type Action Number: ')

                    if platform == '1':
                        pl = 'STEAM'
                        platform = 'FFA24STM'
                    
                    elif platform == '2':
                        cls()
                        continue
                    
                    elif platform == '3':
                        pl = 'PS5'
                        platform = 'FFA24PS5'
                    
                    elif platform == '4':
                        pl = 'PS4'
                        platform == 'FFA24PS4'
                    
                    else:
                        continue

                    cls()

                    print(f'\n{green}[+] Platform {res}==> {blue}{pl}{res}')

                    email = input(f'\n{yellow}[!] {blue}Your EA {res}Email: ')

                    password = input(f'\n{yellow}[!] {blue}Your EA {res}Password: ')

                    check_account(email, password, platform)

                    break
        
        elif action == '4':

            update()

        else:
            continue