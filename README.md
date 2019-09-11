## django_vue
#### 在django中使用vue的组件

**使用方法:**

1.需要在 apps.py 中添加

Appname = ’你的app名称‘

2.需要引用组件的HTML中的 script 中放置

import 组件名称

3.在 View 视图中

用renderPlus包装render

#---------------------------

具体使用示例在 demo 中

核心文件是./demo/component.py
![chrome](https://github.com/WOSHIliuhailong/djangovue/blob/dev/chrome_2019-09-11_16-07-40.png)
![route](https://github.com/WOSHIliuhailong/djangovue/blob/dev/Code_2019-09-11_16-07-30.png)
