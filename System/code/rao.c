#include <stdio.h>
#include <unistd.h>

void get_shell() { // 0x00000000004005a7
  char *cmd = "/bin/sh";
  char *args[] = {cmd, NULL};

  execve(cmd, args, NULL);
}

int main() {
  char buf[0x28]; // 40bytes

  printf("Input: ");
  scanf("%s", buf);

  return 0;
}