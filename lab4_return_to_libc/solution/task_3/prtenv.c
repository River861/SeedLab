#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
   char* shell = getenv("MYSHELL");
   if (shell)
       printf("%x\n", (unsigned int)shell);
   return 1;
}
