# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

estados_finais = [
        'q51','q45','q47','q24','q61',
        'q72','q21','q18','q7','q12',
        'q30','q34','q38','q59','q54',
        'q63','q69','q80','q84','q43'
    ]
tabela_ids = []
tabela_reservadas = []
lexema = []
caracteres_especiais = [',',':',';','=','(',')']

def verificarInsercaoReservadas(palavra):
    if(palavra in tabela_reservadas):
        return True
    return False

def verificarInsercaoIds(palavra):
    if(palavra in tabela_ids):
        return True
    return False

def lendoArquivo():
    dados = open('dados.txt', 'r')
    valores = []
    for i in dados:
        for j in i:
            valores.append(j)
    return valores
           
def maquinaEstados(dados):
    estadofinal = 'q0'
    for i in dados:
        if(i == ' ' or i == '\n' or i in caracteres_especiais):
            if(estadofinal in estados_finais):
                valor_lexema = "".join(lexema)
                if(verificarInsercaoReservadas(valor_lexema) != 1):
                    tabela_reservadas.append(valor_lexema)
                estadofinal = 'q0'
                print('\n')
            else:
                valor_lexema = "".join(lexema)
                if(verificarInsercaoIds(valor_lexema)!= 1 and valor_lexema != ''):
                    tabela_ids.append(valor_lexema)
                estadofinal = 'q0'
                print('\n')
            lexema.clear()
            
        else:
            lexema.append(i)
            estadofinal = verificarEstado(estadofinal,i)
            
