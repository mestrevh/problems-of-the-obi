#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE * sol_aluno;

#define MAX_VERTICES 110

int soma_adjs[MAX_VERTICES];

struct
{
  int vert;
  int nivel;
} fila[MAX_VERTICES];

int ifila, ffila;
int grau[MAX_VERTICES];

void erro(char * msg)
{
  fprintf(stderr,"%s\n",msg);
  exit(1);
}

main(int argc, char * argv[])
{
  int caso=1, caso_aluno;
  char linha_aluno[10000];
  int n, x, y, v, nivel, centro_1, centro_2, centro_aluno;

  sol_aluno = fopen(argv[1],"rt");
  freopen(argv[2], "rt", stdin);

  while (scanf("%d",&n) == 1 && n > 0)
  {
    memset(soma_adjs,0,sizeof(soma_adjs));
    memset(grau,0,sizeof(grau));
    for (v=0; v < n-1; v++)
    {
      scanf("%d %d",&x,&y);
      x--; y--;
      soma_adjs[x] += y;
      soma_adjs[y] += x;
      grau[x]++;
      grau[y]++;
    }
    if (n == 1)
      centro_1 = centro_2 = 1;
    else
    {  
      ifila = ffila = 0;
      for (v=0; v < n; v++)
        if (grau[v] == 1)
        {
          fila[ffila].vert = v;
          fila[ffila].nivel = 0;
          ffila++;
        }
      while (ffila < n)
      {
        v = fila[ifila].vert;
        nivel = fila[ifila].nivel;
        grau[soma_adjs[v]]--;
        soma_adjs[soma_adjs[v]] -= v;
        if (grau[soma_adjs[v]] == 1)
        {
          fila[ffila].vert = soma_adjs[v];
          fila[ffila].nivel = nivel+1;
          ffila++;
        }
        grau[v] = 0;
        ifila++;
      }
      centro_1 = fila[n-1].vert+1;
      if (fila[n-2].nivel == fila[n-1].nivel)
        centro_2 = fila[n-2].vert+1;
      else
        centro_2 = centro_1;
    }
// printf("CENTRO_1 = %d    CENTRO_2 = %d\n",centro_1,centro_2); 
    /* Testa Solucao do Aluno */


    if ((fscanf(sol_aluno,"%s",linha_aluno) != 1) ||
        (strcmp(linha_aluno,"Teste")))
      erro("Palavra 'Teste' nao encontrada");
    if ((fscanf(sol_aluno,"%d",&caso_aluno) != 1) || (caso_aluno != caso++))
      erro("Nro do teste incorreto");
    fscanf(sol_aluno,"%d",&centro_aluno);
    if (centro_aluno != centro_1 && centro_aluno != centro_2)
      erro("Resposta errada!");
  }
  /* if (fscanf(sol_aluno," %c",lixo) != EOF) */
  /*  erro("Lixo no final do arquivo"); */
  fclose(sol_aluno);
  return 0;
}
