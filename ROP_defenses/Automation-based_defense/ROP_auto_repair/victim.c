#include <stdio.h>
int main(){
	char buf[64];
	char tmp[32];
	printf("buffer address = %p\n", buf);
	fgets(buf,128,stdin);
	strcpy(buf,tmp);
	return 0;
}

