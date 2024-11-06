import wx


class ToolBar(wx.ToolBar):
    def __init__(self, parent):
        super().__init__(parent)

        # 添加逻辑门按钮
        and_gate_tool = self.AddTool(wx.ID_ANY, "AND 门", wx.ArtProvider.GetBitmap(wx.ART_PLUS, wx.ART_TOOLBAR))
        or_gate_tool = self.AddTool(wx.ID_ANY, "OR 门", wx.ArtProvider.GetBitmap(wx.ART_MINUS, wx.ART_TOOLBAR))
        not_gate_tool = self.AddTool(wx.ID_ANY, "NOT 门", wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_TOOLBAR))

        # 绑定按钮事件
        self.Bind(wx.EVT_TOOL, lambda event: self.add_gate(event, "AND"), and_gate_tool)
        self.Bind(wx.EVT_TOOL, lambda event: self.add_gate(event, "OR"), or_gate_tool)
        self.Bind(wx.EVT_TOOL, lambda event: self.add_gate(event, "NOT"), not_gate_tool)

        # 设置工具栏
        self.Realize()
