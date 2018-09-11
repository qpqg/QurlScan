from threading import Thread
from sys import exit
import requests
from modul.color import colorku
cl = colorku()
hijau = []
def sit(sites):
    if sites == "https://" or "http://":
        return sites.replace("https://","").replace("http://","")
def open_list(f):
    site = []
    try:
        with open(f) as files:
            for list_web in files.readlines():
                web = list_web.split("\n")[0]
                site.append(sit(web))
    except IOError:
        print cl.warning_red("PATH TIDAK DI KETAHUI")
        exit(0)
    scanning = cl.dflt_C("\n".join([str(i)+". "+site[i] for i in range(len(site))]))
    print cl.dflt_G("[+] ========== [ SITES ] =========== [+]")
    print scanning
    print cl.dflt_end()
    return  site
def goto(x):
    global code
    format = "http://" + x
    try:
        code = requests.get(format, allow_redirects=False, timeout=5)
        if code.status_code != 200:
            print cl.dflt_R(format)
            print cl.dflt_R("STATUS CODE: " + str(code.status_code))
        else:
            hijau.append(cl.dflt_G(format))
            print cl.dflt_G(format)
            print cl.dflt_G("STATUS CODE: "+str(code.status_code))
            try:
                log = "log.txt"
                with open(log, "a+") as save:
                    print "File Saved To: {}".format(log)
                    save.write(format + "\n")
                    save.close()
            except:
                print "Error Save File"
    except requests.exceptions.Timeout:
        print cl.dflt_R(format)
        print cl.dflt_R("TIME OUT")
    except:
        print cl.dflt_R(format)
        print cl.dflt_R("UNKNOWN ERROR")
def checking():
    expl = []
    for site in sit:
        for scan in open("urlscan").readlines():
            scan = scan.split("\n")[0]
            expl.append(site+scan)
    return expl
def start_all():
    t = []
    for i in range(len(checking())):
        th = Thread(target=goto, args=(checking()[i], ))
        t.append(th)
        th.start()
    [i.join()for i in t]
    print cl.dflt_end()
    if len(hijau) > 0:
        print "[+] ========== [ HIJO ] =========== [+]"
        print "\n".join([hijau[i] for i in range(len(hijau))])
    else:
        print cl.dflt_R("GA ADA IJO")
if __name__ == '__main__':
    cl.baleho(40,judul="Simple Url Scanner")
    print cl.help_B("input path file, Example: c://site.txt")
    f = raw_input(cl.dflt_O(" > ")+'\033[34m')
    sit = open_list(f)
    start_all()
