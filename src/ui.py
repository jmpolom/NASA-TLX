# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

"""
NASA-TLX implementation with wxWidgets

Copyright (C) 2011 Jon Polom <jmpolom@wayne.edu>
See 'COPYING' in the src directory for license terms
"""

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcmainFrame(wx.Frame):
#!XRCED:begin-block:xrcmainFrame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcmainFrame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "mainFrame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.rdoPD1 = xrc.XRCCTRL(self, "rdoPD1")
        self.rdoMD1 = xrc.XRCCTRL(self, "rdoMD1")
        self.rdoTD1 = xrc.XRCCTRL(self, "rdoTD1")
        self.rdoMD2 = xrc.XRCCTRL(self, "rdoMD2")
        self.rdoOP1 = xrc.XRCCTRL(self, "rdoOP1")
        self.rdoMD3 = xrc.XRCCTRL(self, "rdoMD3")
        self.rdoFR1 = xrc.XRCCTRL(self, "rdoFR1")
        self.rdoMD4 = xrc.XRCCTRL(self, "rdoMD4")
        self.rdoEF1 = xrc.XRCCTRL(self, "rdoEF1")
        self.rdoMD5 = xrc.XRCCTRL(self, "rdoMD5")
        self.rdoTD2 = xrc.XRCCTRL(self, "rdoTD2")
        self.rdoPD2 = xrc.XRCCTRL(self, "rdoPD2")
        self.rdoOP2 = xrc.XRCCTRL(self, "rdoOP2")
        self.rdoPD3 = xrc.XRCCTRL(self, "rdoPD3")
        self.rdoFR2 = xrc.XRCCTRL(self, "rdoFR2")
        self.rdoPD4 = xrc.XRCCTRL(self, "rdoPD4")
        self.rdoEF2 = xrc.XRCCTRL(self, "rdoEF2")
        self.rdoPD5 = xrc.XRCCTRL(self, "rdoPD5")
        self.rdoTD3 = xrc.XRCCTRL(self, "rdoTD3")
        self.rdoOP3 = xrc.XRCCTRL(self, "rdoOP3")
        self.rdoTD4 = xrc.XRCCTRL(self, "rdoTD4")
        self.rdoFR3 = xrc.XRCCTRL(self, "rdoFR3")
        self.rdoTD5 = xrc.XRCCTRL(self, "rdoTD5")
        self.rdoEF3 = xrc.XRCCTRL(self, "rdoEF3")
        self.rdoOP4 = xrc.XRCCTRL(self, "rdoOP4")
        self.rdoFR4 = xrc.XRCCTRL(self, "rdoFR4")
        self.rdoOP5 = xrc.XRCCTRL(self, "rdoOP5")
        self.rdoEF4 = xrc.XRCCTRL(self, "rdoEF4")
        self.rdoEF5 = xrc.XRCCTRL(self, "rdoEF5")
        self.rdoFR5 = xrc.XRCCTRL(self, "rdoFR5")
        self.mentalMagSlider = xrc.XRCCTRL(self, "mentalMagSlider")
        self.physicalMagSlider = xrc.XRCCTRL(self, "physicalMagSlider")
        self.temporalMagSlider = xrc.XRCCTRL(self, "temporalMagSlider")
        self.perfMagSlider = xrc.XRCCTRL(self, "perfMagSlider")
        self.effortMagSlider = xrc.XRCCTRL(self, "effortMagSlider")
        self.frustrMagSlider = xrc.XRCCTRL(self, "frustrMagSlider")
        self.scoreTxt = xrc.XRCCTRL(self, "scoreTxt")

        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoPD1, self.rdoPD1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoMD1, self.rdoMD1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoTD1, self.rdoTD1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoMD2, self.rdoMD2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoOP1, self.rdoOP1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoMD3, self.rdoMD3)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoFR1, self.rdoFR1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoMD4, self.rdoMD4)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoEF1, self.rdoEF1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoMD5, self.rdoMD5)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoTD2, self.rdoTD2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoPD2, self.rdoPD2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoOP2, self.rdoOP2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoPD3, self.rdoPD3)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoFR2, self.rdoFR2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoPD4, self.rdoPD4)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoEF2, self.rdoEF2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoPD5, self.rdoPD5)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoTD3, self.rdoTD3)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoOP3, self.rdoOP3)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoTD4, self.rdoTD4)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoFR3, self.rdoFR3)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoTD5, self.rdoTD5)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoEF3, self.rdoEF3)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoOP4, self.rdoOP4)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoFR4, self.rdoFR4)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoOP5, self.rdoOP5)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoEF4, self.rdoEF4)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoEF5, self.rdoEF5)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_rdoFR5, self.rdoFR5)
        self.Bind(wx.EVT_SCROLL, self.OnScroll_mentalMagSlider, self.mentalMagSlider)
        self.Bind(wx.EVT_SCROLL, self.OnScroll_physicalMagSlider, self.physicalMagSlider)
        self.Bind(wx.EVT_SCROLL, self.OnScroll_temporalMagSlider, self.temporalMagSlider)
        self.Bind(wx.EVT_SCROLL, self.OnScroll_perfMagSlider, self.perfMagSlider)
        self.Bind(wx.EVT_SCROLL, self.OnScroll_effortMagSlider, self.effortMagSlider)
        self.Bind(wx.EVT_SCROLL, self.OnScroll_frustrMagSlider, self.frustrMagSlider)

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoPD1
    def OnRadiobutton_rdoPD1(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoPD1()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoPD1        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoMD1
    def OnRadiobutton_rdoMD1(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoMD1()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoMD1        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoTD1
    def OnRadiobutton_rdoTD1(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoTD1()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoTD1        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoMD2
    def OnRadiobutton_rdoMD2(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoMD2()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoMD2        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoOP1
    def OnRadiobutton_rdoOP1(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoOP1()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoOP1        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoMD3
    def OnRadiobutton_rdoMD3(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoMD3()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoMD3        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoFR1
    def OnRadiobutton_rdoFR1(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoFR1()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoFR1        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoMD4
    def OnRadiobutton_rdoMD4(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoMD4()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoMD4        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoEF1
    def OnRadiobutton_rdoEF1(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoEF1()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoEF1        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoMD5
    def OnRadiobutton_rdoMD5(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoMD5()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoMD5        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoTD2
    def OnRadiobutton_rdoTD2(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoTD2()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoTD2        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoPD2
    def OnRadiobutton_rdoPD2(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoPD2()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoPD2        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoOP2
    def OnRadiobutton_rdoOP2(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoOP2()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoOP2        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoPD3
    def OnRadiobutton_rdoPD3(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoPD3()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoPD3        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoFR2
    def OnRadiobutton_rdoFR2(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoFR2()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoFR2        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoPD4
    def OnRadiobutton_rdoPD4(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoPD4()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoPD4        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoEF2
    def OnRadiobutton_rdoEF2(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoEF2()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoEF2        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoPD5
    def OnRadiobutton_rdoPD5(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoPD5()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoPD5        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoTD3
    def OnRadiobutton_rdoTD3(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoTD3()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoTD3        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoOP3
    def OnRadiobutton_rdoOP3(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoOP3()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoOP3        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoTD4
    def OnRadiobutton_rdoTD4(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoTD4()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoTD4        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoFR3
    def OnRadiobutton_rdoFR3(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoFR3()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoFR3        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoTD5
    def OnRadiobutton_rdoTD5(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoTD5()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoTD5        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoEF3
    def OnRadiobutton_rdoEF3(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoEF3()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoEF3        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoOP4
    def OnRadiobutton_rdoOP4(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoOP4()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoOP4        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoFR4
    def OnRadiobutton_rdoFR4(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoFR4()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoFR4        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoOP5
    def OnRadiobutton_rdoOP5(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoOP5()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoOP5        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoEF4
    def OnRadiobutton_rdoEF4(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoEF4()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoEF4        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoEF5
    def OnRadiobutton_rdoEF5(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoEF5()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoEF5        

#!XRCED:begin-block:xrcmainFrame.OnRadiobutton_rdoFR5
    def OnRadiobutton_rdoFR5(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_rdoFR5()"
#!XRCED:end-block:xrcmainFrame.OnRadiobutton_rdoFR5        

#!XRCED:begin-block:xrcmainFrame.OnScroll_mentalMagSlider
    def OnScroll_mentalMagSlider(self, evt):
        # Replace with event handler code
        print "OnScroll_mentalMagSlider()"
#!XRCED:end-block:xrcmainFrame.OnScroll_mentalMagSlider        

#!XRCED:begin-block:xrcmainFrame.OnScroll_physicalMagSlider
    def OnScroll_physicalMagSlider(self, evt):
        # Replace with event handler code
        print "OnScroll_physicalMagSlider()"
#!XRCED:end-block:xrcmainFrame.OnScroll_physicalMagSlider        

#!XRCED:begin-block:xrcmainFrame.OnScroll_temporalMagSlider
    def OnScroll_temporalMagSlider(self, evt):
        # Replace with event handler code
        print "OnScroll_temporalMagSlider()"
#!XRCED:end-block:xrcmainFrame.OnScroll_temporalMagSlider        

#!XRCED:begin-block:xrcmainFrame.OnScroll_perfMagSlider
    def OnScroll_perfMagSlider(self, evt):
        # Replace with event handler code
        print "OnScroll_perfMagSlider()"
#!XRCED:end-block:xrcmainFrame.OnScroll_perfMagSlider        

#!XRCED:begin-block:xrcmainFrame.OnScroll_effortMagSlider
    def OnScroll_effortMagSlider(self, evt):
        # Replace with event handler code
        print "OnScroll_effortMagSlider()"
#!XRCED:end-block:xrcmainFrame.OnScroll_effortMagSlider        

#!XRCED:begin-block:xrcmainFrame.OnScroll_frustrMagSlider
    def OnScroll_frustrMagSlider(self, evt):
        # Replace with event handler code
        print "OnScroll_frustrMagSlider()"
#!XRCED:end-block:xrcmainFrame.OnScroll_frustrMagSlider        




# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    __res.Load('ui.xrc')
