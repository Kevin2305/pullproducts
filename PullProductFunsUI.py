#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,base64,sys,json
from requests import post
import datetime,xmltodict
from Product import CustomerItems,Events,PricingProduct,get_visitdate_utc,get_visitdate_shanghai
initData={}
conffile='pullproducts.txt'
querycustomercmd='QueryCustomerItems_cmd.txt'
queryeventscmd='QueryEvents_cmd.txt'
eGalaxylog='eGalaxy_log.txt'
pricinglog='pricing_log.txt'
messageidcount=0
def InitData():
    global initData
    if not os.path.exists(conffile):
        print("no config file, exiting")
        sys.exit(1)
    with open(conffile,"r") as f:
        initData["egalaxyurl"] = f.readline().replace("\n","").split("==")[1]
        initData["pricingurl"] = f.readline().replace("\n","").split("==")[1]
        initData["auth"] = f.readline().replace("\n","").split("==")[1]
        initData["plu"] = f.readline().replace("\n","").split("==")[1]
        initData["startdate"] = f.readline().replace("\n","").split("==")[1]
        initData["enddate"] = f.readline().replace("\n","").split("==")[1]
        initData["customerid"] = f.readline().replace("\n","").split("==")[1]
        initData["timeout"] = f.readline().replace("\n","").split("==")[1]

def QueryCustomer(egalayurl,timeout,plulistfromui,customerid):
    if not os.path.exists(querycustomercmd):
        return {'error':'no query customer cmd file'}
    with open(querycustomercmd,'r') as f:
        queryxml=f.readlines()
    queryxml=''.join(queryxml)
    response = ExecQueryeGal(queryxml,egalayurl,timeout,customerid)
    return FindPLUInfo(response,plulistfromui)

def QueryEventID(querycustomerresult,sdate,edate,egalayurl,timeout,customerid):
    if not os.path.exists(queryeventscmd):
        return ({'error':'no query event cmd file'},'')
    with open(queryeventscmd,'r') as f:
        queryxml=f.readlines()
    queryxml=''.join(queryxml)
    queryxml=queryxml.replace('$startdate$',str(sdate +' 00:00:00'))
    queryxml=queryxml.replace('$enddate$',str(edate +' 23:59:59'))
    tickets = ''
    for product in querycustomerresult:
        ticket = '\n\t<Ticket>\
                  \n\t\t\t<PLU>$plu$</PLU>\
                  \t\t\t<Price>$pricing$</Price>\n\
				  <UpdateStatus>0</UpdateStatus>\n\
				  </Ticket>\n'
        ticket=ticket.replace('$plu$',str(product.plu))
        tickets = tickets + ticket.replace('$pricing$',product.price)
    queryxml = queryxml.replace('$tickets$',tickets)
    queryeventsresponse = ExecQueryeGal(queryxml,egalayurl,timeout,customerid)
    return FindEventID(queryeventsresponse), FindProducts(queryeventsresponse)
    


def GetCurTime():
    return datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

def ExecQueryeGal(querycmd,egalayurl,timeout,customerid):
    global messageidcount
    querycmd=querycmd.replace('$messageid$',str(messageidcount+1))
    querycmd=querycmd.replace('$timestamp$',GetCurTime())
    querycmd=querycmd.replace('$customerid$',customerid)
    headers = {'Content-Type':'application/xml','charset':'utf-8'}
    r = post(egalayurl,data=querycmd,headers=headers,timeout=int(timeout))
    if r.status_code == 200:
        with open(eGalaxylog,'a',encoding='utf-8') as f:
            f.write(querycmd)
            f.write('\n')
            f.write(r.text)
        return r.text
    else:
        with open(eGalaxylog,'a') as f:
            f.write('eGalaxy Connection Error')


def ExecQueryPricing(querycmds,pricingurl,timeout,auth):
    with open('Result_NoPackageProducts.txt','w',encoding='utf-8') as f:
        f.write('VisitDate,ProductCode,ProductName,Price,EventID\n')
    with open('Result_PackageProducts.txt','w',encoding='utf-8') as f:
        f.write('VisitDate,ProductCode,ProductName,Price,EventID,pkgProductCode,pkgProductName,pkgPrice,pkgEventID\n')
    headers = {'Content-Type':'application/json','charset':'utf-8','Authorization':auth}
    for cmd in querycmds:
        jsoncmd = json.dumps(cmd)
        #print(jsoncmd)
        r = post(pricingurl,data=jsoncmd,headers=headers,timeout=int(timeout))
        if r.status_code == 200:
            with open(pricinglog,'a',encoding='utf-8') as f:
                f.write('request: {}'.format(jsoncmd))
                f.write('\n')
                f.write('response: {}'.format(r.text))
                f.write('\n\n')
            ParsePricingResponse(r.text)
        else:
            with open(pricinglog,'a') as f:
                f.write('Pricing Connection Error')

