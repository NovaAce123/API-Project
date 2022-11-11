import logging
import urllib.request

log = logging.getLogger(__name__)

def get_url(url):
    reqinfo = urllib.request.urlopen(url)
    info = reqinfo.read()
    dec_info = info.decode("utf8")
    reqinfo.close()
    log.info("Requesting URL")
    return dec_info
