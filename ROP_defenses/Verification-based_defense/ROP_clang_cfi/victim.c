#include <stdio.h>
int main(){
	char buf[64];
	printf("buffer address = %p\n", buf);
	gets(buf);
	return 0;
}

