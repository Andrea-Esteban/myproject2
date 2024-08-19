import sys

def test_python_version():
    version = f'{sys.version_info.major}.{sys.version_info.minor}'
    print(f'Versión de Python: {version}')
    
    flag = True
    if not sys.version_info.major == 3 and sys.version_info.minor >= 9:
        flag = False
    
    assert flag, 'Se está usando una versión inferior a Python 3.9.'
