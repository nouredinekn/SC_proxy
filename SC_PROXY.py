import requests
import webbrowser
# my banner with my any  info
print(''' \033[01m
\033[91m
███╗   ██╗ ██████╗ ██╗   ██╗██████╗ ███████╗██████╗ ██╗███╗   ██╗███████╗
████╗  ██║██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔══██╗██║████╗  ██║██╔════╝
██╔██╗ ██║██║   ██║██║   ██║██████╔\033[31m╝█████╗  ██║  ██║██║██╔██╗ ██║█████╗  
██║╚██╗██║██║   ██║██║   ██║██╔══██╗██╔══╝  ██║  ██║██║██║╚██╗██║██╔══╝  
██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║███████╗██████╔╝██║██║ ╚████║███████╗
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
\033[94m                                                                      
███████╗ ██████╗        ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗       
██╔════╝██╔════╝        ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝       
███████╗██║             ██████╔\033[96m╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝        
╚════██║██║             ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝         
███████║╚██████╗███████╗██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║          
╚══════╝ ╚═════╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝          
 \033[36m                                                                  
--------------------------------------------------------------------------------------------
       \033[91m [\033[93m ! \033[91m] \033[35m NAME: \033[34m NOUREDINE KAOINE
       \033[91m [\033[93m ! \033[91m] \033[35m USER: \033[34mNOUREDINE_KN 
  \033[91m [\033[93m ! \033[91m] \033[35mTELEGRAM-USER: \033[34m https://t.me/n2k4n
       \033[91m [\033[93m ! \033[91m] \033[35mCHANEL: \033[34m https://t.me/nkcp_tm
    \033[91m [\033[93m ! \033[91m] \033[35m YT:\033[34m NOUREDINE KAOINE
    \033[91m [\033[93m ! \033[91m] \033[35mgithub: \033[34mhttps://github.com/nouredinekn
\033[36m''')
 #for get my  github
webbrowser.open('https://github.com/nouredinekn')
 #for chose type proxy
print(f'''  \033[36m  
--------------------------------------------------------------------------------------------
                         \033[93mCHOSE TYPE OF YOUR PROXY\033[36m  
--------------------------------------------------------------------------------------------
              \033[91m [\033[93m 1 \033[91m] \033[0m \033[01mhttp \033[01m
              \033[91m [\033[93m 2 \033[91m] \033[0m \033[01mhttps \033[01m
              \033[91m [\033[93m 3 \033[91m] \033[0m \033[01msocks4 \033[01m
              \033[91m [\033[93m 4 \033[91m] \033[0m \033[01msocks5 \033[01m
              \033[91m [\033[93m 5 \033[91m] \033[0m \033[01msocks \033[01m\033[36m 
--------------------------------------------------------------------------------------------
''')
#for input type proxy
x=int(input(' \033[0m \033[01m[\033[93m \033[01m!\033[0m \033[01m] \033[91mENTRE  NUMBER OF YOUR PROXY:\t\033[0m \033[01m'))
#scraping proxy
if x==5:
    url = 'https://www.socks-proxy.net/'
    r = requests.get(url).text
    sp = r.split('''onclick="select(this)">Free socks proxies from socks-proxy.net''')[1].split('</textarea></div>')[0]
    update = sp.split('UTC.')[0]
    proxy = sp.split('UTC.')[1]
    with  open('socks[NOUREDINE_KN].txt', 'w') as rusalt:
        rusalt.write(proxy)
    print("\033[36m  -------------> \033[92mYOUR PROXY SAVE AS socks[NOUREDINE_KN].txt")
else:
    proxy = ['http', 'https', 'socks4', 'socks5']
    url = f'https://www.proxy-list.download/api/v1/get?type={proxy[x + 1]}'
    r = requests.get(url).text
    with  open(f'{proxy[x+1]}[NOUREDINE_KN].txt', 'w') as rusalt:
        rusalt.write(r)
    print(f"\033[36m  -----------> \033[92mYOUR PROXY SAVE AS {proxy[x+1]}[NOUREDINE_KN].txt")
