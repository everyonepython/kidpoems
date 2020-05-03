## PyQt5 Qt-Creator 操作流程

1. 打開 Qt-Creator
2. File -> New File or Project
3. File and Classes - Qt - Qt Designer Form
4. Main Window 或 Widget
   它們的區別是 Main Window 有菜單及狀態欄。
5. Location -> Pycharm 項目的路徑。

進入設計界面後，只需要用到 Design。

#### 左邊欄
所有可用的 widget，只需要拖方進設計窗口即可。

#### 右邊欄
- 上面是 widget 的結構，可以拖動來改變從屬關係，像文件夾一樣。
    - 記得修改每個 widget 的名字，否則在調用時很容易造成混亂。

-  下面是所選 widget 的屬性，可以點擊進行更改。
    - 注意設置 maximumSize，否則在設計中很容易造成 widget 變形。
    - 可以參考屬性名字，在代碼中測試各種屬性。



## 所有 App 界面上看到的内容都是一个组件 widget。

- 包括buttons, labels, windows, dialogs, progress bars 等等。
- 类似 HTML 元素一样，经常一个嵌套另一个。
- 一个按钮 Button 上包含一个标签 Label


## 页面设计与业务逻辑分离
编写逻辑文件時 Class-類 的设置

如有报错为 `AttributeError: '***' object has no attribute 'setCentralWidget'`，很可能是没有继承 QMainWindow。

类 必须继承 `QMainWindow` 及 生成 `ui_**.py` 文件的 `Ui_MainWindow/Ui_Form/` 等 两个类。

继承之后初始化调用 `super` 函数超类的 `__init__()` 方法初始化，需要两个参数：
第一个参数，自定义类，说明想要调用超类的某个方法，这里的超类，即 `QMainWindow` 和 `UiMainWindow/Ui_Form`。
第二个参数，`self`，引用的是刚刚实例化出来的自己，于是超类就能得到这个对象 `self`，并向其添加 parent 特性，这里 `parent=None`，`QMainWindow` 的__init__()方法中默认值就是None，其实可以用不添加。

超类初始化后，调用 `QMainWindow`/`Ui_Form` 的 `setupUi()` 方法，把 `self` 对象传入。
否则不能引用 `ui_**.py` 中的所有组件。

 
```Python
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_stackwidget import Ui_MainWindow


class MyStackWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyStackWidget, self).__init__(parent)
        self.setupUi(self)
```

Python3 中，可以简写成：
```Python
class MyStackWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init()
        self.setupUi(self)
```


# fbs - Python 打包工具
下載 fbs 生成項目的源代碼後運行 `main.py` 抱錯如下。

![img](https://build-system.fman.io/static/public/img/widgets.png)

[此图的代码](a04_widgets_example.py)

报错：
```
Traceback (most recent call last):
  File "widgets_example.py", line 44, in <module>
    from fbs_runtime.application_context.PyQt5 import ApplicationContext
ModuleNotFoundError: No module named 'fbs_runtime'
```
原因是未安裝 fbs。
fbs为Python程序打包、创建安装程序和签署应用程序提供了强大的环境。它支持管理应用程序的更新，它基于PyInstaller，因此它支持Linux，macOS和Windows。


# fsb 上下文 Application.Context()

執行 `fsb startproject` 會自動生成一個項目，項目入口時 main.py 裡面有如下代碼
```python
from fbs_runtime.application_context.PyQt5 import ApplicationContext
...
# main.py
if __name__ == '__main__':
    appctxt = ApplicationContext()
    ...
    appctxt.app.exec_()
```
封裝了原來 PyQt5 QApplication，可以調用 ApplicationContext.app。
其中還有一個 get_resources() 的方法可以訪問項目中的資源文件。
若想在邏輯文件中方便地訪問資源文件，之前想一個種方法，就是把上下文對象傳入邏輯文件。
```python
# main.py
...
context = ApplicationContext()
window = QMainWindow(context)
```
但這樣的話，代碼就會有點麻煩。
網上介紹有中更乾淨的方法，就是新建一個 base.py 文件，只有兩行代碼。
```python
# base.py
from fbs_runtime.application_context.PyQt5 import ApplicationContext

context = ApplicationContext()
```
結構如下：
```
項目 python 文件夾中的結構
python
├── base.py
├── gui.py
├── logic.py
└── main.py
```
然後在每一個文件中調用 base.context，就可以讓每一個文件都可以優雅地訪問上下文。
```python
from base import context

context.get_resource('audio')
...
context.app.exec_()
...
context.build_settings['version']
...
```
改寫後 main.py 文件就變成這樣了。
```python
# main.py
import sys

from base import context
from call_stackwidget import MyStackWidget

if __name__ == '__main__':
    my_window = MyStackWidget()
    my_window.show()
    exit_code = context.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
```


## fbs - 未能正確播放聲音文件（資源文件）

用 fbs 開發時，資源文件必須放在 `./src/main/resources/base/` 文件夾中，初始化項目時不會生成此文件夾，需要自己添加。
否則 `ApplicaitionContext.content.get_resource(relPath)` 方法會返回 `./src/mai/icons` 文件夾。
不能把資源放在 icons/ 文件夾中，因為 fbs 打包時不會把放在 icons/ 中的資源文件輸出到 app 裡面，因此必須手動添加 base 路徑。
添加後，調用 `get_resource(<相對路徑>)` 將會正確找到 base/ 的絕對路徑。 

運行 fbs freeze 後，Terminal 提示：
```
Done. You can now run `target/KidPoems.app/Contents/MacOS/KidPoems`.
```
問題仍然存在。
按照提示運行 `KidPoems.app/Contents/MacOS/KidPoems` 可以正確播放聲音文件。
聲音文件到處到 `KidPoems.app/Contents/Resources/` 中，相對與開發時的 `base/` 文件夾。

然而，若直接打開 KidPoems.app 可以運行，但不能播放聲音。必須打開 app 查看內容，然後按路徑找到 KidPoems 的二進制執行文件來運行。
兩者的區別在於，直接運行 app 則沒有彈出 terminal，比較美觀。後者則彈出 terminal 像開發者調試的模式。


