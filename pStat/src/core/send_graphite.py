#encoding=utf-8
'''
Created on 2014.8.27

@author: guanzx
'''

from graphite_client import StatsdClient

def sendPubAndMcRequest(pub_count,mc_count):
#     client = StatsdClient()   
#     client.gauge('microlens.hermes.pub.request', pub_count)
#     client.gauge('microlens.hermes.mc.request', mc_count)
    print pub_count,mc_count


def sendDataToGraphite(pub_tt_pdata,pub_tr_pdata,mc_tt_pdata,mc_tr_pdata):
    
    pubPath = "microlens.hermes.pub.%s"
    mcPath = "microlens.hermes.mc.%s"

    data = {}
    for key in pub_tt_pdata:
        data[pubPath % (key)] = pub_tt_pdata[key]
    for key in pub_tr_pdata:
        data[pubPath % (key)] = pub_tr_pdata[key]
    for key in mc_tt_pdata:
        data[mcPath % (key)] = mc_tt_pdata[key]
    for key in mc_tr_pdata:
        data[mcPath % (key)] = mc_tr_pdata[key]
    print data
#     dstAddr = ("192.168.112.50", 8125)
#     StatsdClient.send(data, dstAddr)
    
    
        
        
        