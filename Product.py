#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import pytz
class CustomerItems(object):
    def __init__(self,plu,name,desc,price,eventtypeid):
        self.plu = plu
        self.name = name
        self.desc = desc
        self.price = price
        self.details = []
        self.eventtypeid = eventtypeid

    def AddPackage(self,pkg):
        if isinstance(pkg,CustomerItems):
            self.details.append(pkg)
            return True
        return False
    
    def GetName(self):
        return self.name

    def GetPrice(self):
        return self.price

    def GetDesc(self):
        return self.desc

    def GetPLU(self):
        return self.plu
    
    def GetEventTypeID(self):
        return self.eventtypeid

    def GetPackagePLU(self):
        details = []
        if self.details:
            for d in self.details:
                details.append(d.GetPLU())
        return details

    def GetDetails(self):
        details = []
        if self.details:
            for d in self.details:
                details.append('PLU:{0}, Name:{1}, Desc:{2}, Price:{3}, EventTypeID:{4} Details:{5}'.format(d.GetPLU(),d.GetName(),d.GetDesc(),d.GetPrice(),d.GetEventTypeID(),'None'))
        if details:
            return details
        else:
            return 'None'

    def __str__(self):
        return 'PLU:{0}, Name:{1}, Desc:{2}, Price:{3}, EventTypeID:{4} Details:{5}'.format(self.plu,self.name,self.desc,self.price,self.eventtypeid,self.GetDetails())
    
class PricingProduct(object):
    def __init__(self,plu,eventid):
        self.plu = plu
        self.eventid = eventid
        self.details = []

    def FormatSelf(self):
        if self.HasDetails():
            detail = []
            for d in self.details:
                detail.append(d.FormatSelf())
            return 'PLU:{0}, EventID:{1}, Details:{2}'.format(self.plu,self.eventid,detail)
        else:
            return 'PLU:{0}, EventID:{1}, Details:{2}'.format(self.plu,self.eventid,'None')
    
    def GetEventID(self):
        return self.eventid

    def GetPLU(self):
        return self.plu

    def GetDetailsPLU(self):
        details = []
        for d in self.details:
            details.append(d.GetPLU())
        return details

    def GetPLUFromEventID(self,inputeventid):
        if self.eventid == inputeventid:
            return {'PLU':self.plu,'EventID':self.eventid,'Details':[]}
        elif self.HasDetails():
            for d in self.details:
                d1 = d.GetPLUFromEventID(inputeventid)
                if d1:
                    return {'PLU':self.plu,'EventID':self.eventid,'Details':self.GetDetailsPLU()}
        else: 
            return None
    
    def GetPLUListFromEventIDList(self,eventidlist):
        details = []
        if self.HasDetails():
            for eid in eventidlist:
                for d in self.details:
                    if d.GetEventID() == eid:
                        details.append({'PLU':d.GetPLU(),'EventID':d.GetEventID()})
            return {'PLU':self.plu,'EventID':self.eventid,'details':details}
        else:
            for eid in eventidlist:
                if self.eventid == eid:
                    return {'PLU':self.plu,'EventID':self.eventid,'details':details}
        return None

    def UpdateEventID(self,eventid):
        self.eventid = eventid
        
    def AddDetails(self,pkd):
        self.details.append(pkd)
    
    def HasDetails(self):
        if self.details or len(self.details):
            return True
        return False


class Events(object):
    def __init__(self,eventid,eventtypeid,eventname,startdate):
        self.eventid = eventid
        self.eventtypeid = eventtypeid
        self.eventname = eventname
        self.startdate = startdate
    
    def get_startdate(self):
        return self.startdate[0:10]

    def get_eventid(self):
        return self.eventid

    def __str__(self):
        return 'EventID:{0}, EventTypeID:{1}, EventName:{2}, StartDate:{3}'.format(self.eventid,self.eventtypeid,self.eventname,self.startdate)

def get_visitdate_utc(startdate):
    visitdate = startdate + ' 00:00:00+0800'
    date = datetime.strptime(visitdate, '%Y-%m-%d %H:%M:%S%z')
    visitday = date.astimezone(pytz.timezone('UTC'))
    return visitday.strftime('%Y-%m-%dT%H:%M:%SZ')

def get_visitdate_shanghai(utcdate):
    visitdate = utcdate[0:18] + '+0000'
    date = datetime.strptime(visitdate, '%Y-%m-%dT%H:%M:%S%z')
    visitday = date.astimezone(pytz.timezone('Asia/Shanghai'))
    return visitday.strftime('%Y-%m-%d')

'''
for tz in pytz.all_timezones:
    print tz
'''
if __name__ == "__main__":
    print(get_visitdate_shanghai('2020-02-28T16:00:00Z'))
    #for tz in pytz.all_timezones:
    #    print(tz)