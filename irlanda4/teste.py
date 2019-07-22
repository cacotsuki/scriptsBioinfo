import os
import subprocess
os.name

#print(os.name)

'''
path = "/home/ivan/Downloads"
dirs = os.listdir( path )
for file in dirs:
    print(file)
'''



'''cmd = "java --version"
dk = os.system(cmd)
print(dk)'''



'''def linux(m):
        ler = str(os.system(m))
        return ler
'''

def linux(m):
    ler = (subprocess.check_output(m))

    str(ler, 'utf-8')
    #
    return ler.decode("utf-8")




'''
criar uma janela para argumento
criar uma janela para parametro do argumento
'''


'''for a in os.listdir("."):
     if os.path.isdir(a):
         print("directory: %s" % a)
     elif os.path.isfile(a):
         print("file: %s" % a)'''

'''
a = "venv"

if os.path.exists(a):
     print("O diretório" ,a, "existe.")
else:
     print("O diretório" ,a, "não existe.")
'''

