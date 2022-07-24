# prueba_tecnica
Hola, Estos son los pasos a seguir para poder ver mi proyecto:
(El proceso está basado en el sistema operativo Windows 10 y utilizando la terminaL CMDER)

Número Uno: Instalación del Proyecto

1. Abra la terminal de comandos.
2. Ingrese el comando Documents/ ( Terminal Bash: cd Documents/).
3. Con el comando mkdir orusxpert crea la carpeta donde vamos a copiar el repositorio.
4. Ingrese a la carpeta con el comado /orusxpert (Terminal Bash: cd orusxpert/)
5. Inicialice git con el comando git init.
6. Clone el repositorio con el comando git clone git@github.com:MatheoArias/Prueba_Tecnica.git
7. Cree un entorno virual. En el caso de Windows:
      -python3 -m venv venv
      -alias avenv=.\venv\Scripts\
      -Para Activar el entorno avenv o para Desactivar el entorno decativate
9. Instale los requerimientos (en el repositorio se encuentra un archivo requieriments.txt), usando el comando  pip install -r .\requirements.txt 
Nota: En los requerimientos ya se encuentra la version de django, por lo tanto, cuando realice el proceso lo tendrá instalado en el entorno virtual.
10. Inicialice el servidor con el comando py manage.py runserver

Número Uno: Visualización de la aplicación

11. Para entrar en la vista login en el buscador de su navegador favorito: http://127.0.0.1:8000/login/
    - El Usuario es : MatheoArias
    - La contraseñ es : mateocorrea1
12. El flujo de Aplicación lo podemos interpretar de la siguiente manera:
    -Menu ----> -Ingresar Usuario--->Formulario Registrar Usuario (Signup) :Puede registrar un nuevo Usuario (nombrede usuario-correolectronico-contraseña)
                - Ingresar Lugar---->Formulario Registrar Ciudad o Departamento (register: addspace): Puede Registrar  un nuevo Departamento o Ciudad: Puede ingresar una ciudad o Departamento (El nombre de la Ciudad o Departamento y el indictaivo del Departamento)
                - Ingresar Habitantes---->Formulario Registrar Habitantes (register: add) : Puede Registrar un Habitante (cédula-departamento-ciudad-primernombre-segundonombre-primerapellido-segundoapellido-direccion-telefonofijo-celular)
13. En caso de no recordar la contraseña, en el template login, pues pasar el curso por el texto ("¿Ha olvidado su contraseña? Puede restaurarla ----->aquí") da click y el lo redireccionará a el template donde podrá enviarse un correo para restaurar la contraseña
              
