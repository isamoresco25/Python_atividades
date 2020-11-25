{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "exercício02.py",
      "provenance": [],
      "authorship_tag": "ABX9TyO0NSG9v0doeTrFGzK/4fmy"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "QvW_biEkAlmr"
      },
      "source": [
        "# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. \n",
        "# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, \n",
        "# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.\n",
        "\n",
        "#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:\n",
        "#     comprar apenas latas de 18 litros;\n",
        "#     comprar apenas galões de 3,6 litros;\n",
        "#     misturar latas e galões, de forma que o desperdício de tinta seja menor. \n",
        "#     Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.\n",
        "\n",
        "import math \n",
        "\n",
        "area = float(input('Digite a area em metros quadrados que deseja pintar: '))\n",
        "\n",
        "litro_tinta = math.ceil(area/6)\n",
        "\n",
        "tinta_mais_folga = (litro_tinta*0.1) + litro_tinta\n",
        "\n",
        "qtd_lata = math.ceil(litro_tinta/18)\n",
        "\n",
        "qtd_galao = math.ceil(litro_tinta/3.6)\n",
        "\n",
        "litro = area/6\n",
        "lata = int(litro/18)\n",
        "galao = math.ceil((litro_tinta%18)/3.6)\n",
        "\n",
        "\n",
        "print(f'''\n",
        "Quantidade de tinta: {math.ceil(tinta_mais_folga)} litros\n",
        "\n",
        "Opção 1) Quantidade: {qtd_lata} latas.\n",
        "         Total: {qtd_lata*80} reais\n",
        "Opção 2) Quantidade: {qtd_galao} galões\n",
        "         Total: {qtd_galao*25} reais\n",
        "Opção 3) Quantidade: {lata} latas e {galao} galões\n",
        "         Total: {lata*80 + galao*25} reais\n",
        "''')"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}