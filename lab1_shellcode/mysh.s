section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor  eax, eax

      ; Construct "cccc=1234" to edx
      push  eax
      mov   ebx, "4aaa"
      shl   ebx, 24
      shr   ebx, 24
      push  ebx
      push  "=123"
      push  "cccc"
      mov   edx, esp
      
      ; Construct "bbb=5678" to ecx
      push  eax
      push  "5678"
      push  "bbb="
      mov   ecx, esp
      
      ; Construct "aaa=1234" to ebx
      push  eax
      push  "1234"
      push  "aaa="
      mov   ebx, esp
      
      ; Construct the environment array env[]
      push  eax
      push  edx
      push  ecx
      push  ebx
      mov   edx, esp

      ; Construct "/bin/sh"
      push eax          ; Use 0 to terminate the string
      push "/env"
      push "/bin"
      push "/usr"
      mov  ebx, esp     ; Get the string address

      ; Construct the argument array argv[]
      push eax
      push ebx          ; argv[0] points "/usr/bin/env"
      mov  ecx, esp     ; Get the address of argv[]

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
