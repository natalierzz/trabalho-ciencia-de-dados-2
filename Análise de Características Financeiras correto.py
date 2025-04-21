Análise de Características Financeiras com Python
Alunos Responsáveis: Kauã Ericklis Rodrigues, Gabriel Ortolan, Natali Eliza Rodrigues, Guilheme Finsterbusch Aniba e Lucas de Rezende

Este notebook realiza a análise das colunas financeiras do dataset default_of_credit_card_clients__courseware_version_1_21_19.xls como parte da atividade prática.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
     

file_path = 'default_of_credit_card_clients__courseware_version_1_21_19.xls'
df = pd.read_excel(file_path, header=1)
     
Exercício 1: Criação de listas com nomes das características financeiras

bill_features = ['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']
pay_features = ['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
     
Exercício 2: Síntese estatística das características de valor da fatura

df[bill_features].describe()
     
Exercício 3: Histogramas das características de valor da fatura

plt.figure(figsize=(15, 10))
for i, feature in enumerate(bill_features):
    plt.subplot(2, 3, i + 1)
    plt.hist(df[feature], bins=20, color='skyblue')
    plt.title(f'Histograma de {feature}')
    plt.xlabel('Valor da Fatura')
    plt.ylabel('Frequência')
plt.tight_layout()
plt.show()
     
Exercício 4: .describe() das características de valor do pagamento

df[pay_features].describe()
     
Exercício 5: Histograma das características de pagamento com rotação no eixo x

plt.figure(figsize=(15, 10))
for i, feature in enumerate(pay_features):
    plt.subplot(2, 3, i + 1)
    plt.hist(df[feature], bins=20, color='salmon')
    plt.title(f'Histograma de {feature}')
    plt.xlabel('Valor do Pagamento')
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
     
Exercício 6: Contagem de pagamentos iguais a zero

zero_mask = df[pay_features] == 0
zero_counts = zero_mask.sum()
print("Pagamentos iguais a zero:")
print(zero_counts)
     
Exercício 7: Histogramas logarítmicos de pagamentos diferentes de zero

df_non_zero = df[pay_features].replace(0, np.nan)
log_transformed = df_non_zero.apply(np.log10)

plt.figure(figsize=(12, 8))
for i, feature in enumerate(pay_features):
    plt.subplot(2, 3, i + 1)
    plt.hist(log_transformed[feature].dropna(), bins=20, color='gray')
    plt.title(f'{feature}')
plt.tight_layout()
plt.show()
