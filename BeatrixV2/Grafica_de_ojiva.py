class Grafico_de_ojiva:
    def __init__(self):
        pass
    def dibujar (self,intervalos,nombre_archivo_final):
        
        print("\n\nGrafica de ojiva\n\n")
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write("\n\nGrafica de ojiva\n\n")
        
        lista_acomodar = [sublista[1] for sublista in intervalos]
        lista_con_intervalos= self.acomodar_lista(lista_acomodar)
        numero_de_intervalos=len(lista_con_intervalos)
        lista_con_nombre = [sublista[0] for sublista in intervalos]
        nombre_intervalo_grande= max(lista_con_nombre, key=len)
        intervalo_mas_grande= max(lista_con_intervalos)
        espacio_inter=2
        espacio=6
        if (len(nombre_intervalo_grande)>6):
            espacio=len(nombre_intervalo_grande)
        if (len(str(intervalo_mas_grande))>1):
            espacio_inter= len(str(intervalo_mas_grande))
        
        for i in range (numero_de_intervalos):         
            mensaje= []
            contador=numero_de_intervalos
            for j in  range(len(intervalos)):
                #PARA ESPACIO NORMAL
                if (intervalos[j][1]==lista_con_intervalos[i]):
                    forma_linea= "\u2501\u2501\u2501\u25CF\u2501\u2501".center(espacio," ")
                    mensaje.append (forma_linea)
                elif (intervalos[j][1]>  lista_con_intervalos[i]):
                    forma_linea = "\u2800".center(espacio," ")
                    mensaje.append (forma_linea)
                else:
                    forma_linea = "\u2800".center(espacio," ")
                    mensaje.append (forma_linea)
                #PARA ESPACIO INTERMEDIO
                if (contador >= 0):
                    try:
                        forma_linea = self.determinar_espacio_intermedio(lista_con_intervalos[i],intervalos[j][1],intervalos[j+1][1])
                    except (IndexError):
                        forma_linea = self.determinar_espacio_intermedio(lista_con_intervalos[i],intervalos[j][1],intervalos[j][1])
                        
                    mensaje.append (forma_linea)
                    contador-=1

            linea_contructura= ("") .join (mensaje)
            
            print ("\033["+"7;30;45"+"m "+ str(lista_con_intervalos[i]).center(espacio_inter," ") +"\u2523"+" "+linea_contructura+" ".center(espacio_inter,"\u2800")+"\033[0m")
        
            with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
                f.write(" "+ str(lista_con_intervalos[i]).center(espacio_inter," ") +"\u2523"+" "+linea_contructura+" ".center(espacio_inter,"\u2800")+"" +"\n")
        
        print ("\033["+"7;30;45"+"m "+" ".center(espacio_inter," ")+("\u2517")+"\u2501"+((("\u2501")+('\u2501')+('\u2501')+("\u2533")+('\u2501')+('\u2501')).center(espacio+1,"\u2501"))*(len(lista_acomodar))+" ".center(espacio_inter," ")+"\033[0m")
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write(" "+" ".center(espacio_inter," ")+("\u2517")+"\u2501"+((("\u2501")+('\u2501')+('\u2501')+("\u2533")+('\u2501')+('\u2501')).center(espacio+1,"\u2501"))*(len(lista_acomodar))+" ".center(espacio_inter," ")+"" +"\n")
        
        contador=[]
        num_contador=0
        for i in range (len(lista_con_nombre)):
            lista_con_nombre[i]=str(lista_con_nombre[i]).center(espacio,"\u2800")
            num_contador +=1
            contador.append(str(num_contador))
        linea_intervalos= ((" ")*(espacio))  .join (contador)

        print ("\033["+"7;30;45"+"m"+" ".center(espacio+2,"\u2800")+linea_intervalos+" ".center(espacio,"\u2800")+"\033[0m")
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write(""+" ".center(espacio+2,"\u2800")+linea_intervalos+" ".center(espacio,"\u2800")+"" +"\n")
        
        
        for i in  range (len(lista_con_nombre)):
            print("\n\nGrafica de ojiva\n\n")
            print ("\033["+"7;30;45"+"m "+contador[i]+" = "+lista_con_nombre[i]+"\u2800"+"\033[0m") 

            with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
                f.write("\n\nGrafica de ojiva\n\n")
                f.write(" "+contador[i]+" = "+lista_con_nombre[i]+"\u2800"+"" +"\n")
        
    
    
    def acomodar_lista(self, intervalos):
    # Eliminar duplicados convirtiendo la lista a un conjunto
        conjunto_intervalos = set(intervalos)
        lista_ordenada = list(conjunto_intervalos)
    
    # Implementar el algoritmo de ordenamiento burbuja para ordenar de mayor a menor
        n = len(lista_ordenada)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista_ordenada[j] < lista_ordenada[j+1]:  
                    lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
    
        return lista_ordenada
    def determinar_espacio_intermedio (self,fr,fri,frd):
        if (fr >=fri):
            izquierda = True
        else:
            izquierda = False
        if (fr >= frd):
            derecha = True
        else:
            derecha = False
        if (izquierda== True and derecha ==False):
            if (fri==fr):
                return("\u251B")
            elif (frd==fr):
                return("\u2517")
            else:
                return("\u2503")
        if (izquierda== False and derecha ==True):
            if (fri==fr):
                return("\u251B")
            elif (frd==fr):
                return("\u2517")
            else:
                return("\u2503")
        if (izquierda== False and derecha ==False):
            return("\u2800")
        if (izquierda== True and derecha ==True) :
            if (fri > fr and frd >fr):
                return("\u2800")
            if (fri == fr and frd ==fr):
                return("\u2501")
            if (fri > frd):
                if (fri==fr):
                    return("\u2513")
                elif (frd==fr):
                    return("\u2517")
                else:
                    return("\u2800")
            if (frd>fri):
                if (fri==fr):
                    return("\u251B")
                elif (frd==fr):
                    return("\u250F")
                else:
                    return("\u2800")
        return("\u2800")


'''nueva_accion = accion_8 ()
intervalos_prueba=  [['21.2-21.8',72, 0.002, 0.002, 0.2, 0.2, 0.72], ['21.9-22.5',2610, 0.0712, 0.073, 7.12, 7.32, 25.63], ['22.6-23.2',2824, 0.0771, 0.15, 7.71, 15.03, 27.76], ['23.3-23.9',6183, 0.1688, 0.319, 16.88, 31.91, 60.77], ['24.0-24.6', 9727, 0.2655, 0.585, 26.55, 58.46, 95.58], ['24.7-25.3', 9468, 0.2584, 0.843, 25.84, 84.3, 93.02], ['25.4-26.0', 4282, 0.1169, 0.96, 11.69, 95.99, 42.08], ['26.1-26.7', 1172, 0.032, 0.992, 3.2, 99.19, 11.52], ['26.8-27.4', 296, 0.0081, 1.0, 0.81, 100.0, 2.92], ['27.5-28.1', 0, 0.0, 1.0, 0.0, 100.0, 0.0]]
nueva_accion.dibujar (intervalos_prueba)'''
