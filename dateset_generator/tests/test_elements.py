from generator.elements import Column, Conector, Beam, Plate, CornerFrame
import pint

def test_column():
    '''
    Teste da classe: valores de entrada, recebimento e devolução
    '''
    # Entradas
    entrada = {'name':1,
               'tf':1,
               'h':1}
    
    coluna = Column(name=entrada['name'],
                    tf=entrada['tf'],
                    h=entrada['h'],
                    )
    
    # Obtendo os parâmetros da classe
    saida = coluna.__dict__
    
    # Varificação das entradas
    for chave in entrada.keys():
        if isinstance(saida[chave],pint.Quantity):
            value = saida[chave].magnitude
        
        else:
            value = saida[chave]
        
        assert value == entrada[chave], 'Valores de entrada errada'
            

def test_conector():
    '''
    Teste da classe: valores de entrada, recebimento e devolução
    '''
    # Entradas
    entrada = {'d_b':1,
               'f_ub':1}
    
    conect = Conector(d_b=entrada['d_b'],
                    f_ub=entrada['f_ub'],
                    )
    
    # Obtendo os parâmetros da classe
    saida = conect.__dict__
    
    # Varificação das entradas
    for chave in entrada.keys():
        if isinstance(saida[chave],pint.Quantity):
            value = saida[chave].magnitude
        
        else:
            value = saida[chave]
        
        assert value == entrada[chave], 'Valores de entrada errada'


def test_plate():
    '''
    Teste da classe: valores de entrada, recebimento e devolução
    '''
    # Entradas
    entrada = {'t_ch':6.35,
               'f_uc':1,
               'f_yc':1,
               'c':1}
    
    chapa = Plate(name='CH 1/4"',
                  f_uc=entrada['f_uc'],
                  f_yc=entrada['f_yc'],
                  c=entrada['c'],
                    )
    
    # Obtendo os parâmetros da classe
    saida = chapa.__dict__

    # Varificação das entradas
    for chave in entrada.keys():
        if isinstance(saida[chave],pint.Quantity):
            value = saida[chave].magnitude
        
        else:
            value = saida[chave]
        
        assert value == entrada[chave], 'Valores de entrada errada'
    

def test_beam():
    '''
    Teste da classe: valores de entrada, recebimento e devolução
    '''
    # Entradas
    entrada = {'name':1,
               'h':1,
               'tw':1,
               'tf':1,
               'fy':1,
               'fu':1}
    
    viga = Beam(name=entrada['name'],
                  h=entrada['h'],
                  tf=entrada['tf'],
                  tw=entrada['tw'],
                  fy=entrada['fy'],
                  fu=entrada['fu'],
                    )
    
    # Obtendo os parâmetros da classe
    saida = viga.__dict__
    
    # Varificação das entradas
    for chave in entrada.keys():
        if isinstance(saida[chave],pint.Quantity):
            value = saida[chave].magnitude
        
        else:
            value = saida[chave]
        
        assert value == entrada[chave], 'Valores de entrada errada'


def test_conerframe():
    '''
    Teste da classe: valores de entrada, recebimento e devolução
    '''
    # Entradas
    entrada = {'t_c':1,
               'fy':1,
               'lc':1,
               }
    
    cantoneira = CornerFrame(fy=entrada['fy'],
                       lc=entrada['lc'],
                       t_c=entrada['t_c']
                    )
    
    # Obtendo os parâmetros da classe
    saida = cantoneira.__dict__
    
    # Varificação das entradas
    for chave in entrada.keys():
        if isinstance(saida[chave],pint.Quantity):
            value = saida[chave].magnitude
        
        else:
            value = saida[chave]
        
        assert value == entrada[chave], 'Valores de entrada errada'
