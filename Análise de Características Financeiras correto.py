{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c29252c3",
   "metadata": {},
   "source": [
    "# Análise de Características Financeiras com Python\n",
    "Alunos Responsáveis: Kauã Ericklis Rodrigues, Gabriel Ortolan, Natali Eliza Rodrigues, Guilheme Finsterbusch Aniba e Lucas de Rezende\n",
    "\n",
    "Este notebook realiza a análise das colunas financeiras do dataset `default_of_credit_card_clients__courseware_version_1_21_19.xls` como parte da atividade prática."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b11be25e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f28aeb6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "file_path = 'default_of_credit_card_clients__courseware_version_1_21_19.xls'\n",
    "df = pd.read_excel(file_path, header=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f165f4e",
   "metadata": {},
   "source": [
    "## Exercício 1: Criação de listas com nomes das características financeiras"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e345eaf",
   "metadata": {},
   "outputs": [],
   "source": [
    "bill_features = ['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']\n",
    "pay_features = ['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e00e0e6a",
   "metadata": {},
   "source": [
    "## Exercício 2: Síntese estatística das características de valor da fatura"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c0b6d3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[bill_features].describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee54ab2a",
   "metadata": {},
   "source": [
    "## Exercício 3: Histogramas das características de valor da fatura"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79ea0106",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(15, 10))\n",
    "for i, feature in enumerate(bill_features):\n",
    "    plt.subplot(2, 3, i + 1)\n",
    "    plt.hist(df[feature], bins=20, color='skyblue')\n",
    "    plt.title(f'Histograma de {feature}')\n",
    "    plt.xlabel('Valor da Fatura')\n",
    "    plt.ylabel('Frequência')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91cc3756",
   "metadata": {},
   "source": [
    "## Exercício 4: .describe() das características de valor do pagamento"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2a2be89",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[pay_features].describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5964586",
   "metadata": {},
   "source": [
    "## Exercício 5: Histograma das características de pagamento com rotação no eixo x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef35244b",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(15, 10))\n",
    "for i, feature in enumerate(pay_features):\n",
    "    plt.subplot(2, 3, i + 1)\n",
    "    plt.hist(df[feature], bins=20, color='salmon')\n",
    "    plt.title(f'Histograma de {feature}')\n",
    "    plt.xlabel('Valor do Pagamento')\n",
    "    plt.ylabel('Frequência')\n",
    "    plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "613e44a5",
   "metadata": {},
   "source": [
    "## Exercício 6: Contagem de pagamentos iguais a zero"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5b611d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "zero_mask = df[pay_features] == 0\n",
    "zero_counts = zero_mask.sum()\n",
    "print(\"Pagamentos iguais a zero:\")\n",
    "print(zero_counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "339f8fb6",
   "metadata": {},
   "source": [
    "## Exercício 7: Histogramas logarítmicos de pagamentos diferentes de zero"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ade0d44",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_non_zero = df[pay_features].replace(0, np.nan)\n",
    "log_transformed = df_non_zero.apply(np.log10)\n",
    "\n",
    "plt.figure(figsize=(12, 8))\n",
    "for i, feature in enumerate(pay_features):\n",
    "    plt.subplot(2, 3, i + 1)\n",
    "    plt.hist(log_transformed[feature].dropna(), bins=20, color='gray')\n",
    "    plt.title(f'{feature}')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}