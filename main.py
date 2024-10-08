from gerdau.elements import Plate, Conector, Beam
from gerdau.connection import EndPLate

chapa = Plate(t_ch=6.3,
              c= 200,
              f_uc=400,
              f_yc=250)

parafuso = Conector(d_b=15.875,
                    f_ub=825)

viga = Beam(name='W150x13',
            tw=4.3,
            tf=4.3,
            h=138,
            fy=345,
            fu=400)

conexao = EndPLate(Conector=parafuso,
                   Plate=chapa,
                   Viga=viga,
                   n_ps=4,
                   s=60,
                   g_ch=120)


block = conexao.blockShear()

Vrd = conexao.plateShear()

Mpl = conexao.plateBearing()

F = conexao.plateCrush()

F_vRd = conexao.boltShear()

web = conexao.beamWebShear()

intera = conexao.dunkerStability(97)
print(f'''
      Cisalhamento na placa: {Vrd}
      Cisalhamento na alma: {web}
      Cisalhamento no conjunto de parafusos: {F_vRd}
      Pressão de contato: {F}
      Normal na placa: {Mpl}
      Block Shear: {block}
      ''')

conexao.platePlot()