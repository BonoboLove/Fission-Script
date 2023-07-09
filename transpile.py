import sys, re, os, shutil, PyInstaller.__main__

code_path = './code.fss'
script_path = './pycode.py'
error_path = './error_log.txt'
output_path = './output'

def transpile():
    with open(code_path, 'r') as f:
        global x
        x = f.read()
    x = x.split('\n')
    for i in range(len(x)):
        x[i] = x[i]
        if x[i].strip().startswith('send'):
            x[i] = x[i].replace('send', 'return')

        pattern = r'\([^)]*\)\.len'
        matches = re.findall(pattern, x[i])
        for match in matches:
            if all(char not in x[i][x[i].index(match)+1] or '_' in char for char in ('`', "'", '"')):
                x[i] = x[i].replace(match, ("len"+match[:-4]), 1).replace('len(_','len(', 1)

        pattern = r'<>'
        matches = re.findall(pattern, x[i])
        for match in matches:
            if x[i][x[i].index(match) + len(match)] not in ('"', "'", '`'):
                x[i] = x[i].replace(match, '.index')
        
        pattern = r'.add'
        matches = re.findall(pattern, x[i])
        for match in matches:
            if x[i][x[i].index(match) + len(match)] not in ('"', "'", '`'):
                x[i] = x[i].replace(match, '.append')
          
        if "=" in x[i] and "=>" in x[i]:
            index_equal = x[i].index("=")
            index_arrow = x[i].index("=>")
            substring = x[i][index_equal + 1: index_arrow].strip()
            x[i] = x[i][:index_equal] + " = " + "lambda " + substring + ":" + x[i][index_arrow + 2:]

    return '\n'.join(x)

def main():
    f = open(script_path, "w")
    f.write(transpile())
    f.close()

    options = [
        '--onefile',
        '--console',
        '--name=app',
        ('--distpath='+output_path)
    ]
    try:
        PyInstaller.__main__.run([script_path] + options)
    except Exception as e:
        with open(error_path, "w") as file:
            file.write(str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
    os.remove("./app.spec")
    shutil.rmtree("./build")    