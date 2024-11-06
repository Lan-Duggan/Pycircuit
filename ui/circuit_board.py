import wx
import wx.lib.scrolledpanel as scrolled


class CircuitBoard(scrolled.ScrolledPanel):
    def __init__(self, parent):
        super().__init__(parent, size=(1500, 900),style=wx.SUNKEN_BORDER)

        self.SetBackgroundColour("WHITE")
        self.SetupScrolling()