def ParsePricingResponse(pricingresponse):
    a = json.loads(pricingresponse)
    for p in a['products']:
        if p.get('details'):
            pkgdetails = set()
            for d in p['details']:
                pkgdetails.update(['{},{},{},{}'.format(d['productCode'],d['productName'],d['total'],d['eventId'])])
            for pkg in pkgdetails:
                pg = pkg.split(',')
                with open('Result_PackageProducts.txt','a',encoding='utf-8') as f:
                    f.write('{0},{1},{2},{3},{4},{5},{6},{7},{8}\n'.format(\
                        get_visitdate_shanghai(a['visitDate']),\
                        p['productCode'],\
                        p['productName'],\
                        p['total'],\
                        p['eventId'],\
                        pg[0],\
                        pg[1],\
                        pg[2],\
                        pg[3])\
                        )
        else:
            with open('Result_NoPackageProducts.txt','a',encoding='utf-8') as f:
                f.write('{0},{1},{2},{3},{4}\n'.format(\
                    get_visitdate_shanghai(a['visitDate']),\
                    p['productCode'],\
                    p['productName'],\
                    p['total'],\
                    p['eventId'])\
                    )

def FindPLUInfo(responsexml,plulistfromui):    
    if XMLtoDict(responsexml)['Envelope']['Body']['ItemList'] == None:
        return {'error':'no products in response xml'}
    rdict = XMLtoDict(responsexml)['Envelope']['Body']['ItemList']['Item']
    if plulistfromui != '*':
        plus = (plulistfromui +',').split(',')
        plus.remove('')
        plulist = set(plus)
    else:
        plulist = ''
    pluqueried = []
    if plulist:
        for r in rdict:
            sub = (r['PLU']+',').split(',')
            sub.remove('')
            if plulist.intersection(set(sub)):
                if r.get('EventTypeID'):
                    eventtypeid = r['EventTypeID']
                else:
                    eventtypeid = 0
                a = CustomerItems( r['PLU'] , r['Name'] , r['Description'] , r['Price'] , eventtypeid)
                if r.get('PackageDetails'):
                    for d in r['PackageDetails']['PackageDetail']:
                        if d.get('EventTypeID'):
                            eventtypeid = d['EventTypeID']
                        else:
                            eventtypeid = 0
                        a.AddPackage(CustomerItems( d['PLU'],d['Name'],d['Description'],d['Price'],eventtypeid ))
                pluqueried.append(a)
    else:
        for r in rdict:
            if r.get('EventTypeID'):
                eventtypeid = r['EventTypeID']
            else:
                eventtypeid = 0
            a = CustomerItems( r['PLU'] , r['Name'] , r['Description'] , r['Price'], eventtypeid )
            if r.get('PackageDetails'):
                for d in r['PackageDetails']['PackageDetail']:
                    if d.get('EventTypeID'):
                        eventtypeid = d['EventTypeID']
                    else:
                        eventtypeid = 0
                    a.AddPackage(CustomerItems( d['PLU'],d['Name'],d['Description'],d['Price'] , eventtypeid ))
            pluqueried.append(a)
    return pluqueried

def ReOrgEventIDandVisitDate(eventsobjects):
    visitdateandeventid = {}
    for eob in eventsobjects:
        if not visitdateandeventid.get(eob.get_startdate()):
            visitdateandeventid[eob.get_startdate()] = []
        visitdateandeventid[eob.get_startdate()].append( eob.get_eventid() )
    return visitdateandeventid

def FindEventID(queryeventsresponse):
    if XMLtoDict(queryeventsresponse)['Envelope']['Body']['Events'] == None:
        return {'error':'No Event ID in respons'}
    rdict = XMLtoDict(queryeventsresponse)['Envelope']['Body']['Events']['Event']
    l = []
    for rd in rdict:
        l.append( Events(rd['EventID'],rd['EventTypeID'],rd['EventName'],rd['StartDateTime']) )
    return l

