#!/usr/bin/python

#
# NASA-TLX python implementation with wxWidgets
#
# Copyright (C) 2011 Jon Polom <jmpolom@wayne.edu>
#
# See 'COPYING' in the src directory for license terms
#

import wx
from ui import xrcmainFrame

class tlxMainFrame(xrcmainFrame):

    def __init__(self):
        xrcmainFrame.__init__(self, parent=None)
        self.Show()
        self.calcScore()

    # there has to be a better way... maybe later...
    def OnRadiobutton_rdoPD1(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoMD1(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoTD1(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoMD2(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoOP1(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoMD3(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoFR1(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoMD4(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoEF1(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoMD5(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoTD2(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoPD2(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoOP2(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoPD3(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoFR2(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoPD4(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoEF2(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoPD5(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoTD3(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoOP3(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoTD4(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoFR3(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoTD5(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoEF3(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoOP4(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoFR4(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoOP5(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoEF4(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoEF5(self, evt):
        self.calcScore()

    def OnRadiobutton_rdoFR5(self, evt):
        self.calcScore()

    def OnScroll_mentalMagSlider(self, evt):
        self.calcScore()

    def OnScroll_physicalMagSlider(self, evt):
        self.calcScore()

    def OnScroll_temporalMagSlider(self, evt):
        self.calcScore()

    def OnScroll_perfMagSlider(self, evt):
        self.calcScore()

    def OnScroll_effortMagSlider(self, evt):
        self.calcScore()

    def OnScroll_frustrMagSlider(self, evt):
        self.calcScore()

    def calcScore(self):
        # calculate factor totals
        self.pdTot = self.rdoPD1.GetValue() + self.rdoPD2.GetValue() +  \
                     self.rdoPD3.GetValue() + self.rdoPD4.GetValue() +  \
                     self.rdoPD5.GetValue()

        self.mdTot = self.rdoMD1.GetValue() + self.rdoMD2.GetValue() +  \
                     self.rdoMD3.GetValue() + self.rdoMD4.GetValue() +  \
                     self.rdoMD5.GetValue()

        self.tdTot = self.rdoTD1.GetValue() + self.rdoTD2.GetValue() +  \
                     self.rdoTD3.GetValue() + self.rdoTD4.GetValue() +  \
                     self.rdoTD5.GetValue()

        self.opTot = self.rdoOP1.GetValue() + self.rdoOP2.GetValue() +  \
                     self.rdoOP3.GetValue() + self.rdoOP4.GetValue() +  \
                     self.rdoOP5.GetValue()

        self.efTot = self.rdoEF1.GetValue() + self.rdoEF2.GetValue() +  \
                     self.rdoEF3.GetValue() + self.rdoEF4.GetValue() +  \
                     self.rdoEF5.GetValue()

        self.frTot = self.rdoFR1.GetValue() + self.rdoFR2.GetValue() +  \
                     self.rdoFR3.GetValue() + self.rdoFR4.GetValue() +  \
                     self.rdoFR5.GetValue()

        # put the magnitude values (ints) into class variables
        self.mentalMag = self.mentalMagSlider.GetValue()
        self.physicalMag = self.physicalMagSlider.GetValue()
        self.temporalMag = self.temporalMagSlider.GetValue()
        self.perfMag = self.perfMagSlider.GetValue()
        self.effortMag = self.effortMagSlider.GetValue()
        self.frustrMag = self.frustrMagSlider.GetValue()

        # FINALLY FOR THE LOVE OF CHRIST
        # calculate the goddam tlx score! hmmph!!!
        self.tlxScore = self.mdTot * self.mentalMag +    \
                        self.pdTot * self.physicalMag +  \
                        self.tdTot * self.temporalMag +  \
                        self.opTot * self.perfMag +      \
                        self.efTot * self.effortMag +    \
                        self.frTot * self.frustrMag
        self.tlxScore /= 15

        # put the score in the label we have for it
        self.scoreTxt.SetLabel(str(self.tlxScore))

        # smoke signals. maybe someone will see them?
        print "calcScore():"
        print "Factor Weights (MD PD TD OP EF FR):",
        print self.mdTot,self.pdTot,self.tdTot,
        print self.opTot,self.efTot,self.frTot
        print "Magnitudes (MD PD TD OP EF FR):",self.mentalMag,self.physicalMag,
        print self.temporalMag,self.perfMag,self.effortMag,self.frustrMag
        print "TLX score:",self.tlxScore

# the real deal
if __name__ == "__main__":
    tlxApp = wx.App(False)
    tlxFrame = tlxMainFrame()
    tlxApp.MainLoop()
