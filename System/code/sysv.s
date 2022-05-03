	.file	"sysv.c"
	.intel_syntax noprefix
	.text
	.globl	callee
	.type	callee, @function
callee:
	push	ebx
	sub	esp, 24
	mov	eax, DWORD PTR [esp+32]
	mov	DWORD PTR [esp], eax
	mov	eax, DWORD PTR [esp+36]
	mov	DWORD PTR [esp+4], eax
	mov	eax, DWORD PTR [esp+40]
	mov	ecx, eax
	mov	ebx, eax
	sar	ebx, 31
	mov	eax, DWORD PTR [esp]
	mov	edx, DWORD PTR [esp+4]
	add	ecx, eax
	adc	ebx, edx
	mov	eax, DWORD PTR [esp+44]
	cdq
	add	ecx, eax
	adc	ebx, edx
	mov	eax, DWORD PTR [esp+48]
	cdq
	add	ecx, eax
	adc	ebx, edx
	mov	eax, DWORD PTR [esp+52]
	cdq
	add	ecx, eax
	adc	ebx, edx
	mov	eax, DWORD PTR [esp+56]
	cdq
	add	ecx, eax
	adc	ebx, edx
	mov	eax, DWORD PTR [esp+60]
	cdq
	add	eax, ecx
	adc	edx, ebx
	mov	DWORD PTR [esp+16], eax
	mov	DWORD PTR [esp+20], edx
	mov	eax, DWORD PTR [esp+16]
	mov	edx, DWORD PTR [esp+20]
	add	esp, 24
	pop	ebx
	ret
	.size	callee, .-callee
	.globl	caller
	.type	caller, @function
caller:
	sub	esp, 4
	push	7
	push	6
	push	5
	push	4
	push	3
	push	2
	push	28744523
	push	-1395630315
	call	callee
	add	esp, 32
	nop
	add	esp, 4
	ret
	.size	caller, .-caller
	.globl	main
	.type	main, @function
main:
	lea	ecx, [esp+4]
	and	esp, -8
	push	DWORD PTR [ecx-4]
	push	ebp
	mov	ebp, esp
	push	ecx
	sub	esp, 4
	call	caller
	mov	eax, 0
	add	esp, 4
	pop	ecx
	pop	ebp
	lea	esp, [ecx-4]
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
