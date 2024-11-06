import wx

class MenuBar(wx.MenuBar):
    def __init__(self):
        super().__init__()

        # 创建并添加文件菜单
        file_menu = self._create_file_menu()
        self.Append(file_menu, "&文件")

    def _create_file_menu(self):
        """创建文件菜单并绑定事件，便于维护和扩展。"""
        file_menu = wx.Menu()

        # 菜单项配置：键为菜单项id，值为(名称, 描述, 绑定方法)
        menu_items = {
            wx.ID_NEW: ("&新建", "创建一个新的逻辑电路文件", self.on_new_file),
            wx.ID_OPEN: ("&打开", "打开一个已有的电路文件", self.on_open_file),
            wx.ID_SAVE: ("&保存", "保存当前电路文件", self.on_save_file),
        }

        # 添加菜单项及事件绑定
        for item_id, (label, help_text, handler) in menu_items.items():
            menu_item = file_menu.Append(item_id, label, help_text)
            self.Bind(wx.EVT_MENU, handler, menu_item)

        return file_menu

    def _get_file_path(self, style, wildcard, message):
        """通用的文件对话框处理方法，简化打开和保存文件逻辑"""
        with wx.FileDialog(None, message, wildcard=wildcard,
                           style=style) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return None  # 用户取消了操作
            return file_dialog.GetPath()

    def on_new_file(self, event):
        """处理新建文件的逻辑"""
        path = self._get_file_path(wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, "电路文件 (*.cir)|*.cir", "新建文件")
        if not path:
            return

        try:
            with open(path, 'w') as file:
                file.write("")  # 写入空内容，创建一个空文件
                wx.LogMessage(f"新文件已创建: {path}")
                wx.MessageBox("新文件创建成功！", "提示", wx.OK | wx.ICON_INFORMATION)
        except IOError:
            wx.LogError(f"无法创建文件 '{path}'")

    def on_open_file(self, event):
        """处理打开文件的逻辑"""
        path = self._get_file_path(wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, "电路文件 (*.cir)|*.cir|所有文件 (*.*)|*.*", "打开文件")
        if not path:
            return

        try:
            with open(path, 'r') as file:
                content = file.read()  # 读取文件内容
                wx.LogMessage(f"打开文件的操作: {path}")
                # 显示内容或处理内容（根据项目需要）
                wx.MessageBox(f"文件内容:\n{content}", "文件内容", wx.OK | wx.ICON_INFORMATION)
        except IOError:
            wx.LogError(f"无法打开文件 '{path}'")

    def on_save_file(self, event):
        """处理保存文件的逻辑"""
        path = self._get_file_path(wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, "电路文件 (*.cir)|*.cir|所有文件 (*.*)|*.*", "保存文件")
        if not path:
            return

        try:
            with open(path, 'w') as file:
                content = "电路文件的保存内容"  # 假设有要保存的内容
                file.write(content)
                wx.LogMessage(f"保存文件的操作: {path}")
                wx.MessageBox("文件已成功保存", "提示", wx.OK | wx.ICON_INFORMATION)
        except IOError:
            wx.LogError(f"无法保存文件 '{path}'")
