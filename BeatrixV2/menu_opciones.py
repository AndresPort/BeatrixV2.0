class menu:
    #Constructor 
    def __init__(self):
        pass
    
    #Metodo para dibujar el menu
    def dibujar (self, nombre_archivo_final):
        print ("\033["+"7;30;45"+"m "+'\u250F'+('\u2501')*95+'\u2513'" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                \u2572     \u2571\u203E\u2572     \u2571  \u250C\u2500\u2500\u2500   \u2502    \u250C\u2500\u2500\u2500  \u256D\u2500\u2500\u2500\u256E   \u2571\u203E\u2572   \u2571\u203E\u2572   \u250C\u2500\u2500\u2500                    \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                 \u2572   \u2571   \u2572   \u2571   \u251C\u2500\u2500\u2500   \u2502    \u2502     \u2502   \u2502  \u2571   \u2572_\u2571   \u2572  \u251C\u2500\u2500\u2500                    \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                  \u2572\u005F\u2571     \u2572\u005F\u2571    \u2514\u2500\u2500\u2500   \u2514\u2500\u2500\u2500 \u2514\u2500\u2500\u2500  \u2570\u2500\u2500\u2500\u256F \u2571           \u2572 \u2514\u2500\u2500\u2500                    \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                       \u2500\u2500\u2500\u252C\u2500\u2500\u2500 \u256D\u2500\u2500\u2500\u256E                                           \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                          \u2502    \u2502   \u2502                                           \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                          \u2502    \u2570\u2500\u2500\u2500\u256F                                           \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                         \u250c\u2500\u2500\u2500\u256E  \u250c\u2500\u2500\u2500    \u2571\u203E\u2572   \u2500\u2500\u2500\u252C\u2500\u2500\u2500 \u250c\u2500\u2500\u2500\u2510  \u2500\u2500\u2500\u252C\u2500\u2500\u2500   \u2572 \u2571                     \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                         \u251C\u2500\u2500\u2500\u2524  \u251C\u2500\u2500\u2500   \u2571 \u2500 \u2572     \u2502    \u2502\u2500\u2500\u2500\u2518     \u2502       \u2573                      \u2503"+" \033[0m")   
        print ("\033["+"7;30;45"+"m "+"\u2503                         \u2514\u2500\u2500\u2500\u256F  \u2514\u2500\u2500\u2500  \u2571     \u2572    \u2502    \u2502  \u2572   \u2500\u2500\u2500\u2534\u2500\u2500\u2500   \u2571 \u2572                     \u2503"+" \033[0m") 
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2523" +('\u2501')*95+"\u252B"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                DIGITE LA OPEACION QUE SEA HACER                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503  1. MOSTRAR TABLA DE FRECUENCIA    5. GRAFICO DE PUNTOS              9. DIAGRAMA DE CAJA      \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503  2. MEDIDAS DE TENDENCIA CENTRAL   6. MOSTRAR DIAGRAMA DE BARRAS    10. OJIVA                 \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503  3. MOSTRAR HISTOGRAMA             7. TEOREMA DE CHEBYSHEV Y        11.                       \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                        MEDIDAS DE VARIABILIDAD                                \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503  4. DIAGRAMA DE TORTAS             8. DIAGRAMA DE DISPERSION        12. TODOS LOS GRAFICOS    \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+'\u2517'+('\u2501')*95+'\u251B'+" \033[0m")
        
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write('\u250F'+('\u2501')*95+'\u2513'"\n" +
                    "\u2503                                                                                               \u2503"+" \n"+
                    "\u2503                \u2572     \u2571\u203E\u2572     \u2571  \u250C\u2500\u2500\u2500   \u2502    \u250C\u2500\u2500\u2500  \u256D\u2500\u2500\u2500\u256E   \u2571\u203E\u2572   \u2571\u203E\u2572   \u250C\u2500\u2500\u2500                    \u2503"+" \n"
                    "\u2503                 \u2572   \u2571   \u2572   \u2571   \u251C\u2500\u2500\u2500   \u2502    \u2502     \u2502   \u2502  \u2571   \u2572_\u2571   \u2572  \u251C\u2500\u2500\u2500                    \u2503"+"  \n"+
                    "\u2503                  \u2572\u005F\u2571     \u2572\u005F\u2571    \u2514\u2500\u2500\u2500   \u2514\u2500\u2500\u2500 \u2514\u2500\u2500\u2500  \u2570\u2500\u2500\u2500\u256F \u2571           \u2572 \u2514\u2500\u2500\u2500                    \u2503"+"  \n"+
                    "\u2503                                                                                               \u2503"+"  \n"+
                    "\u2503                                                                                               \u2503"+"  \n"+
                    "\u2503                                       \u2500\u2500\u2500\u252C\u2500\u2500\u2500 \u256D\u2500\u2500\u2500\u256E                                           \u2503"+"  \n"+
                    "\u2503                                          \u2502    \u2502   \u2502                                           \u2503"+"  \n"+
                    "\u2503                                          \u2502    \u2570\u2500\u2500\u2500\u256F                                           \u2503"+"  \n"+
                    "\u2503                                                                                               \u2503"+"  \n"+
                    "\u2503                                                                                               \u2503"+"  \n"+
                    "\u2503                         \u250c\u2500\u2500\u2500\u256E  \u250c\u2500\u2500\u2500    \u2571\u203E\u2572   \u2500\u2500\u2500\u252C\u2500\u2500\u2500 \u250c\u2500\u2500\u2500\u2510  \u2500\u2500\u2500\u252C\u2500\u2500\u2500   \u2572 \u2571                     \u2503"+"  \n"+
                    "\u2503                         \u251C\u2500\u2500\u2500\u2524  \u251C\u2500\u2500\u2500   \u2571 \u2500 \u2572     \u2502    \u2502\u2500\u2500\u2500\u2518     \u2502       \u2573                      \u2503"+"  \n"+
                    "\u2503                         \u2514\u2500\u2500\u2500\u256F  \u2514\u2500\u2500\u2500  \u2571     \u2572    \u2502    \u2502  \u2572   \u2500\u2500\u2500\u2534\u2500\u2500\u2500   \u2571 \u2572                     \u2503"+"  \n"+
                    "\u2503                                                                                               \u2503"+"  \n"+
                    "\u2523" +('\u2501')*95+"\u252B"+"  \n"+
                    "\u2503                                DIGITE LA OPEACION QUE SEA HACER                               \u2503"+"  \n"+
                    "\u2503  1. MOSTRAR TABLA DE FRECUENCIA    5. GRAFICO DE PUNTOS              9. DIAGRAMA DE CAJA      \u2503"+"  \n"+
                    "\u2503  2. MEDIDAS DE TENDENCIA CENTRAL   6. MOSTRAR DIAGRAMA DE BARRAS    10. OJIVA                 \u2503"+"  \n"+
                    "\u2503  3. MOSTRAR HISTOGRAMA             7. TEOREMA DE CHEBYSHEV Y        11.                       \u2503"+"  \n"+
                    "\u2503                                        MEDIDAS DE VARIABILIDAD                                \u2503"+"  \n"+
                    "\u2503                                                                                               \u2503"+"  \n"+
                    "\u2503  4. DIAGRAMA DE TORTAS             8. DIAGRAMA DE DISPERSION        12. TODOS LOS GRAFICOS    \u2503"+"  \n"+
                    '\u2517'+('\u2501')*95+'\u251B'+"  \n"
                    
                    
                    
                    
                    
                    
                    
                    )
        

        while True:
            try:
                respuesta = int(input("Ingrese un número entre 1 y 12: "))
                if 1 <= respuesta <= 12:
                    return respuesta
                else:
                    print("Debe ingresar una de las 12 opciones.")
            except ValueError:
                print("Debe ingresar un número válido.")
 