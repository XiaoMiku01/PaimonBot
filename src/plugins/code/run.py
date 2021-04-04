import requests
import re

codeType = {
    'py': ['python', 'py'],
    'cpp': ['cpp', 'cpp'],
    'java': ['java', 'java'],
    'php': ['php', 'php'],
    'js': ['javascript', 'js'],
    'c': ['c', 'c'],
    'c#': ['csharp', 'cs'],
    'go': ['go', 'go'],
    'asm': ['assembly', 'asm']
}


async def run(str):
    try:
        a = re.findall(r'(py|php|java|cpp|js|c#|c|go|asm)(\n|\r)((?:.|\n)+)', str)[0]
    except:
        return "暂不支持该语言，目前仅支持c/cpp/c#/py/php/go/java/js。"
    lang, code = a[0], a[2]
    headers = {
        "Authorization": "Token 0123456-789a-bcde-f012-3456789abcde",
        "content-type": "application/"
    }
    dataJson = {
        "files": [
            {
                "name": f"main.{codeType[lang][1]}",
                "content": code
            }
        ],
        "stdin": "",
        "command": ""
    }
    res = requests.post(url=f'https://glot.io/run/{codeType[lang][0]}?version=latest', headers=headers, json=dataJson)
    if res.status_code == 200:
        if res.json()['stdout'] != "":
            if len(res.json()['stdout']) < 200:
                return res.json()['stdout']
            else:
                return "返回字符过长！你在拿派蒙寻开心是吧！"
        else:
            return res.json()['stderr']


if __name__ == '__main__':
    print(run('cpp\n#include <iostream>\nusing namespace std;\nint main() \n{\ndouble a=0.1;\ndouble b=0.2;\ncout << '
              'a+b;\nreturn 0;\n}'))
