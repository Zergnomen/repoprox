#!/usr/bin/python3
import flask
import configparser
import urllib.request
import hashlib
import os
import os.path
proxyPort = os.getenv('PROXY_PORT', 5000)
myConfile = '../etc/repoprox.conf'
myConf = configparser.RawConfigParser()
try:
    myConf.read( myConfile )
except configparser.MissingSectionHeaderError:
    print("Missing section in %s" % myConfile)
    exit(1)

fileprefix = myConf.get('storage', 'storagepath')
def return_paths():
    returen = ''
    for a in myConf.items("paths"):
        returen = returen +"%s\t%s\n" % (a[0], a[1])
    return(returen)

def fetchdata(repopath, filehash, fetchpay):
    #needs check
    return(200)


app = flask.Flask(__name__)

@app.route("/")
def usage():
    return(return_paths())

@app.route('/<repopath>//<path:fetchpay>')
@app.route('/<repopath>/<path:fetchpay>')
def get(repopath,fetchpay):
    if(myConf.has_option("paths",repopath)):
        filehash = hashlib.sha256(repopath.encode('utf-8') + 
                                  fetchpay.encode('utf-8')).hexdigest() 
        if not os.path.isfile(fileprefix + filehash):
            url = myConf.get("paths",repopath) + fetchpay
            try:
                if(myConf.has_section('debug')):
                   print(fetchpay)
                urllib.request.urlretrieve(url, fileprefix + filehash)
            except:
                return flask.abort(404)
        if(myConf.has_section('debug')):
           print(filehash)
        return flask.send_from_directory(directory=fileprefix, filename=filehash)
    else:
        return(return_paths())



if __name__ == '__main__':
    app.run(port=proxyPort)
