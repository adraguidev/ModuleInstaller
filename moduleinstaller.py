import os

def ModuleInstaller(*args):
    for x in args:
        try:
            print(f'>>>>>Intentando instalar {x} con Conda:')
            result_conda = os.system(f"conda install -c anaconda {x} -y")
            if result_conda == 256:
                print(f"No se encontro el modulo {x} en Conda")
                raise ValueError('No se encontro el modulo en Conda.')
        except:
            try:
                print(f'>>>>>Intentando instalar {x} con pip:')
                result_pip = os.system(f"pip install {x}")
                if result_pip == 256:
                    print("No se encontro el modulo en Pip.")
                    raise ValueError("No se encontro el modulo en Pip.")
            except:
                try:
                    print(f'>>>>>Intentando instalar {x} con pip3:')
                    result_pip3 = os.system(f"pip3 install {x}")
                    if result_pip3 == 256:
                        print(">>>>>No se encontro el modulo en Pip3.")
                        raise ValueError('No se encontro el modulo en Pip3.')
                except:
                    print(f">>>>>No se encontro la libreria {x}")
                    
    print("Proceso Terminado")