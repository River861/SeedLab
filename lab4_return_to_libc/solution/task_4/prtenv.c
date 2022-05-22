#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
   char* shell = getenv("MYSHELL");
   if (shell)
       printf("MYSHELL: %x\n", (unsigned int)shell);
   char* option = getenv("OPTION");
   if (option)
       printf("OPTION: %x\n", (unsigned int)option);
   return 1;
}
