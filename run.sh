#!/bin/bash

# armazenando nossas colorescapes
RESET_ESCAPE='\e[0m'
ERROR_ESCAPE='\e[1;31m'
SUCES_ESCAPE='\e[1;32m'

# caminho do program principal
PROGRAM_PATH=./src/main.py

# se o arquivo citado anteriormente existe, printar sucesso e chamar arquivo
if [ -f "$PROGRAM_PATH" ]; then
  echo ;
  echo -e "Program file$SUCES_ESCAPE was found!$RESET_ESCAPE";
  echo -n "It will run in ";
  for i in {3..1}; do
    echo -n "$i ";
    sleep 1;
  done ;
  echo ;
  python $PROGRAM_PATH;
  exit 0; # retorna 0 (sem erros)

# caso contrário, printar erro e encerrar
else
  echo ;
  echo -e "Program file cannot be found! $ERROR_ESCAPE < $PROGRAM_PATH > $RESET_ESCAPE";
  echo ;
  exit 1; # retorna 1 (erro)
fi