def FindProducts(queryeventsresponse):
    if XMLtoDict(queryeventsresponse)['Envelope']['Body']['Pricing'] == None:
        return {'error':'No Pricing Tag in response'}
    rdict = XMLtoDict(queryeventsresponse)['Envelope']['Body']['Pricing']['Tickets']['Ticket']
    #print(type(rdict))
    if not isinstance(rdict,list):
        l = []
        l.append(rdict)
        print('not list')
        rdict = l
    products = []
    #print(type(rdict))
    for d in rdict:
        #print(d)
        if d.get('PackageDetails'):
            a = None
            a = PricingProduct(d['PLU'],0)
            if d['PackageDetails']['PackageDetail'].get('Events'):
                d1 = d['PackageDetails']['PackageDetail']['Events']['Event']
            else:
                continue

            if not isinstance(d1,list):
                l = []
                l.append(d1)
                d1 = l
            for dd in d1:
                a.AddDetails(PricingProduct(d['PackageDetails']['PackageDetail']['PLU'],dd['EventID']))
            #print(a.FormatSelf())
            products.append(a)
        elif d.get('Events'):
            d2 = d['Events']['Event']
            if not isinstance(d2,list):
                l = []
                l.append(d2)
                d2 = l
            for li in d2:
                #print(li)
                c = PricingProduct( d['PLU'] , li['EventID'] )
                #print(c.FormatSelf())
                products.append(c)
        else:
            products.append( PricingProduct(d['PLU'] , 0) )
    return products

def MakePricingRequest(reorgedeventsid,inputproducts,customeritems,custid):
    pricingcmds = []
    #id = 1
    for visitdate,eventidlist in reorgedeventsid.items():
        products = []
        for p in inputproducts:
            validplu = p.GetPLUListFromEventIDList(eventidlist)
            if validplu and validplu['details']:
                for cusitem in customeritems:
                    if cusitem.GetPLU() == validplu['PLU']:
                        cusdetails = cusitem.GetPackagePLU()
                        validpludetails = validplu['details']
                        detailproduct = []
                        for cusd in cusdetails:
                            for validplud in validpludetails:
                                if cusd == validplud['PLU']:
                                    detailproduct.append({"quantity":1,"eventId":int(validplud['EventID']),"productCode":validplud['PLU']})
                                    flag = False
                            if flag:
                                detailproduct.append({"quantity":1,"eventId":0,"productCode":cusd})
                            flag = True
                products.append({"quantity":1,"eventId":0,"productCode":validplu['PLU'],"details":detailproduct})
            if validplu and (not validplu['details']):
                products.append({"quantity":1,"eventId":int(validplu['EventID']),"productCode":validplu['PLU']})
        pricingcmds.append({'visitdate':get_visitdate_utc(visitdate),"salesProgramId": 0,"customerId":custid,"products":products})
    return pricingcmds

def WriteGAProducts(customeritemresult):
    with open('Result_GAProducts.txt','w',encoding='utf-8') as f:
        f.write('{0},{1},{2}\n'.format(\
            'ProductCode',\
            'ProductName',\
            'Price')\
            )
    for customeritem in customeritemresult:
        if customeritem.GetEventTypeID() == 0 and customeritem.GetDetails() == 'None':
            with open('Result_GAProducts.txt','a',encoding='utf-8') as f:
                f.write('{0},{1},{2}\n'.format(\
                    customeritem.GetPLU(),\
                    customeritem.GetName(),\
                    customeritem.GetPrice())\
                    )

def ToBase64Encode(mingwen):
    try:
        aw=mingwen
        if len(aw)>0:
            miwen=base64.b64encode(aw.encode('utf-8')).decode('utf-8')
            return miwen
    except Exception:
        return None

def ToPlainText(miwen):
    try:
        bw=miwen
        if len(bw)>0:
            mingwen=base64.b64decode(bw).decode('utf-8')
            return mingwen
    except Exception:
        return None

def XMLtoDict(xml):
    return xmltodict.parse(xml,encoding='utf-8')

def CleanLogFile():
    if os.path.exists(eGalaxylog):
        os.remove(eGalaxylog)
    if os.path.exists(pricinglog):
        os.remove(pricinglog)
    return 'log files cleaned...'

def Run():
    print('Clean Logs...')
    CleanLogFile()
    InitData()
    print('\nQuery Customer Items...\n')
    customeritems = QueryCustomer(initData['egalaxyurl'],initData['timeout'],initData['plu'],initData['customerid'])
    for c in customeritems:
        print(c)
    print('\nQuery Events...\n')
    eventids,products = QueryEventID(customeritems,initData['startdate'],initData['enddate'],initData['egalaxyurl'],initData['timeout'],initData['customerid'])
    for e in eventids:
        print(e)
    print('\nProduct Events...\n')
    for p in products:
        print(p.FormatSelf())
    reorgedeventids = ReOrgEventIDandVisitDate(eventids)
    print('\nQuery Pricing...\n')
    pricingcmds = MakePricingRequest(reorgedeventids,products,customeritems,initData['customerid'])
    print('\nWriting Files...\n')
    ExecQueryPricing(pricingcmds,initData['pricingurl'],initData['timeout'],initData['auth'])
    WriteGAProducts(customeritems)
    print('Completed.')


