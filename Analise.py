import pandas as pd
import math
df = pd.read_excel("TABELA.xlsx")

Z = 1.96 # 95% de confiança

# 1 objetivo: Mostrar o intervalo de confiaça entre as mulheres das turmas A e B e sua proporção em cada grupo

# filtra por turma é sexo
QuantidadeF_TurmaA = df[(df['Turma'] == 'A') & (df['Sexo'] == 'F')].shape[0]
QuantidadeF_TurmaB = df[(df['Turma'] == 'B') & (df['Sexo'] == 'F')].shape[0]

# Obs: foi contada manualmente, apesar que poderia ser feito de um jeito mais eficiente 
Numero_De_vagas_casoA = 20

# a media aritmética 
ProporcaoFemininaA = QuantidadeF_TurmaA/Numero_De_vagas_casoA
ProporcaoFemininaB = QuantidadeF_TurmaB/Numero_De_vagas_casoA

Diferenca_De_ProporcoesA = abs(ProporcaoFemininaA - ProporcaoFemininaB)

ErroPadrao = math.sqrt(((ProporcaoFemininaA*(1 - ProporcaoFemininaA))/Numero_De_vagas_casoA) + ((ProporcaoFemininaB*(1- ProporcaoFemininaB))/Numero_De_vagas_casoA))

# Obs: isso é mais ou menos dois resultados
Intervalo_De_Confianca_Mais = Diferenca_De_ProporcoesA + Z * ErroPadrao
Intervalo_De_Confianca_Menos = Diferenca_De_ProporcoesA - Z * ErroPadrao



print('=-=-'*25)
print("[1ª] INTERVALO DE CONFIANÇA")
print("objetivo: Mostrar o intervalo de confiaça entre as mulheres das turmas A e B e sua proporção em cada grupo\n")
print("""
========= RESUMO DAS FÓRMULAS =========

1) Proporção amostral:
p̂ = x / n
(x = número de mulheres, n = total da turma)

2) Diferença entre proporções:
D = | p̂A - p̂B |

3) Erro padrão:
EP = √ [ (p̂A(1-p̂A)/nA) + (p̂B(1-p̂B)/nB) ]

4) Intervalo de confiança (95%):
IC = D ± 1.96 * EP

Se o IC contém 0 → não há diferença significativa.
Se não contém 0 → há diferença estatística.
=======================================
""")
print(f'O intervalo de confiança é +- : IC = ([{Intervalo_De_Confianca_Menos:.3f}][{Intervalo_De_Confianca_Mais:.3f}])')
print(f'A amostra do grupo era de {QuantidadeF_TurmaA + QuantidadeF_TurmaB} Alunos')
print(f'Na turma A {ProporcaoFemininaA:.2%} são mulheres, já na turma B há um total de {ProporcaoFemininaB:.2%}, é uma diferença de {Diferenca_De_ProporcoesA:.2%}')

print('=-=-'*25)


# 2 Objetivo: Teste de hipótese para proporção de variáveis categóricas: No exemplo entre estudantes do curso de Fisíca e computação além de sua proporção amostral

# H0: Pa != Pb
# H1: Pa = Pb

Estudantes_de_fisica = df[(df['Curso'] == 'FIS')].shape[0]
Estudantes_de_Computacao = df[(df['Curso'] == 'COMP')].shape[0]

# OBs: Deixei como caso B para manter um padrão 
Numero_De_vagas_casoB = 19

# Médias e proporções
Proporcao_estudComp = Estudantes_de_Computacao / Numero_De_vagas_casoB
Proporcao_estudFis = Estudantes_de_fisica / Numero_De_vagas_casoB
Diferenca_De_ProporcoesB = abs(Proporcao_estudComp - Proporcao_estudFis)

Pa = Estudantes_de_Computacao / Numero_De_vagas_casoB
Pb = Estudantes_de_fisica / Numero_De_vagas_casoB

# Obs: Fiz a soma em vez de * 2, para facilitar caso eu mude de tabela.
Proporcao_combinada = (Estudantes_de_Computacao + Estudantes_de_fisica) / ( Numero_De_vagas_casoB + Numero_De_vagas_casoB )

ErroPadrao = math.sqrt((Proporcao_combinada * (1 - Proporcao_combinada)) * (1/Numero_De_vagas_casoB  +  1/Numero_De_vagas_casoB))

Estatistica_De_TestZ = (Pa - Pb )/ ErroPadrao

