void __attribute__((cdecl)) callee(int a1, int a2){ // cdecl로 호출
}
void caller(){
   callee(1, 2);
}