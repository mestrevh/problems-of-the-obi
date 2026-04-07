#include <stdio.h>
#include <stdlib.h>
#include <time.h>

main(int argc, char *argv[])
{
  int max, n, k;
  
  if (argc != 2) {
    printf("Uso: %s Max\nMax -> maior valor possível para o número aleatório\n", argv[0]);
    exit(1);
  }

  srand(time(NULL));
  
  sscanf(argv[1], "%d", &max);

  n = rand() % max + 1;
  k = rand() % n + 1;

  printf("%d %d\n", n, k);
}