def verificarEstado(estadoAtual,i):
    
    if(estadoAtual == 'q0' and i == 'w'):
        estado = 'q39'
    elif(estadoAtual == 'q39' and i == 'h'):
        estado = 'q48'
    elif(estadoAtual == 'q39' and i == 'r'):
        estado = 'q40'
    elif(estadoAtual == 'q48' and i == 'i'):
        estado = 'q49'
    elif(estadoAtual == 'q49' and i == 'l'):
        estado = 'q50'
    elif(estadoAtual == 'q50' and i == 'e'):
        estado = 'q51'
    elif(estadoAtual == 'q40' and i == 'i'):
        estado = 'q41'
    elif(estadoAtual == 'q41' and i == 't'):
        estado = 'q42'
    elif(estadoAtual == 'q42' and i == 'e'):
        estado = 'q43'
    elif(estadoAtual == 'q43' and i == 'l'):
        estado = 'q44'
    elif(estadoAtual == 'q44' and i == 'n'):
        estado = 'q45'  
        
        
    elif(estadoAtual == 'q0' and i == 'd'):
        estado = 'q46'
    elif(estadoAtual == 'q46' and i == 'o'):
        estado = 'q47'       
        
        
    elif(estadoAtual == 'q0' and i == 'o'):
        estado = 'q60'
    elif(estadoAtual == 'q60' and i == 'f'):
        estado = 'q61'        
                
        
    elif(estadoAtual == 'q0' and i == 'e'):
        estado = 'q19'
    elif(estadoAtual == 'q19' and i == 'l'):
        estado = 'q70'
    elif(estadoAtual == 'q70' and i == 's'):
        estado = 'q71'
    elif(estadoAtual == 'q71' and i == 'e'):
        estado = 'q72'
    elif(estadoAtual == 'q19' and i == 'n'):
        estado = 'q20'
    elif(estadoAtual == 'q20' and i == 'd'):
        estado = 'q21'
        
        
    elif(estadoAtual == 'q0' and i == 'p'):
        estado = 'q1'
    elif(estadoAtual == 'q1' and i == 'r'):
        estado = 'q2'
    elif(estadoAtual == 'q2' and i == 'o'):
        estado = 'q3'
    elif(estadoAtual == 'q3' and i == 'c'):
        estado = 'q13'
    elif(estadoAtual == 'q13' and i == 'e'):
        estado = 'q14'
    elif(estadoAtual == 'q14' and i == 'd'):
        estado = 'q15'
    elif(estadoAtual == 'q15' and i == 'u'):
        estado = 'q16'
    elif(estadoAtual == 'q16' and i == 'r'):
        estado = 'q17'
    elif(estadoAtual == 'q17' and i == 'e'):
        estado = 'q18'
    elif(estadoAtual == 'q3' and i == 'g'):
        estado = 'q4'
    elif(estadoAtual == 'q4' and i == 'r'):
        estado = 'q5'
    elif(estadoAtual == 'q5' and i == 'a'):
        estado = 'q6'
    elif(estadoAtual == 'q6' and i == 'm'):
        estado = 'q7'
        
        
        
    elif(estadoAtual == 'q0' and i == 'b'):
        estado = 'q8'
    elif(estadoAtual == 'q8' and i == 'e'):
        estado = 'q9'
    elif(estadoAtual == 'q9' and i == 'g'):
        estado = 'q10'
    elif(estadoAtual == 'q10' and i == 'i'):
        estado = 'q11'
    elif(estadoAtual == 'q11' and i == 'n'):
        estado = 'q12'
    elif(estadoAtual == 'q8' and i == 'o'):
        estado = 'q25'
    elif(estadoAtual == 'q25' and i == 'o'):
        estado = 'q26'
    elif(estadoAtual == '26' and i == 'l'):
        estado = 'q27'
    elif(estadoAtual == 'q27' and i == 'e'):
        estado = 'q28'
    elif(estadoAtual == 'q28' and i == 'a'):
        estado = 'q29'
    elif(estadoAtual == 'q29' and i == 'n'):
        estado = 'q30'
        
        
    elif(estadoAtual == 'q0' and i == 't'):
        estado = 'q31'
    elif(estadoAtual == 'q31' and i == 'h'):
        estado = 'q32'
    elif(estadoAtual == 'q32' and i == 'e'):
        estado = 'q33'
    elif(estadoAtual == 'q33' and i == 'n'):
        estado = 'q34'
    
        
        
    elif(estadoAtual == 'q0' and i == 'c'):
        estado = 'q35'
    elif(estadoAtual == 'q35' and i == 'h'):
        estado = 'q36'
    elif(estadoAtual == 'q36' and i == 'a'):
        estado = 'q37'
    elif(estadoAtual == 'q37' and i == 'r'):
        estado = 'q38'
    
        
        
    elif(estadoAtual == 'q0' and i == 'a'):
        estado = 'q55'
    elif(estadoAtual == 'q55' and i == 'r'):
        estado = 'q56'
    elif(estadoAtual == 'q56' and i == 'r'):
        estado = 'q57'
    elif(estadoAtual == 'q57' and i == 'a'):
        estado = 'q58'
    elif(estadoAtual == 'q58' and i == 'y'):
        estado = 'q59'
        
        
        
    elif(estadoAtual == 'q0' and i == 'v'):
        estado = 'q52'
    elif(estadoAtual == 'q52' and i == 'a'):
        estado = 'q53'
    elif(estadoAtual == 'q53' and i == 'r'):
        estado = 'q54'
        
        
        
    elif(estadoAtual == 'q0' and i == 'i'):
        estado = 'q62'
    elif(estadoAtual == 'q62' and i == 'f'):
        estado = 'q63'
    elif(estadoAtual == 'q62' and i == 'n'):
        estado = 'q64'    
    elif(estadoAtual == 'q64' and i == 't'):
        estado = 'q65'
    elif(estadoAtual == 'q65' and i == 'e'):
        estado = 'q66'
    elif(estadoAtual == 'q66' and i == 'g'):
        estado = 'q67'
    elif(estadoAtual == 'q67' and i == 'e'):
        estado = 'q68'
    elif(estadoAtual == 'q68' and i == 'r'):
        estado = 'q69'  
        
        
    elif(estadoAtual == 'q0' and i == 'f'):
        estado = 'q73'
    elif(estadoAtual == 'q73' and i == 'u'):
        estado = 'q74'
    elif(estadoAtual == 'q74' and i == 'n'):
        estado = 'q75'
    elif(estadoAtual == 'q75' and i == 'c'):
        estado = 'q76'
    elif(estadoAtual == 'q76' and i == 't'):
        estado = 'q77'
    elif(estadoAtual == 'q77' and i == 'i'):
        estado = 'q78'
    elif(estadoAtual == 'q78' and i == 'o'):
        estado = 'q79'
    elif(estadoAtual == 'q79' and i == 'n'):
        estado = 'q80'
        
        
    elif(estadoAtual == 'q0' and i == 'r'):
        estado = 'q81'
    elif(estadoAtual == 'q81' and i == 'e'):
        estado = 'q82'
    elif(estadoAtual == 'q82' and i == 'a'):
        estado = 'q83'
    elif(estadoAtual == 'q83' and i == 'd'):
        estado = 'q84' 
        
    
    else:
        estado = 'q100'
    print("LETRA.: %s  | ESTADO.: %s"%(i,estadoAtual))                       
    return estado
    
dadosGlobais = lendoArquivo() 
maquinaEstados(dadosGlobais)
print('**************\nTABELA DE PALAVRAS RESERVADAS\n**************\n%s\n\n'%(tabela_reservadas))
print('**************\nTABELA DE PALAVRAS IDENTIFICADORAS\n**************\n%s\n\n'%(tabela_ids))
