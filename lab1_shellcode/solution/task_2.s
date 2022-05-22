section .text
  global _start
    _start:
	BITS 32
	jmp short two
    one:
 	pop ebx                ; ebx points "/usr/bin/env*a=11*b=22*AAAABBBBCCCCDDDDEEEE"
 	xor eax, eax           ; eax = 0
 	
 	; Change * to 0
 	mov [ebx+12], al
 	mov [ebx+17], al
 	mov [ebx+22], al
 	
 	; Save "/usr/bin/env" addr to AAAA and "\0" to BBBB
 	mov [ebx+23], ebx
 	mov [ebx+27], eax
 	
 	; Save "a=11" addr to CCCC, "b=22" addr to DDDD and "\0" to EEEE
 	lea ecx, [ebx+13]
 	mov [ebx+31], ecx
 	lea ecx, [ebx+18]
 	mov [ebx+35], ecx
 	mov [ebx+39], eax
 	
 	lea ecx, [ebx+23]      ; ecx: points array argv[]
 	lea edx, [ebx+31]      ; edx: points array env[] 
 	
 	mov al,  0x0b          ; exec
 	int 0x80
     two:
 	call one
 	db '/usr/bin/env*a=11*b=22*AAAABBBBCCCCDDDDEEEE' 
