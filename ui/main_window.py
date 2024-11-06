import wx
import wx.lib.scrolledpanel as scrolled
from ui.tool_bar import ToolBar
from ui.menu import MenuBar
from ui.free_tree import FreeTree
from ui.circuit_board import CircuitBoard


class CircuitSimulator(wx.Frame):
    def __init__(self):
        # 调用父类wx.Frame,正确初始化一个窗口框架 None说明没有父窗口，此窗口即为顶级窗口
        super().__init__(None, title="Logic Circuit Simulator", size=(1200, 800))

        # 初始化器件
        self.menu_bar = MenuBar()  # 创建菜单栏
        self.tool_bar = ToolBar(self)  # 创建工具栏
        self.file_tree = FreeTree(self)
        self.circuit_board = CircuitBoard(self)

        # 布局管理
        self._init_ui()

    def _init_ui(self):
        # 将 菜单栏 和 工具栏 添加到 主窗口中
        self.SetMenuBar(self.menu_bar)
        self.SetToolBar(self.tool_bar)

        # 创建主布局
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.file_tree, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        main_sizer.Add(self.circuit_board, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # 设置主布局
        self.SetSizer(main_sizer)


if __name__ == '__main__':
    app = wx.App(False)
    frame = CircuitSimulator()
    frame.Show()
    app.MainLoop()
