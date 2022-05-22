section .text
  global _start
    _start:
      ; The following code calls execve("/bin/sh", ...)
      xor  rsi, rsi        ; 2nd argument
      xor  rdx, rdx       ; 3rd argument
      push rdx
      
      ; Construct "/bin/bash"
      mov  rax,'haaaaaaa'
      shl  rax, 56
      shr  rax, 56
      push rax
      mov  rax, '/bin/bas'
      push rax

      mov  rdi, rsp        ; 1st argument
      
      ; push rdx 
      ; push rdi
      ; mov  rsi, rsp

      xor  rax, rax
      mov  al, 0x3b        ; execve()
      syscall
