import wx


class FreeTree(wx.TreeCtrl):
    def __init__(self, parent):
        super().__init__(parent, size =(150,600))

        # 添加根节点
        self.root = self.AddRoot("根节点")

        # 向根节点添加子节点
        self.node1 = self.AppendItem(self.root, "子节点 1")
        self.node2 = self.AppendItem(self.root, "子节点 2")

        # 向子节点添加子节点
        self.AppendItem(self.node1, "子节点 1-1")
        self.AppendItem(self.node2, "子节点 2-1")



