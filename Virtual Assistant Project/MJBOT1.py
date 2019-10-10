# Combining the GUI piece and the wikipedia and Wolfram Pieces together
# Run the Script MJBOT for better experience

import wx
import wikipedia
import wolframalpha
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="MJBOT")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am MJBOT the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        inp = self.txt.GetValue()
        inp = inp.lower()
        try:
            app_id = "L53TAJ-427HL6WKXQ"
            client = wolframalpha.Client(app_id)
            res = client.query(inp)
            answer = next(res.results).text # text specifies we only retrieve text results.
            print(answer)
        except:
            inp = inp.split(' ')
            inp = " ".join(inp[2:])
            wikipedia.set_lang("en") # Set the language for wikipedia - fr = French, es = Spanish, de = German, zh = Chinese
            print(wikipedia.summary(inp,sentences = 2)) # Sentences limits the number of sentences returned by wikipedia


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()