##使用方法

```python
import sys
from PyQt5.QtWidgets import QApplication
from generator import ToolWindow, ToolConf, Button, ReqProto

app = QApplication(sys.argv)
tw = ToolWindow(ToolConf(
    name="my window",
    desc="my window desc",
    buttons=[
        Button("test", "desc", ReqProto("http://127.0.0.1:8000/hello?user=1", "GET", None)),
    ]
))
sys.exit(app.exec_())
```