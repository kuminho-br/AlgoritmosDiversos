/*
FUN��ES A SEREM IMPLEMENTADAS:
    - INICIALIZAR A ESTRUTURA:
        PENSAR NOS VALORES ADEQUADOS PARA CADA UM DOS CAMPOS DA ESTRUTURA
    - RETORNAR A QUANTIDADE DE ELEMENTOS V�LIDOS
    - EXIBIR OS ELEMENTOS DA ESTRUTURA
    - BUSCAR POR UM ELEMENTO NA ESTRUTURA
    - INSERIR ELEMENTOS NA ESTRUTURA
    - EXCLUIR ELEMENTOS DA ESTRUTURA
    - REINICIALIZAR A ESTRUTURA
*/

#define MAX 50 //ESPECIFICA O TAMANHO PREDEFINIDO DO ARRANJO

typedef int ID; //NOMEIA O TIPO int COMO ID

typedef struct{ //CRIA UM TIPO DE TUPLA PARA ARMAZENAR INFORMA��ES QUAISQUER
    ID chave;  // NO EX, FOI INSERIDO APENAS O CAMPO CHAVE PARA TESTES
} registro;

typedef struct { //CRIA UM TIPO DE  ESTRUTURA CHAMADA lista QUE CONT�M UMA LISTA
    registro a[MAX]; //DE REGISTROS  COM ESPA�O PARA ARMAZENAR 50 REGISTROS,
    int nElem;  //E UMA VARI�VEL PARA REGISTROS O N DE ELEMENTOS Q DA LISTA
} lista;

void inicializarLista(lista* l){//DEFINE UMA FUN��O QUE RECEBE UM PONTEIRO PARA
    l->nElem = 0; //UM TIPO lista E FAZ COM QUE O CAMPO nElem SEJA ZERO, PARA
} // INICIALIZAR A lista

int retornarTamanho(lista* l){ //DEFINE UMA FUN��O QUE RETORNA O N�MERO DE
    return l->nElem; // ELEMENTOS ARMAZENADOS NA LISTA LINEAR SEQUENCIAL
}

void exibirLista(lista* l){
    int i;
    pr  intf("Lista: \" ");
    for (i = 0; i < l->nElem; i++){
        printf("%i",l->a[i].chave);
    }
    printf("\"\n");
}

int buscaSequencial(lista* l, chave ch){
    int i = 0;
    while (i < l->nElem){
        if (ch == l->a[i].chave) return i;
        else i++;
    }
}

int main(int argc, char *argv[])
{
  printf("Press enter to continue ...");
  getchar();
  return 0;

}
