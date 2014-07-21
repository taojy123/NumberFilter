#coding=gbk
#Boa:Frame:NumberFilter

import wx

def create(parent):
    return NumberFilter(parent)

[wxID_NUMBERFILTER, wxID_NUMBERFILTERBUTTON1, wxID_NUMBERFILTERPANEL1, 
 wxID_NUMBERFILTERSTATICTEXT1, wxID_NUMBERFILTERTEXTCTRL1, 
 wxID_NUMBERFILTERTEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(6)]

class NumberFilter(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_NUMBERFILTER, name='NumberFilter',
              parent=prnt, pos=wx.Point(398, 219), size=wx.Size(771, 358),
              style=wx.DEFAULT_FRAME_STYLE, title='NumberFilter')
        self.SetClientSize(wx.Size(755, 320))

        self.panel1 = wx.Panel(id=wxID_NUMBERFILTERPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(755, 320),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('')

        self.textCtrl1 = wx.TextCtrl(id=wxID_NUMBERFILTERTEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(32, 64),
              size=wx.Size(120, 176), style=wx.TE_MULTILINE,
              value='12345\n56789\n48901\n74568\n21345\n51234\n94567\n25678\n14567\n34567')
        self.textCtrl1.SetToolTipString('')

        self.textCtrl2 = wx.TextCtrl(id=wxID_NUMBERFILTERTEXTCTRL2,
              name='textCtrl2', parent=self.panel1, pos=wx.Point(168, 64),
              size=wx.Size(552, 176), style=wx.TE_MULTILINE, value='')
        self.textCtrl2.SetToolTipString('')

        self.button1 = wx.Button(id=wxID_NUMBERFILTERBUTTON1,
              label='\xc9\xb8\xd1\xa1\xbc\xc6\xcb\xe3', name='button1',
              parent=self.panel1, pos=wx.Point(224, 264), size=wx.Size(248, 32),
              style=0)
        self.button1.SetToolTipString('')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_NUMBERFILTERBUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_NUMBERFILTERSTATICTEXT1,
              label='\xd6\xc7\xc4\xdc\xca\xfd\xd7\xd6\xc9\xb8\xd1\xa1\xd6\xfa\xca\xd6',
              name='staticText1', parent=self.panel1, pos=wx.Point(208, 16),
              size=wx.Size(288, 35), style=0)
        self.staticText1.SetToolTipString('')
        self.staticText1.SetFont(wx.Font(26, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, '\xc1\xa5\xca\xe9'))

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def is_in(self, num, nums):
        if not num:
            return False
        for n in nums:
            if not n:
                continue
            if num == n:
                return True
            if num == n[::-1]:
                return True
        return False
    
    def is_repeat(self, num, nums):
        nums = ".".join(nums)
        if num[0] in nums and num[1] in nums:
            return True
        return False
    
    def count_nums(self, nums):
        return len(nums) - nums.count("")
    
    def remove_num(self, num, nums):
        i = nums.index(num)
        nums[i] = ""
        if self.count_nums(nums) <= 4 and self.count_nums(nums) >= 2:
            r = []
            for n in nums:
                if n:
                    r.append(n)
            self.textCtrl2.SetValue(self.textCtrl2.GetValue() + ".".join(r) + "    ")

            
    def OnButton1Button(self, event):
        self.textCtrl2.SetValue("")
        data = self.textCtrl1.GetValue()
        data = data.strip()
        lines = data.split("\n")
        for i in range(len(lines[0]) - 1):
            for j in range(i+1, len(lines[0])):
                
                self.textCtrl2.SetValue(self.textCtrl2.GetValue() + str(i+1) + str(j+1) + ":    ")
                
                nums = []
                for n in lines:
                    num = n[i] + n[j]
                    nums.append(num)
                
                self.textCtrl2.SetValue(self.textCtrl2.GetValue() + ".".join(nums) + "    |    ")
                    
                for k in range(1, len(nums)):
                    num = nums[k]
                    if self.is_in(num, nums[:k]):
                        self.remove_num(num, nums)
                
                                
                while self.count_nums(nums) > 2:
                                        
                    flag = False
                    
                    for k in range(len(nums)):
                        num = nums[k]
                        if not num:
                            continue
                        if not self.is_repeat(num, nums[:k] + nums[k+1:]):
                            self.remove_num(num, nums)
                            flag = True
                            
                    if not flag:
                        for num in nums:
                            if num:
                                self.remove_num(num, nums)
                            
                self.textCtrl2.SetValue(self.textCtrl2.GetValue() + "\n")
                
        self.textCtrl2.SetValue(self.textCtrl2.GetValue().strip()[:-1] + "*")
        event.Skip()


