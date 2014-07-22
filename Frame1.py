#coding=gbk
#Boa:Frame:NumberFilter

import wx

from numbers import Numbers
import time
import os

def create(parent):
    return NumberFilter(parent)

[wxID_NUMBERFILTER, wxID_NUMBERFILTERBUTTON1, wxID_NUMBERFILTERBUTTON2, 
 wxID_NUMBERFILTERBUTTON3, wxID_NUMBERFILTERPANEL1, 
 wxID_NUMBERFILTERSTATICTEXT1, wxID_NUMBERFILTERTEXTCTRL1, 
 wxID_NUMBERFILTERTEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(8)]

class NumberFilter(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_NUMBERFILTER, name='NumberFilter',
              parent=prnt, pos=wx.Point(323, 215), size=wx.Size(695, 401),
              style=wx.DEFAULT_FRAME_STYLE,
              title='\xd5\xbd\xc9\xf1\xd6\xc7\xc4\xdc\xd1\xa1\xba\xc5\xd6\xfa\xca\xd6')
        self.SetClientSize(wx.Size(679, 363))

        self.panel1 = wx.Panel(id=wxID_NUMBERFILTERPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(679, 363),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('')

        self.textCtrl1 = wx.TextCtrl(id=wxID_NUMBERFILTERTEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(24, 64),
              size=wx.Size(176, 216), style=wx.TE_MULTILINE,
              value=u'04   06   10   11   05\n01   04   08   03   05\n03   11   01   08   10\n09   04   08   10   02\n01   04   11   08   05\n01   06   08   10   02\n03   05   10   07   09\n08   05   04   06   09\n08   11   09   02   07\n06   04   11   09   08')
        self.textCtrl1.SetToolTipString('')

        self.textCtrl2 = wx.TextCtrl(id=wxID_NUMBERFILTERTEXTCTRL2,
              name='textCtrl2', parent=self.panel1, pos=wx.Point(216, 64),
              size=wx.Size(424, 216), style=wx.TE_MULTILINE, value='')
        self.textCtrl2.SetToolTipString('')

        self.button1 = wx.Button(id=wxID_NUMBERFILTERBUTTON1,
              label='\xc9\xb8\xd1\xa1\xbc\xc6\xcb\xe3', name='button1',
              parent=self.panel1, pos=wx.Point(264, 304), size=wx.Size(152, 32),
              style=0)
        self.button1.SetToolTipString('')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_NUMBERFILTERBUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_NUMBERFILTERSTATICTEXT1,
              label='\xd5\xbd\xc9\xf1\xd6\xc7\xc4\xdc\xd1\xa1\xba\xc5\xd6\xfa\xca\xd6',
              name='staticText1', parent=self.panel1, pos=wx.Point(184, 16),
              size=wx.Size(288, 35), style=0)
        self.staticText1.SetToolTipString('')
        self.staticText1.SetFont(wx.Font(26, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, '\xc1\xa5\xca\xe9'))

        self.button2 = wx.Button(id=wxID_NUMBERFILTERBUTTON2,
              label='\xc7\xe5\xbf\xd5', name='button2', parent=self.panel1,
              pos=wx.Point(40, 304), size=wx.Size(152, 32), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_NUMBERFILTERBUTTON2)

        self.button3 = wx.Button(id=wxID_NUMBERFILTERBUTTON3,
              label='\xb1\xa3\xb4\xe6', name='button3', parent=self.panel1,
              pos=wx.Point(464, 304), size=wx.Size(152, 32), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_NUMBERFILTERBUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def OnButton1Button(self, event):
        self.textCtrl2.SetValue("")
        input_str = self.textCtrl1.GetValue().strip()
        numbers = Numbers(input_str)
        result_str = numbers.get_result()
        self.textCtrl2.SetValue(result_str)
        event.Skip()

    def OnButton2Button(self, event):
        self.textCtrl1.SetValue("")
        self.textCtrl2.SetValue("")
        event.Skip()

    def OnButton3Button(self, event):
        if not os.path.exists('历史数据'):
            os.makedirs('历史数据')
        s = self.textCtrl1.GetValue() + "\n\n" + self.textCtrl2.GetValue()
        fn = "历史数据/" + time.strftime("%Y%m%d") + ".txt"
        open(fn, "w").write(s)
        event.Skip()


