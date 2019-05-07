# -*- coding: cp1254 -*-
import zeep

d = dict()
d['GrupKodu'] = 0.0
d['KrediBanka'] = 0.0
d['KrediSube'] = 0.0
d['Police'] = 0.0
d['RequestBag'] = dict()
d['RequestBag']['Channel'] = 'FORMS'
d['RequestBag']['Client'] = 'BANKASSURUANCE'
d['RequestBag']['ClientSEQ'] = '16032111813213863299'
d['RequestBag']['CustomParameter'] = None
d['RequestBag']['HostSCR'] = None
d['RequestBag']['OperationCode'] = 'BKYP'
d['RequestBag']['Organization'] = 'BANK'
d['RequestBag']['Reference'] = None
d['RequestBag']['RequestTime']= dict()
d['RequestBag']['RequestTime']['DateTimeStr'] = '20190202111813'
d['UnitCode'] = '1234'
d['User'] = 'eauser'
d['Version'] = None
d['SorguBaslangic'] = None
d['SorguBitis'] = None
d['TcKimlikNo']= '12345678901'
d['sorguTipi'] = 'TcKimlik'

url = "https://uatservis/WCF/PoliceServisi.svc/Basic"
client = zeep.Client(url)
q = client.service.PoliceSorgula(d)

print len(q['policeler']['PoliceBilgileri']), u'tane poliçesi var:'
for p in q['policeler']['PoliceBilgileri']:
    print int(p['GrupKodu']), "-", int(p['PoliceNo']) 
