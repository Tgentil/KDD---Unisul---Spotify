# Projeto de Limpeza de Dados do Spotify

[![GitHub](https://img.shields.io/badge/Visit-My%20Profile-0891B2?style=flat-square&logo=github)](https://github.com/Tgentil)

Este projeto faz parte da matéria de Análise de Dados e Big Data, ministrada pelo Professor Jorge Werner.

## Objetivo do Projeto

O objetivo deste projeto é realizar a limpeza de dados de um conjunto de músicas do Spotify, preparando-os para análise posterior. Os dados foram limpos através da minha interpretação de cada variável na Documentação da API do Spotify, conforme documentação disponível [aqui](https://developer.spotify.com/documentation/web-api/reference/get-audio-features).

## Bibliotecas Necessárias

Para executar o projeto, é necessário ter o Python instalado juntamente com as seguintes bibliotecas:

- pandas

Você pode instalar as dependências utilizando o comando:

```bash
pip install -r requirements.txt
```

## Executando o Projeto

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de que as dependências estão instaladas.
3. Execute o script `script.py` no terminal.

Certifique-se de que o arquivo CSV de entrada esteja no diretório `data/` e o arquivo Excel de saída será gerado no diretório `out/`.

## Estrutura do Repositório

```bash
+--./
|-- script.py
| +--data/
| |-- spotify1_20240415200237.csv
| +--docs/
| |-- 02BigDatalimpezadedados_20240408211508.pdf
| |-- spotify1_20240415200237.csv
| +--out/
| |-- cleaned_spotify_data.xlsx
```

Este projeto foi desenvolvido como parte do aprendizado na disciplina de Análise de Dados e Big Data. Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato!

## Autor do Projeto

- Thiago Gentil
