from Cuadro_de_frecuencias_intervalos import Cuadro_de_frecuencias_intervalos as cuadro_de_frecuencias
from Controlador_vista_medidas_de_tendencia_central import Controlador_vista_medidas_de_tendencia_central
from Grafica_de_frecuencias import accion_1

class Controlador_vista_cuadro_de_frecuencias_intervalos():
    #Atributos
    un_cuadro_de_frecuencias= cuadro_de_frecuencias()
    unas_medidas_de_tendencia= Controlador_vista_medidas_de_tendencia_central()
    una_grafica_de_frecuencias= accion_1()

    #Metodos
    #Metodo constructor
    def __init__(self,):
        pass

    #Metodo para llenar una lista con todos los datos para analizar
    def ingresar_y_almacenar_todos_los_datos(self):
        archivo_csv= input("Por favor ingrese la raiz del archivo .csv a evaluar, asegurese de que los datos se encuentren seaparados por comas ','\n Ej: D:\\Programacion\\repositorios\\BeatrixV2\\base de datos para pruebas meteorologica\\datos1.csv\n : ")
        #i=0
        datos_temperatura_interior=[]
        datos_humedad_interior=[]
        datos_temperatura_exterior=[]
        datos_humedad_exterior=[]
        datos_presion_relativa=[]
        datos_presion_absoluta=[]
        
        with open(archivo_csv, mode='r') as archivo:
            # Leer los datos del archivo CSV fila por fila 
            # Convertir los datos de temperatura y presion de String a float
            # Convertir los datos de humedad de String a int
            for linea in archivo:
                # Eliminar caracteres de nueva línea y separar por comas
                fila = linea.strip().split(',')
                
                if(fila[3]!=''):
                    datos_temperatura_interior.append(float(fila[3]))
                
                if(fila[4]!=''):    
                    datos_humedad_interior.append(int(fila[4]))
                
                if(fila[5]!='--.-' and fila[5]!=''):
                    datos_temperatura_exterior.append(float(fila[5]))
                    
                    
                if(fila[6]!='--' and fila[6]!=''):
                    datos_humedad_exterior.append(int(fila[6]))    
                
                if(fila[7]!=''):
                    datos_presion_relativa.append(float(fila[7]))
                
                if(fila[8]!=''):
                    datos_presion_absoluta.append(float(fila[8]))

        
        self.un_cuadro_de_frecuencias.set_datos_temperatura_interior(datos_temperatura_interior)
        self.un_cuadro_de_frecuencias.set_datos_humedad_interior(datos_humedad_interior)
        self.un_cuadro_de_frecuencias.set_datos_temperatura_exterior(datos_temperatura_exterior)
        self.un_cuadro_de_frecuencias.set_datos_humedad_exterior(datos_humedad_exterior)
        self.un_cuadro_de_frecuencias.set_datos_presion_relativa(datos_presion_relativa)
        self.un_cuadro_de_frecuencias.set_datos_presion_absoluta(datos_presion_absoluta)
         
        #Llamado al metodo determinar_el_ancho_de_cada_intervalo para decifrar la cantidad de elementos que se encontrarán en el rango de cada
        #intervalo
            
        self.determinar_el_ancho_de_cada_intervalo ()
    
    def copiar_lista(self):
        lista= []
        if(self.un_cuadro_de_frecuencias.numero_lista==1):
            for dato in self.un_cuadro_de_frecuencias.get_datos_temperatura_interior():
                lista.append(dato)
                
        elif(self.un_cuadro_de_frecuencias.numero_lista==2):
            for dato in self.un_cuadro_de_frecuencias.get_datos_humedad_interior():
                lista.append(dato)
            
        elif(self.un_cuadro_de_frecuencias.numero_lista==3):
            for dato in self.un_cuadro_de_frecuencias.get_datos_temperatura_exterior():
                lista.append(dato)
        
        elif(self.un_cuadro_de_frecuencias.numero_lista==4):
            for dato in self.un_cuadro_de_frecuencias.get_datos_humedad_exterior():
                lista.append(dato)
        
        elif(self.un_cuadro_de_frecuencias.numero_lista==5):
            for dato in self.un_cuadro_de_frecuencias.get_datos_presion_relativa():
                lista.append(dato)
        
        elif(self.un_cuadro_de_frecuencias.numero_lista==6):
            for dato in self.un_cuadro_de_frecuencias.get_datos_presion_absoluta():
                lista.append(dato)
        
        return lista
     
    
    #Método para  determinar el ancho de cada intervalo con base a restar el numero_mayor con el numero_menor y dividir todo entre el numero de intervalos
    def determinar_el_ancho_de_cada_intervalo(self):
        todos_los_datos=[]
        
        for dato in self.copiar_lista():
            todos_los_datos.append(dato)

        todos_los_datos.sort()

        num_intervalos= int(input("Por favor ingrese el numero de intervalos que quiere que aparezcan en la tabla de frecuenncias, minimo 5:  "))
        while (num_intervalos<4):
            num_intervalos= int(input("Por favor ingrese el numero de intervalos que quiere que aparezcan en la tabla de frecuenncias, minimo 5:  "))
         
        numero_mas_pequeno= min(todos_los_datos)
        numero_mas_grande=max(todos_los_datos)
        
        if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):
            ancho_intervalos= round((numero_mas_grande- numero_mas_pequeno)/num_intervalos)
            
        elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
            ancho_intervalos= round((numero_mas_grande- numero_mas_pequeno)/num_intervalos,1)
            
        else:
            ancho_intervalos= round((numero_mas_grande- numero_mas_pequeno)/num_intervalos,2)
        
        #Llamado al metodo determinar_frecuencias_en_grados para continuar con la recoleccion de las frecuencias
        self.determinar_intervalos(ancho_intervalos, num_intervalos,todos_los_datos)
        
        
    #Metodo para hacer la lista de los intervalos que se van a crear, aunque la lista es visual, de tipo string
    def determinar_intervalos(self, ancho_intervalos,num_intervalos,todos_los_datos ):
        intervalos= []
        if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):
                menor= (min(todos_los_datos) -1)
        elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
                menor= (min(todos_los_datos) -0.1)
           
        else:
            menor= (min(todos_los_datos) -0.01)
            
        mayor= (menor + ancho_intervalos)
        
        #Desicion para determinar como se van a crear los intervalos segun si los numeros son enteros o decimales
        if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):
            #ciclo para rellenar la lista intervalos con los mensajes de los intervalos que se evaluaran en un rato
            for i in range(num_intervalos):
                intervalo= "("+str(menor)+"-"+str(mayor)+")"
                intervalos.append(intervalo)
                menor+=(ancho_intervalos + 1)
                mayor+= (ancho_intervalos + 1)
                
        elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
            #ciclo para rellenar la lista intervalos con los mensajes de los intervalos que se evaluaran en un rato
            for i in range(num_intervalos):
                intervalo= str(round(menor,2))+"-"+str(round(mayor,2))
                intervalos.append(intervalo)
                menor+=(ancho_intervalos + 0.1)
                mayor+= (ancho_intervalos + 0.1)
        
        else:
             #ciclo para rellenar la lista intervalos con los mensajes de los intervalos que se evaluaran en un rato
            for i in range(num_intervalos):
                intervalo= str(round(menor,3))+"-"+str(round(mayor,3))
                intervalos.append(intervalo)
                menor+=(ancho_intervalos + 0.01)
                mayor+= (ancho_intervalos + 0.01)
            
        self.un_cuadro_de_frecuencias.set_datos_para_evaluar(intervalos)
        
        #Llamado al metodo determinar_la_frecuencia_de_aparicion_de_los_intervalos para continuar con la recoleccion de las frecuencias
        self.determinar_la_frecuencia_de_aparicion_de_los_intervalos(todos_los_datos,ancho_intervalos, num_intervalos,intervalos)
        
        
    #Metoto para determinar la cantidad de veces que un numero se encuentra en los rangos de cada intervalo 
    def determinar_la_frecuencia_de_aparicion_de_los_intervalos(self,todos_los_datos, ancho_intervalos, num_intervalos,intervalos):
        frecuencia_aparicion_intervalos= list()
        iteracion=0
        if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):
            menor= round(min(todos_los_datos) -1, 2)
           
        elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
                menor= (min(todos_los_datos) -0.1)
           
        else:
            menor= (min(todos_los_datos) -0.01)
            
        mayor= round(menor + ancho_intervalos, 2)
        
        #ciclo para determinar si un numero de todos los ingresados se encuentra en el rango de los intervalos
        while iteracion<= (num_intervalos-1):
            frecuencia=0
            for i in todos_los_datos:
                if (i>=menor and i<=mayor):
                    frecuencia+=1
                    
                    
            if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):                    
                frecuencia_aparicion_intervalos.append(frecuencia)
                menor+=(ancho_intervalos + 1)
                mayor+= (ancho_intervalos + 1)
                
            elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
                frecuencia_aparicion_intervalos.append(frecuencia)
                menor+= (ancho_intervalos + 0.1)
                menor = round(menor, 2)
                mayor+= (ancho_intervalos + 0.1)
                mayor = round(mayor,2)
                
            else:
                frecuencia_aparicion_intervalos.append(frecuencia)
                menor+= (ancho_intervalos + 0.01)
                menor = round(menor, 3)
                mayor+= (ancho_intervalos + 0.01)
                mayor = round(mayor,3)
                
            
            iteracion +=1
        
        suma=0
        for i in frecuencia_aparicion_intervalos:
            suma+=i
        print (suma)
            
        #Se envia la lista frecuencias_de_aparicion al objeto un_cuadro_de_frecuencia en el atributo frecuencia_de_aparicion
        self.un_cuadro_de_frecuencias.set_frecuencias_de_apari(frecuencia_aparicion_intervalos)
        
           
        self.determinar_las_frecuencias_relativas(frecuencia_aparicion_intervalos, todos_los_datos, intervalos)   
        
      
    #Metodo para obtener la frecuencia relativa de un dato con base a dividir su frecuencia entre el total de datos ingresados
    def determinar_las_frecuencias_relativas(self,frecuencias_de_apari, todos_los_datos, intervalos):
        frecuencias_relativas= list()
        
        for i in range(len(frecuencias_de_apari)):
            #operacion para dividir la frecuencia de apariciones de cada dato entre el total de datos ingresados, limitando la cantidad de decimales a 4
            frecuencias_relativas.append(round(frecuencias_de_apari[i]/(len(todos_los_datos)),4))
        
         #mandar la lista de frecuencias relativas  al objeto un_cuadro_de_frecuencias para almacenar los datos en el atributo de lista fecuencias_relativas    
        self.un_cuadro_de_frecuencias.set_frecuencias_relativas(frecuencias_relativas)
        
        #Llamado al metodo determinar_las_fecuencias_rel_acum para continuar con la recoleccion de las frecuencias
        self.determinar_las_fecuencias_rel_acum(frecuencias_relativas, todos_los_datos, frecuencias_de_apari, intervalos)

    
    #Metodo para obtener la frecuencia relativa acumulada sumando consecutivamente los elementos de la lista de las frecuencias relativas    
    def determinar_las_fecuencias_rel_acum(self, frecuencias_relativas,todos_los_datos, frecuencias_de_apari, intervalos):
        frecuencias_rel_acum= list()
        acumulado=0
        
        #Ciclo para asignarle a la variable acumulado la suma consecutiva de los elementos de la lista frecuencias_relativas
        for i in range(len(frecuencias_relativas)):
            acumulado+= frecuencias_relativas[i]
            acumulado_redondeado=round(acumulado,3)
            frecuencias_rel_acum.append(acumulado_redondeado)
            
        #mandar la lista de frecuencias relativas acumuladas al objeto un_cuadro_de_frecuencias para almacenar los datos en el atributo de lista fecuencias_rel_acum
        self.un_cuadro_de_frecuencias.set_frecuencias_relat_acu(frecuencias_rel_acum)
        
        self.determinar_frecuencias_porcentuales(frecuencias_relativas,todos_los_datos, frecuencias_de_apari, intervalos)
        
       
   #Metodo que saca la frecuencia porcentual tras multiplicar por 100 la frecuencia relativa 
    def determinar_frecuencias_porcentuales(self,frecuencias_relativas, todos_los_datos, frecuencias_de_apari, intervalos):
        frecuencias_porcentuales= list()

        for i in range(len(frecuencias_relativas)):
            frecu_porcent=round(frecuencias_relativas[i]*100,4)
            frecuencias_porcentuales.append(frecu_porcent)
            
        self.un_cuadro_de_frecuencias.set_frecuencias_procentuales(frecuencias_porcentuales)
        
        #Llamado al metodo determinar_las_fecuencias_rel_acum para continuar con la recoleccion de las frecuencias
        self.determinar_frecuencias_porcent_acum(frecuencias_porcentuales, todos_los_datos, frecuencias_de_apari, intervalos)
        
         
    #Metodo que almacena la sumatoria consecutiva de los datos de la lista de frecuencias_porcentuales
    def determinar_frecuencias_porcent_acum(self,frecuencias_porcentuales, todos_los_datos, frecuencias_de_apari, intervalos):
        frecuencias_porcent_acum= list()
        acumulado=0
        
        #Ciclo para asignarle a la variable acumulado la suma consecutiva de los elementos de la lista frecuencias_porcentuales
        for i in range(len(frecuencias_porcentuales)):
            acumulado+= frecuencias_porcentuales[i]
            acumulado_redondeado=round(acumulado,3)
            frecuencias_porcent_acum.append(acumulado_redondeado)
            
        
        self.un_cuadro_de_frecuencias.set_frecuencias_porcent_acu(frecuencias_porcent_acum)
        
        #Llamado al metodo determinar_frecuencias_en_grados para continuar con la recoleccion de las frecuencias
        self.determinar_frecuencias_en_grados(todos_los_datos, frecuencias_de_apari, intervalos)
        
       
    #Metodo que me permite convertir la frecuencia relativa en grados para poder repartirlos correctamente en un grafico de pastel   
    def determinar_frecuencias_en_grados(self, todos_los_datos, frecuencias_de_apari, intervalos):
        frecuencias_en_grados= list()
        frecuencias_relativas= self.un_cuadro_de_frecuencias.get_frecuencias_relativas()
        
        for i in range(len(frecuencias_relativas)):
            frecuencias_en_grados.append(round(frecuencias_relativas[i]*360,2))
            
        
        self.un_cuadro_de_frecuencias.set_frecuencias_en_grados(frecuencias_en_grados)
        
        tabla= self.un_cuadro_de_frecuencias.mostrar_la_tabla_de_frecuencias()
        
        
        #llamado al metodo para mostrar los datos organizados
        self.llamar_a_la_vista_para_mostrar_la_tabla_de_frecuencia(tabla, todos_los_datos, frecuencias_de_apari, intervalos)

     
    #metodo para llamar a la vista y mostrar los datos organizados
    def llamar_a_la_vista_para_mostrar_la_tabla_de_frecuencia(self, tabla, todos_los_datos, frecuencias_de_apari, intervalos):

        print("\n\n Tabla ",self.un_cuadro_de_frecuencias.get_numero_lista())
        self.una_grafica_de_frecuencias.dibujar(tabla)
        
        self.un_cuadro_de_frecuencias.set_numero_lista(self.un_cuadro_de_frecuencias.get_numero_lista() +1)
        
        '''if(self.un_cuadro_de_frecuencias.get_numero_lista() < 7 ):
            self.determinar_el_ancho_de_cada_intervalo()'''

        self.unas_medidas_de_tendencia.calcular_la_media(todos_los_datos,frecuencias_de_apari, intervalos)
    
  