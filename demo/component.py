import re
from .apps import Appname
from django.shortcuts import HttpResponse


def renderPlus(request, response):
    """

            读取render的返回内容解析解析内容

            请在apps.py中添加 Appname 字段
            例如:
                Appname = 'demo'

            匹配到 import '/S+'
            读取 /S+ 这是一个位置信息
            读取文件内容然后返回 HttpResponse

    """

    _content = response.getvalue().decode('utf-8')

    _re = r"[^/|^\*](import '\S*')[\n|\s+\n]"
    _string = r"import '(\S*)'"

    _group = re.compile(_re, re.M).findall(_content)

    for item in _group:
        _path = re.compile(_string, re.M).findall(item)[0]

        if _path != None:
            """
                读取文件
            """
            rel_path = './%s/templates/component/%s' % (Appname,
                                                        _path)

            with open(rel_path, 'r', encoding='utf-8') as fp:
                _content = _content.replace(item, GrammarTransform(_path[:-4],
                                                                   fp.readlines()))

    return HttpResponse(_content)


def GrammarTransform(componentname, Vue):
    """

        .Vue 文件语法转换

        .Vue -> Vue.Component()

    """
    if isinstance(Vue, (list, tuple)):

        _grammar = "Vue.component('%s',{\n%s,\ntemplate:'%s'})"

        _header = ''
        _html = []
        _js = []
        _original_js = (
            'script',
        )
        _original_html = (
            'template',
            'style'
        )

        # 读取行匹配模板语句类型
        for line in Vue:
            if not line.replace(' ','').replace('\n','').replace('\r','') is '':

                _re = re.compile(r'<(\S+)>').findall(line)


                if len(_re):
                    _item = _re[0]
                    # 如果是头的话保存起来
                    if _item in (_original_js + _original_html) or _item[1:] in (_original_js + _original_html):
                        _header = _item
                        continue

                # 是模板的放到template ，不是的放到js
                if _header in _original_html:
                    _html.append(line.replace('\n',''))   # 去换行

                elif _header in _original_js:
                    _js.append(line.replace("'", '"'))

        # 转换语法保存
        return _grammar % (
            componentname,
            ''.join(_js[1:-1]),
            ''.join(_html)
        )

    else:
        raise TypeError('''
                语法转换失败,类型不匹配，需要 list 或者 tuple
                ''')
