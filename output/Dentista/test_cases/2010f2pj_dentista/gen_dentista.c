#include <stdio.h>
#include <stdlib.h>
#include <time.h>

main(int argc, char *argv[])
{
  int maxN, maxT, n, x, y;
  char maxAleatorio;
  
  if (argc != 4) {
    printf("Uso: %s MaxN MaxT A\nMaxN -> maior valor possível para o número de consultas\nMaxT -> Maior valor possível para o tempo de final das consultas\nA -> S/N para número máximo aleatório ou não.\n", argv[0]);
    exit(1);
  }

  srand(time(NULL));
  
  sscanf(argv[1], "%d", &maxN);
  sscanf(argv[2], "%d", &maxT);
  maxAleatorio = argv[3][0];

  if (maxAleatorio == 'N')
    n = maxN;
  else
    n = rand() % maxN + 1;

  printf("%d\n", n);
  
  x = 0;
  while (n > 0) {
    if (rand() % (maxT - x) <= n) {
      y = rand() % ((maxT - x) / (maxT / 100) + 1) + x + 1;
      printf("%d %d\n", x + 1, y + 1);
      n --;
    }
    x ++;
  }  
}
