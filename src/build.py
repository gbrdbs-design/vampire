import base64, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "src/vampire-proto.src.html").read_text()
def uri(name):
    return "data:image/jpeg;base64," + base64.b64encode((root / "assets" / f"{name}.jpg").read_bytes()).decode()
out = re.sub(r"__IMG_(\w+?)__", lambda m: uri(m.group(1)), src)
assert "__IMG_" not in out
head = ('<!doctype html>\n<html lang="hu">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>html,body{margin:0;height:100%}img{max-width:100%}[hidden]{display:none!important}</style>\n')
title, rest = out.split("\n", 1)
(root / "index.html").write_text(head + title + "\n</head>\n<body>\n" + rest + "\n</body>\n</html>\n", encoding="utf-8")
print(len(out))