print("[2ª] INTERVALO DE CONFIANÇA")
print("Objetivo: Teste de hipótese para proporção de variáveis categóricas: No exemplo entre estudantes do curso de Fisíca e computação além de sua proporção amostral\n")
print("""
========= RESUMO DAS FÓRMULAS (Teste Z - Duas Proporções) =========

1) Proporções amostrais:
Pa = xA / nA
Pb = xB / nB

2) Proporção combinada (pooled):
p̂ = (xA + xB) / (nA + nB)

3) Erro padrão:
EP = √ [ p̂(1 - p̂) * (1/nA + 1/nB) ]

4) Estatística do teste Z:
Z = (Pa - Pb) / EP

Decisão (95% confiança):
Se -1.96 < Z < 1.96 → não rejeita H0
Se Z ≤ -1.96 ou Z ≥ 1.96 → rejeita H0

H0: Pa = Pb
H1: Pa ≠ Pb
=============================================================
""")
print(f"Número total da amostra {Numero_De_vagas_casoB}")
print(f"{Proporcao_estudComp:.2%} são estudantes de computação é {Proporcao_estudFis:.2%} são estudantes de física, uma diferença de {Diferenca_De_ProporcoesB:.2%}")
print(f"O desvio padrão é de {ErroPadrao:.3f} ,o testeZ mostra uma média de +- {Estatistica_De_TestZ:.3f}")

if Estatistica_De_TestZ > -Z and Estatistica_De_TestZ < Z:

    print(f'{Z} > {Estatistica_De_TestZ:.3f} > {-Z} : ele está dentro da região normal, H0 não esta rejeitado\n')

else:

    if Estatistica_De_TestZ > Z:
        print(f'{Estatistica_De_TestZ:.3f} > {Z} : ele está fora da região normal, H0 rejeitada')

    else:
        print(f'{Estatistica_De_TestZ:.3f} < {Z} : ele está fora da região normal, H0 rejeitada')
         

# 3 Teste de hipótese para média de variáveis numéricas; usando as notas no pessoasl de Computação

T = 2.064 # < esse é o gral de confiança caso seja 95%

# Obs: Z quando a variabilidade ou a populção é conhecida e T se não.

Media_Hipotetica_U = 5 

#
n = math.sqrt(Estudantes_de_Computacao) 

# a média vai ser 5
#H0: U = 5
#H1: U != 5

MediaAmostral_das_notasDeCalcA_COMP = df.loc[df['Curso'] == 'COMP', 'CalcA'].sum() / Estudantes_de_Computacao
Tamanho_Da_Amostra = df[df['Curso'] == 'COMP'].shape[0]


NotaMax = df.loc[df['Curso'] == 'COMP', 'CalcA'].max()
NotaMin = df.loc[df['Curso'] == 'COMP', 'CalcA'].min()
Diferenca_Notas = NotaMax - NotaMin

# Lembrete: O stf(ddof) existe kkk
DesvioPadrao = df['CalcA'].std(ddof=0)

Estatistica_TestT = (MediaAmostral_das_notasDeCalcA_COMP - Media_Hipotetica_U) / (DesvioPadrao / n)

print('=-=-'*25)
print("[3ª] Teste de hipótese para média de variáveis numéricas")
print("Objetivo: Fazer uma media amostral das notas dos alunos de computação na Materia de CalculoA, além da sua maior é menor nota\n")
print("""
========= RESUMO DAS FÓRMULAS (Teste t - Uma Média) =========

1) Média amostral:
x̄ = Σx / n

2) Desvio padrão amostral:
s = √ [ Σ(x - x̄)² / (n - 1) ]

3) Erro padrão da média:
EP = s / √n

4) Estatística t:
t = (x̄ - μ0) / EP

Onde:
μ0 = média hipotética
n  = tamanho da amostra

Decisão (95% confiança):
Se -T < t < T → não rejeita H0
Se t ≤ -T ou t ≥ T → rejeita H0

H0: μ = μ0
H1: μ ≠ μ0
==============================================================
""")
print(f"O tamanho da amostra é {Tamanho_Da_Amostra}")
print(f"A média amostral é de {MediaAmostral_das_notasDeCalcA_COMP:.2f}, sua nota Max é {NotaMax:.2f} já sua Min é {NotaMin:.2f}, uma diferença de {Diferenca_Notas:.2f}")
print(f"Tem um desvio padrão de {DesvioPadrao:.3f} o test T revela uma média de +- {Estatistica_TestT:.3f}")

if Estatistica_TestT > -T and Estatistica_TestT < T:

    print(f'{T} > {Estatistica_TestT:.3f} > {-T} : ele está dentro da região normal, H0 não esta rejeitado\n')

else:

    if Estatistica_TestT > T:
        print(f'{Estatistica_TestT:.3f} > {T} : ele está fora da região normal, H0 rejeitada')

    else:
        print(f'{Estatistica_TestT:.3f} < {T} : ele está fora da região normal, H0 rejeitada')
               