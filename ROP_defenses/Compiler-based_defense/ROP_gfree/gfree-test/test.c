#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int func1(){
	int a = 0xc2;
	int b = 0xc3;
	int c = a + b - 0xc2;
	return c;
}

void func2(){
	char string[] = "\x5f\x5e\x5a\xc3";
}


int main(){
	func1();
	func2();
	return 0;
}