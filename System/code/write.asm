section .text
global _start
_start:
    mov rax, 0x0a6f6c6c6568
    push rax
    mov rsi, rsp
    push 1
    pop rdi
    push 0x6
    pop rdx
    push 1
    pop rax
    syscall