import sys
class paciente():
    def __init__(self, nombre, apellido, fechaNacimiento,dia,edad, mes,año,hoy, paisResi, genero):
        nombre = nombre
        apellido = apellido
        fechaNacimiento=fechaNacimiento
        paisResi = paisResi
        genero = genero
        dia = dia
        mes=mes
        año=0
        hoy=2020

    def print_nombre(self):
        print(self.nombre)
    def print_apellido(self):
        print(self.apellido)
    def print_fechaNacimiento(self):
        print(self.fechaNacimiento)
    def print_paisResi(self):
        print(self.paisResi)
    def print_genero(self):
        print(self.genero)
    def print_dia(self):
        print(self.dia)
    def print_mes(self):
        print(self.mes)
    def print_año(self):
        print(self.año)
    def print_hoy(self):
        print(self.hoy)
    def print_edad(self):
        print(self.edad)

    def mostrarInfo():
        print("-- ¿QUE ES? --\n")
        print(" Los coronavirus son una familia de virus que pueden causar")
        print(" enfermedades como el resfriado común, el síndrome respiratorio")
        print(" agudo grave (SARS, por sus siglas en inglés), y el síndrome respiratorio")
        print(" de Oriente Medio (MERS, por sus siglas en inglés). En 2019 se identificó un")
        print(" un nuevo coronavirus como la causa de un brote de enfermedades que")
        print("se originó en China.\n")
        print("Este virus ahora se conoce como el síndrome respiratorio agudo grave")
        print(" coronavirus 2 (SARS-CoV-2). La enfermedad que causa se llama enfermedad")
        print(" del coronavirus 2019 (COVID-19).\n")
                
        print("-- CASOS --\n")
        print(" Los casos del COVID-19 se han reportado en un número creciente de países,")
        print(" incluyendo los Estados Unidos. Los grupos de salud pública como la")
        print(" Organización Mundial de la Salud (OMS) y los Centros para el Control y")
        print(" la Prevención de Enfermedades de Estados Unidos (CDC), están vigilando")
        print(" la situación y publicando actualizaciones en sus sitios web.(OMS)declaró")
        print(" una pandemia mundial en marzo de 2020. Estos grupos también han publicado")
        print(" recomendaciones para prevenir y tratar esta enfermedad.\n")

        print("-- TRANSMISION  --\n")
        print(" Las rutas de transmisión de persona a persona del SARS-CoV-2,")
        print(" incluyeron transmisión directa, como tos, estornudos,")
        print(" transmisión por inhalación de gotas y transmisión por contacto,")
        print(" como el contacto con las membranas mucosas orales, nasales y oculares.")
        print(" También se puede transmitir a través de la saliva, y la rutas")
        print(" fecal-oral también pueden ser una posible ruta de transmisión de")
        print(" persona a persona.​ Un estudio de 2.143 niños sugiere pueden ser")
        print(" un factor crítico en la rápida propagación de la enfermedad.\n")

        print("-- SINTOMAS  --\n")
        print("Los signos y síntomas de laCOVID-19, pueden aparecer entre dos y 14 días")
        print("después de estar expuesto, y pueden incluir: \n")
        print("- Tos")
        print("- Fiebre")
        print("- Falta de aire o dificultad para respirar\n")
        print("Otros sintomas pueden ser los siguientes:  \n")
        print("- Dolores")
        print("- Goteo de la nariz")
        print("- Dolor de garganta\n")
        print("La gravedad de los síntomas de laCOVID-19, puede ir de leve a grave. Algunas personas ")
        print(" no presentan síntomas. Las personas mayores o que tienen ciertas afecciones crónicas,")
        print(" como enfermedades cardíacas o pulmonares, o diabetes, pueden correr un riesgo más alto")
        print(" de enfermarse de gravedad. Esto es similar a lo que se ve con otras enfermedades")
        print(" respiratorias, como la influenza.\n")

    def mostrarMundial():
        print("-- PAISES CON MAS CASOS DE CORONAVIRUS DETECTADOS --\n")
        print("------------------------------------ EURO-ASIA ----------------------------------")
        print("--  PAIS  ----------------------- CONTAGIADOS ------------------------ MUERTES   --")
        print("-- CHINA    >>>>>>>>>>>>>>>>>>>>   +81.000   >>>>>>>>>>>>>>>>>>>>>>>>  + 3.270   --")
        print("-- ITALIA   >>>>>>>>>>>>>>>>>>>>   +59.130   >>>>>>>>>>>>>>>>>>>>>>>>  + 5.470   --")
        print("-- ESPAÑA   >>>>>>>>>>>>>>>>>>>>   +33.089   >>>>>>>>>>>>>>>>>>>>>>>>  + 2.200   --")
        print("-- ALEMANIA >>>>>>>>>>>>>>>>>>>>   +27.546   >>>>>>>>>>>>>>>>>>>>>>>>  +   120   --")
        print("-- IRAN     >>>>>>>>>>>>>>>>>>>>   +23.049   >>>>>>>>>>>>>>>>>>>>>>>>  + 1.812   --")
        print("-- FRANCIA  >>>>>>>>>>>>>>>>>>>>   +16.937   >>>>>>>>>>>>>>>>>>>>>>>>  +   680   --")
        print("-- COREA DEL SUR >>>>>>>>>>>>>>>   + 8.961   >>>>>>>>>>>>>>>>>>>>>>>   +   111   --")
        print("-- SUIZA    >>>>>>>>>>>>>>>>>>>>   + 8.234   >>>>>>>>>>>>>>>>>>>>>>>>  +   107   --")
        print("-- UK       >>>>>>>>>>>>>>>>>>>>   + 5.683   >>>>>>>>>>>>>>>>>>>>>>>>  +   281   --")
        print("-- HOLANDA  >>>>>>>>>>>>>>>>>>>>   + 4.204   >>>>>>>>>>>>>>>>>>>>>>>>  +   179   --")
        print("-- AUSTRIA  >>>>>>>>>>>>>>>>>>>>   + 3.806   >>>>>>>>>>>>>>>>>>>>>>>>  +    16   --")
        print("-- BELGICA  >>>>>>>>>>>>>>>>>>>>   + 3.743   >>>>>>>>>>>>>>>>>>>>>>>>  +    88   --")
        print("-- NORUEGA  >>>>>>>>>>>>>>>>>>>>   + 2.415   >>>>>>>>>>>>>>>>>>>>>>>>  +     8   --")
        print("-- PORTUGAL >>>>>>>>>>>>>>>>>>>>   + 2.060   >>>>>>>>>>>>>>>>>>>>>>>>  +    23   --")
        print("-- MALASIA  >>>>>>>>>>>>>>>>>>>>   + 1.518   >>>>>>>>>>>>>>>>>>>>>>>>  +    14   --")
        print("-- DINAMARCA>>>>>>>>>>>>>>>>>>>>   + 1.450   >>>>>>>>>>>>>>>>>>>>>>>>  +    13   --")
        print("-- TURQUIA  >>>>>>>>>>>>>>>>>>>>   + 1.236   >>>>>>>>>>>>>>>>>>>>>>>>  +    30   --")
        print("-- REP.CHECA>>>>>>>>>>>>>>>>>>>>   + 1.165   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- JAPON    >>>>>>>>>>>>>>>>>>>>   + 1.101   >>>>>>>>>>>>>>>>>>>>>>>>  +    41   --")
        print("-- IRLANDA  >>>>>>>>>>>>>>>>>>>>   +   906   >>>>>>>>>>>>>>>>>>>>>>>>  +     4   --")
        print("-- ISRAEL   >>>>>>>>>>>>>>>>>>>>   +   883   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- PAKISTAN >>>>>>>>>>>>>>>>>>>>   +   804   >>>>>>>>>>>>>>>>>>>>>>>>  +     6   --")
        print("-- LUXEMBURGO>>>>>>>>>>>>>>>>>>>   +   798   >>>>>>>>>>>>>>>>>>>>>>>>  +     8   --")
        print("-- TAILANDIA>>>>>>>>>>>>>>>>>>>>   +   721   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- FINLANDIA>>>>>>>>>>>>>>>>>>>>   +   686   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- POLONIA  >>>>>>>>>>>>>>>>>>>>   +   684   >>>>>>>>>>>>>>>>>>>>>>>>  +     8   --")
        print("-- GRECIA   >>>>>>>>>>>>>>>>>>>>   +   624   >>>>>>>>>>>>>>>>>>>>>>>>  +    17   --")
        print("-- INDONESIA>>>>>>>>>>>>>>>>>>>>   +   579   >>>>>>>>>>>>>>>>>>>>>>>>  +    49   --")
        print("-- RUMANIA  >>>>>>>>>>>>>>>>>>>>   +   576   >>>>>>>>>>>>>>>>>>>>>>>>  +     5   --")
        print("-- ISLANDIA >>>>>>>>>>>>>>>>>>>>   +   568   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- ARABIA SAUDITA>>>>>>>>>>>>>>>   +   511   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- SINGAPUR >>>>>>>>>>>>>>>>>>>>   +   509   >>>>>>>>>>>>>>>>>>>>>>>>  +     2   --")
        print("-- QATAR    >>>>>>>>>>>>>>>>>>>>   +   494   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- FILIPINAS>>>>>>>>>>>>>>>>>>>>   +   462   >>>>>>>>>>>>>>>>>>>>>>>>  +    33   --")
        print("-- RUSIA    >>>>>>>>>>>>>>>>>>>>   +   438   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- INDIA    >>>>>>>>>>>>>>>>>>>>   +   425   >>>>>>>>>>>>>>>>>>>>>>>>  +     8   --")
        print("-- ESLOVENIA>>>>>>>>>>>>>>>>>>>>   +   414   >>>>>>>>>>>>>>>>>>>>>>>>  +     3   --")
        print("-- ESTONIA  >>>>>>>>>>>>>>>>>>>>   +   352   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- BAHREIN  >>>>>>>>>>>>>>>>>>>>   +   339   >>>>>>>>>>>>>>>>>>>>>>>>  +     2   --")
        print("-- CROACIA  >>>>>>>>>>>>>>>>>>>>   +   306   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- IRAK     >>>>>>>>>>>>>>>>>>>>   +   266   >>>>>>>>>>>>>>>>>>>>>>>>  +    23   --")
        print("-- LIBANO   >>>>>>>>>>>>>>>>>>>>   +   256   >>>>>>>>>>>>>>>>>>>>>>>>  +     4   --")
        print("-- SERBIA   >>>>>>>>>>>>>>>>>>>>   +   222   >>>>>>>>>>>>>>>>>>>>>>>>  +     2   --")
        print("-- TAIWAN   >>>>>>>>>>>>>>>>>>>>   +   195   >>>>>>>>>>>>>>>>>>>>>>>>  +     2   --")
        print("-- ARMENIA  >>>>>>>>>>>>>>>>>>>>   +   194   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- BULGARIA >>>>>>>>>>>>>>>>>>>>   +   190   >>>>>>>>>>>>>>>>>>>>>>>>  +     3   --")
        print("-- KUWAIT   >>>>>>>>>>>>>>>>>>>>   +   189   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- ESLOVAQUIA>>>>>>>>>>>>>>>>>>>   +   186   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- LETONIA  >>>>>>>>>>>>>>>>>>>>   +   180   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- SAN MARINO>>>>>>>>>>>>>>>>>>>   +   175   >>>>>>>>>>>>>>>>>>>>>>>>  +    20   --")
        print("-- HUNGRIA  >>>>>>>>>>>>>>>>>>>>   +   167   >>>>>>>>>>>>>>>>>>>>>>>>  +     7   --")
        print("-- LITUANIA >>>>>>>>>>>>>>>>>>>>   +   154   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- EMIRATOS ARABES UNIDOS >>>>>>   +   153   >>>>>>>>>>>>>>>>>>>>>>>>  +     2   --")
        print("-- MACEDONIA DEL NORTE>>>>>>>>>>   +   136   >>>>>>>>>>>>>>>>>>>>>>>>  +     2   --")
        print("-- BOSNIA Y HERZEGOVINA >>>>>>>>   +   128   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- VIETNAM  >>>>>>>>>>>>>>>>>>>>   +   121   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- ISLAS FEROE>>>>>>>>>>>>>>>>>>   +   118   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- ANDORRA  >>>>>>>>>>>>>>>>>>>>   +   113   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- JORDANIA >>>>>>>>>>>>>>>>>>>>   +   112   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- MALTA    >>>>>>>>>>>>>>>>>>>>   +   107   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- CHIPRE   >>>>>>>>>>>>>>>>>>>>   +    95   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- MOLDAVIA >>>>>>>>>>>>>>>>>>>>   +    94   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- BRUNEI   >>>>>>>>>>>>>>>>>>>>   +    91   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- ALBANIA  >>>>>>>>>>>>>>>>>>>>   +    89   >>>>>>>>>>>>>>>>>>>>>>>>  +     4   --")
        print("-- SRI LANKA>>>>>>>>>>>>>>>>>>>>   +    87   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- CAMBOYA  >>>>>>>>>>>>>>>>>>>>   +    86   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- BIELORRUSIA>>>>>>>>>>>>>>>>>>   +    81   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- UCRANIA  >>>>>>>>>>>>>>>>>>>>   +    73   >>>>>>>>>>>>>>>>>>>>>>>>  +     3   --")
        print("-- OMAN     >>>>>>>>>>>>>>>>>>>>   +    66   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- AZERBAIYAN>>>>>>>>>>>>>>>>>>>   +    65   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- KAZAJISTAN>>>>>>>>>>>>>>>>>>>   +    62   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- CISJORDANIA>>>>>>>>>>>>>>>>>>   +    57   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- GEORGIA  >>>>>>>>>>>>>>>>>>>>   +    54   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- UZBEKISTAN>>>>>>>>>>>>>>>>>>>   +    46   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- LIECHTENSTEIN>>>>>>>>>>>>>>>>   +    46   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- AFGANISTAN>>>>>>>>>>>>>>>>>>>   +    40   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- BANGLADES>>>>>>>>>>>>>>>>>>>>   +    33   >>>>>>>>>>>>>>>>>>>>>>>>  +     3   --")
        print("-- MONACO   >>>>>>>>>>>>>>>>>>>>   +    23   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- MONTENEGRO>>>>>>>>>>>>>>>>>>>   +    22   >>>>>>>>>>>>>>>>>>>>>>>>  +     1   --")
        print("-- KIRGUISTAN>>>>>>>>>>>>>>>>>>>   +    14   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- MALDIVAS >>>>>>>>>>>>>>>>>>>>   +    13   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- MONGOLIA >>>>>>>>>>>>>>>>>>>>   +    10   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- BUTAN    >>>>>>>>>>>>>>>>>>>>   +     2   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- KOSOVO   >>>>>>>>>>>>>>>>>>>>   +     2   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- TIMOR ORIENTAL>>>>>>>>>>>>>>>   +     1   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- VATICANO >>>>>>>>>>>>>>>>>>>>   +     1   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("-- SIRIA    >>>>>>>>>>>>>>>>>>>>   +     1   >>>>>>>>>>>>>>>>>>>>>>>>  +     /   --")
        print("=================================================================================\n")
        
        
        print("------------------------------------ AFRICA ------------------------------------")
        print("--  PAIS  ----------------------- CONTAGIADOS ------------------------ MUERTES  --")
        print("-- SUDAFRICA >>>>>>>>>>>>>>>>>>>>   +   402   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- EGIPTO    >>>>>>>>>>>>>>>>>>>>   +   327   >>>>>>>>>>>>>>>>>>>>>>>>  +   14  --")
        print("-- ARGELIA   >>>>>>>>>>>>>>>>>>>>   +   210   >>>>>>>>>>>>>>>>>>>>>>>>  +   17  --")
        print("-- MARRUECOS >>>>>>>>>>>>>>>>>>>>   +   134   >>>>>>>>>>>>>>>>>>>>>>>>  +    4  --")
        print("-- BURKINA FASO>>>>>>>>>>>>>>>>>>   +    99   >>>>>>>>>>>>>>>>>>>>>>>>  +    4  --")
        print("-- TUNEZ     >>>>>>>>>>>>>>>>>>>>   +    89   >>>>>>>>>>>>>>>>>>>>>>>>  +    3  --")
        print("-- SENEGAL   >>>>>>>>>>>>>>>>>>>>   +    67   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- CAMERUN   >>>>>>>>>>>>>>>>>>>>   +    56   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- NIGERIA   >>>>>>>>>>>>>>>>>>>>   +    36   >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- R.D DEL CONGO>>>>>>>>>>>>>>>>>   +    30   >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- MAURICIO  >>>>>>>>>>>>>>>>>>>>   +    28   >>>>>>>>>>>>>>>>>>>>>>>>  +    2  --")
        print("-- COSTA DE MARFIL>>>>>>>>>>>>>>>   +    25   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- GHANA     >>>>>>>>>>>>>>>>>>>>   +    24   >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- MAYOTTE   >>>>>>>>>>>>>>>>>>>>   +    21   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- GUERNSEY  >>>>>>>>>>>>>>>>>>>>   +    20   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- RUANDA    >>>>>>>>>>>>>>>>>>>>   +    19   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- TOGO      >>>>>>>>>>>>>>>>>>>>   +    18   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- KENIA     >>>>>>>>>>>>>>>>>>>>   +    15   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- MADAGASCAR>>>>>>>>>>>>>>>>>>>>   +    12   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- TANZANIA  >>>>>>>>>>>>>>>>>>>>   +    12   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- ETIOPIA   >>>>>>>>>>>>>>>>>>>>   +    11   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- SEYCHELLES>>>>>>>>>>>>>>>>>>>>   +     7   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- GUINEA ECUATORIAL>>>>>>>>>>>>>   +     6   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- GABON     >>>>>>>>>>>>>>>>>>>>   +     5   >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- GUINEA    >>>>>>>>>>>>>>>>>>>>   +     4   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- ESUATINI  >>>>>>>>>>>>>>>>>>>>   +     4   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- CABO VERDE>>>>>>>>>>>>>>>>>>>>   +     3   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- ZAMBIA    >>>>>>>>>>>>>>>>>>>>   +     3   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- REPUBLICA CENTROAFRICANA>>>>>>   +     3   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- CONGO     >>>>>>>>>>>>>>>>>>>>   +     3   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- NEPAL     >>>>>>>>>>>>>>>>>>>>   +     2   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- GAMBIA    >>>>>>>>>>>>>>>>>>>>   +     2   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- SUDAN     >>>>>>>>>>>>>>>>>>>>   +     2   >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- MOZAMBIQUE>>>>>>>>>>>>>>>>>>>>   +     1   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- CHAD      >>>>>>>>>>>>>>>>>>>>   +     1   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- YIBUTI    >>>>>>>>>>>>>>>>>>>>   +     1   >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("==================================================================================\n")

        print("------------------------------------ AMERICA ------------------------------------")
        print("--  PAIS  ----------------------- CONTAGIADOS ------------------------- MUERTES  --")
        print("-- EE.UU.  >>>>>>>>>>>>>>>>>>>>>    +41.451    >>>>>>>>>>>>>>>>>>>>>>>>  +  496  --")
        print("-- BRASIL  >>>>>>>>>>>>>>>>>>>>>    + 1.619    >>>>>>>>>>>>>>>>>>>>>>>>  +   25  --")
        print("-- CANADA  >>>>>>>>>>>>>>>>>>>>>    + 1.469    >>>>>>>>>>>>>>>>>>>>>>>>  +   21  --")
        print("-- ECUADOR >>>>>>>>>>>>>>>>>>>>>    +   789    >>>>>>>>>>>>>>>>>>>>>>>>  +   14  --")
        print("-- CHILE   >>>>>>>>>>>>>>>>>>>>>    +   632    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- PERU    >>>>>>>>>>>>>>>>>>>>>    +   363    >>>>>>>>>>>>>>>>>>>>>>>>  +    5  --")
        print("-- MEXICO  >>>>>>>>>>>>>>>>>>>>>    +   316    >>>>>>>>>>>>>>>>>>>>>>>>  +    2  --")
        print("-- PANAMA  >>>>>>>>>>>>>>>>>>>>>    +   313    >>>>>>>>>>>>>>>>>>>>>>>>  +    3  --")
        print("-- ARGENTINA>>>>>>>>>>>>>>>>>>>>    +   266    >>>>>>>>>>>>>>>>>>>>>>>>  +    4  --")
        print("-- COLOMBIA>>>>>>>>>>>>>>>>>>>>>    +   235    >>>>>>>>>>>>>>>>>>>>>>>>  +    2  --")
        print("-- REPUBLICA DOMINICANA>>>>>>>>>    +   202    >>>>>>>>>>>>>>>>>>>>>>>>  +    3  --")
        print("-- URUGUAY >>>>>>>>>>>>>>>>>>>>>    +   158    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- COSTA RICA>>>>>>>>>>>>>>>>>>>    +   134    >>>>>>>>>>>>>>>>>>>>>>>>  +    2  --")
        print("-- VENEZUELA>>>>>>>>>>>>>>>>>>>>    +    77    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- GUADALUPE>>>>>>>>>>>>>>>>>>>>    +    58    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- TRINIDAD Y TOBAGO>>>>>>>>>>>>    +    50    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- CUBA    >>>>>>>>>>>>>>>>>>>>>    +    35    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- HONDURAS>>>>>>>>>>>>>>>>>>>>>    +    27    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --") 
        print("-- BOLIVIA >>>>>>>>>>>>>>>>>>>>>    +    27    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- GUAM    >>>>>>>>>>>>>>>>>>>>>    +    27    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- PUERTO RICO>>>>>>>>>>>>>>>>>>    +    23    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- PARAGUAY>>>>>>>>>>>>>>>>>>>>>    +    22    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- GUYANA  >>>>>>>>>>>>>>>>>>>>>    +    19    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- JAMAICA >>>>>>>>>>>>>>>>>>>>>    +    19    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- GUATEMALA>>>>>>>>>>>>>>>>>>>>    +    19    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- GUAYANA FRANCESA>>>>>>>>>>>>>    +    18    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- BARBADOS>>>>>>>>>>>>>>>>>>>>>    +    17    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- ARUBA   >>>>>>>>>>>>>>>>>>>>>    +     9    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- BERMUDAS>>>>>>>>>>>>>>>>>>>>>    +     6    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- HAITI   >>>>>>>>>>>>>>>>>>>>>    +     5    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- SURINAM >>>>>>>>>>>>>>>>>>>>>    +     5    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- GROENLANDIA>>>>>>>>>>>>>>>>>>    +     4    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- ANTILLAS HOLANDESAS>>>>>>>>>>    +     3    >>>>>>>>>>>>>>>>>>>>>>>>  +    1  --")
        print("-- NICARAGUA>>>>>>>>>>>>>>>>>>>>    +     2    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- SANTA LUCIA>>>>>>>>>>>>>>>>>>    +     2    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- GRANADA >>>>>>>>>>>>>>>>>>>>>    +     1    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("-- ANTIGUA Y BARBUDA>>>>>>>>>>>>    +     1    >>>>>>>>>>>>>>>>>>>>>>>>  +    /  --")
        print("===================================================================================\n")



        print("----------------------------------- OCEANIA ------------------------------------")
        print("--  PAIS  ----------------------- CONTAGIADOS ------------------------ MUERTES  --")
        print("-- AUSTRALIA>>>>>>>>>>>>>>>>>>>>   + 1.682   >>>>>>>>>>>>>>>>>>>>>>>>  +    7   --")
        print("-- NUEVA ZELANDA>>>>>>>>>>>>>>>>   +   102   >>>>>>>>>>>>>>>>>>>>>>>>  +    /   --")
        print("-- POLINESIA FRANCESA>>>>>>>>>>>   +    18   >>>>>>>>>>>>>>>>>>>>>>>>  +    /   --")
        print("-- NUEVA CALEDONIA>>>>>>>>>>>>>>   +     8   >>>>>>>>>>>>>>>>>>>>>>>>  +    /   --")
        print("-- FIYI     >>>>>>>>>>>>>>>>>>>>   +     3   >>>>>>>>>>>>>>>>>>>>>>>>  +    /   --")
        print("-- PAPUA NUEVA GUINEA>>>>>>>>>>>   +     1   >>>>>>>>>>>>>>>>>>>>>>>>  +    /   --")
        print("==================================================================================\n")

        print("UN CASO ESPECIAL ES EL DEL CRUCERO DIAMOND PRINCESS: ")
        print("CONTAGIADOS: 712")
        print("MUERTES:  8")

    def mostrarFormulario():
        print("====== BIENVENIDO AL CENTRO INFORMATIVO ======")
        print("NUESTRA MISION ES MANEJAR LA INFORMACION SOBRE EL COVID-19\n")
        print("¡¡PARA AYUDAR EN ESTA CRISIS INTERNACIONAL PARTICIPA!!")
        print("LLEVAMOS UN REGISTRO DE CADA PERSONA QUE BUSCA INFORMACION EN ESTE CENTRO")
        print("ASI COMO TAMBIEN INFORMACION DE LO QUE SUCEDE A NIVEL MUNDIAL\n")
        print("QUE DESEAS REALIZAR?  ")
        print("(1) REGISTRARME ")
        print("(2) OBTENER INFORMACION")
        print("(3) CASOS A NIVEL MUNDIAL")
        print("¡¡SI SOSPECHA QUE PUEDE ESTAR CONTAGIADO!!")
        print("(4) REALIZAR DIAGNOSTICO CLINICO")
        print("(5) SALIR DEL CENTRO\n")
    hoy=2020    
    pasRiesgo = 0
    pasProp=0
    while True:
        mostrarFormulario()

        opcFor = input("DIGITE SU SELECCION:  ")
        if opcFor == "1":
            print("==== INICIANDO REGISTRO ====")
            nombre = input("NOMBRE:  ")
            apellido=input("APELLIDO:  ")
            print("-- FECHA DE NACIMIENTO --")
            dia = input("DIA:  ")
            mes = input("MES:  ")
            año = int(input("AÑO:  "))
            edad = hoy - año
            if ( edad> 40):
                print("USTED TIENE: ",edad," AÑOS")
                print("LAS EDADES DE RIESGO VAN DESDE LOS 40 AÑOS")
                print("DEBE MANTENER LA CUARENTENA Y EVITAR EXPONERSE AL CONTAGIO")
                pasRiesgo = pasRiesgo+1
            else:
                if(edad < 20):
                    print("USTED TIENE: ",edad," AÑOS")
                    print("LOS JOVENES SON LOS MAS PROPENSOS A PROPAGAR EL VIRUS EN LA SOCIEDAD")
                    print("LAS PERSONAS MAYORES SON LAS MAS AFECTADAS POR EL VIRUS")
                    print("ESTO NO HACE INMUNES A LOS JOVES")
                    pasProp=pasProp+1
                else:
                    print("USTED TIENE: ",edad," AÑOS")
                    print("DEBEN CUMPLIR CON LO IMPUESTO POR LAS AUTORIDADES SANITARIAS")
                    print("¡TRABAJAMOS POR Y PARA TI!")
            genero=input("GENERO:  F/M  ==> ")
            paisResi=input("PAIS DE RESIDENCIA:  ")

        if opcFor=="2":
            mostrarInfo()
        if opcFor=="3":
            mostrarMundial()
        if opcFor=="4":
            def mostrarDiag():
                print("NOTA: EL USUARIO/PACIENTE DEBE REALIZARSE UNA PRUEBA SEROLOGICA SI SOSPECHA O PRESENTA SINTOMAS\n")
                print("========= DIAGNOSTICO CLINICO =======")
                print("PRESENTA ALGUNO DE LOS SIGUIENTES SINTOMAS?")
                print("(1) FIEBRE")
                print("(2) TOS")
                print("(3) DOLORES")
                print("(4) GOTEO DE NARIZ")
                print("(5) DOLOR DE GARGANTA")
                print("(6) DIFICULTAD RESPIRATORIA")
                print("(7) ANOSMIA (NO ES CAPAZ DE PERCIBIR OLORES)")
                print("INDIQUE CUANTOS DE ESTOS SINTOMAS PRESENTA")
            sintomas = 0
            sospechoso = 0
            while True:
                mostrarDiag()

                opcDiag = int(input("SELECCION:  "))
                if opcDiag == 1:
                    print("PRESENTA UN SOLO SINTOMA")
                    sin = input("ESPECIFIQUE:  ")
                    sintomas=sintomas+1
                if opcDiag ==2:
                    print("PRESENTA DOS SINTOMAS")
                    sin = input("ESPECIFIQUE:  ")
                    sintomas=sintomas+2
                if opcDiag ==3:
                    print("PRESENTA TRES SINTOMAS")
                    sin = input("ESPECIFIQUE:  ")
                    sintomas=sintomas+3
                if opcDiag ==4:
                    print("PRESENTA CUATRO SINTOMAS")
                    sintomas=sintomas+4
                    sospechoso=sospechoso+1
                if opcDiag ==5:
                    print("PRESENTA CINCO SINTOMAS")
                    sintomas=sintomas+5
                    if (opcDiag == 5):
                        sospechoso = sospechoso+3
                        print("PACIENTE SOSPECHOSO")
                        print("DEBEN CUMPLIR CON LO IMPUESTO POR LAS AUTORIDADES SANITARIAS")
                    break
                if opcDiag ==6:
                    print("PRESENTA SEIS SINTOMAS")
                    sintomas=sintomas+6
                    if (opcDiag == 6):
                        sospechoso = sospechoso+3
                        print("PACIENTE SOSPECHOSO")
                        print("DEBEN CUMPLIR CON LO IMPUESTO POR LAS AUTORIDADES SANITARIAS")
                        print("DEBE REALIZARSE UNA PRUEBA SEROLOGICA")
                if opcDiag ==7:
                    print("PRESENTA SIETE SINTOMAS")
                    sintomas=sintomas+7
                    if (opcDiag ==7):
                        sospechoso = sospechoso+4
                        print("PACIENTE SOSPECHOSO")
                        print("DEBEN CUMPLIR CON LO IMPUESTO POR LAS AUTORIDADES SANITARIAS")
                        print("DEBE REALIZARSE UNA PRUEBA SEROLOGICA INMEDIATAMENTE")
                else:
                    break
        if opcFor=="5":
            sys.exit(0)        

       

    