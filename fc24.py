import cloudscraper
import time
import json
from bs4 import BeautifulSoup
import sqlite3
import os
import subprocess
from urllib.request import urlretrieve


def banner():


    print('''


 _______   ______     ___    _  _    
|   ____| /      |   |__ \  | || |   
|  |__   |  ,----'      ) | | || |_  
|   __|  |  |          / /  |__   _| 
|  |     |  `----.    / /_     | |   
|__|      \______|   |____|    |_|   
                                     



          
[!] Creator     ==> Sabah

[!] Instagram   ==> Apkaless
          
[!] Github      ==> https://github.com/apkaless
        
[!] Nationality ==> IRAQ

                 
''')
    


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




def check_account(email, password):

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
                        'password': f'{password}'
                    }

                    f.write(json.dumps(data))

                    f.close()

                print('\n\n[+] Your Credentials Are Saved To: user_credentials.json')

                input('\n\n[!] Press ENTER To Go Back To The Main Menu')

            else:
                print('\n[x] Your Credentials Are Incorrect, Please Check Your Information And Try Again !!')

                input('\n\n[!] Press ENTER To Go Back To The Main Menu')

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}               

pheaders = {

    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Host': 'gateway.ea.com'

}

def hunt(pid, mxprice, mnprice,email, password, targeted_player):


    with cloudscraper.create_scraper(debug=True) as sess:

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
                'gameSku': "FFA24PS5",
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

                print(sid_req.text)

                sid = json.loads(str(sid_req.text))['sid']

                headers['X-Ut-Sid'] = sid

                print(f'''
    Account Name: {accName}\n
    Club Name: {userClubName}\n
    Account Creation Date: {accdateCreated}\n
    Account State: {accstatus}\n
    Email State: {accemailstatus}\n
    ''')

                input('\n[!] Press Enter To Keep Going With Hunting ')

                os.system('cls')

                print('[!] The Hunter IS Running...\n\n[*] Please Leave The Hunter Doing His Work\n\n[*] When The Hunter Finish His Work The Transaction Details Will Be Printed On The Screen !!\n')

                counter = 15

                while counter > 0:

                    if counter == 1:
                        time.sleep(60)
                        counter = 15
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

                                os.system('cls')

                                print(f'\n\n[+] The Player Has Been Paurchased:\n\n\t\tPlayer Name: {targeted_player}\n\n\t\tPrice: {buynowprice}')
                                
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


if __name__ == '__main__':

    # install database file from github

    os.system('cls')

    print('[+] Please Wait While Installing The Players Database')

    try:

        fc = download()


    except Exception as e:
        pass

    while True:

        os.system('cls')

        banner()

        attackers_players = {

        }


        midfielders_players = {

        }

        database = sqlite3.connect('fc24players.db')

        attackers(database)

        midfielders(database)

        avail_players = showPlayers(attackers_players, midfielders_players)

        action = input('''\n\n[!] Choose Action: 
                    
                    [1] Hunt A Player
                    
                    [2] Show The Available Players

                    [3] Login (With EA Account) 
                              

[!] Enter The Action Number: ''')
        
        if action == '1':

            os.system('cls')

            # try:

            with open('user_credentials.json', 'r', encoding='utf8') as f:

                data = json.loads(f.read())

                email = data['email']

                password = data['password']

            print('''[*] Note:
                The Player Must Be In The Players List
                
[*] Note:
                Press ENTER To Go Back To The Main Menu''')
            player = input('\n\n[!] Type The Player Name You Want To Hunt (ex "Messi") : ')

            if player == '':
                continue

            player = player.title()

            if player in attackers_players:

                print('\n\n[!] The Player Is Available For Hunt !')

                mnprice = input('\n\n[!] Enter The minimum Price $ You Want To Purchase For: ')

                mxprice = input('\n\n[!] Enter The max Price $ You Want To Purchase For: ')

                pid = attackers_players[player]

                os.system('cls')

                print('[*] Please Note: The 2FA Must Be Enabled On Your EA Account Otherwise The Tool Not Going To Work !!\n')

                print('='*15, f'''\nPlayer: {player}\n\nFirst Price: {mnprice}\n\nSecond Price: {mxprice}\n\n''', '='*15, '\n')

                hunt(pid, mxprice, mnprice, email, password, player)

            # except Exception as e:

            #     print(e)

            #     print('\n[!] You Are Not Logged In !!, Please Log In With Your EA Account And Try Again.\n')

            #     input('\n\n[!] Press ENTER To Go Back To The Main Menu ')

            else:

                time.sleep(200)

        elif action == '2':

            os.system('cls')

            display_players(avail_players)

            back = input('\n\n[!] Press ENTER To Go Back To The Main Menu ')

            continue

        elif action == '3':

            os.system('cls')

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

                        os.system('cls')

                        print('\n[!] You Have Been Logged Out !')

                        input('\n\n[!] Press ENTER To Go Back To The Main Menu')
                    
                    else:
                        continue

            except Exception as e:

                print('[*] Please Note: The 2FA Must Be Enabled By Authenticator App (Not By Email Or Phone Number) On Your EA Account Otherwise The Tool Not Going To Work !!\n')

                email = input('\n[!] Email: ')

                password = input('\n[!] Password: ')

                check_account(email, password)

        else:
            continue