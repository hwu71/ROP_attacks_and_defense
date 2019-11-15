all: victim

victim: victim.c
	gcc -fno-stack-protector -o victim victim.c

gfree: victim.c 
	clang-gfree -fno-stack-protector -o victim_gfree victim.c
clean: 
	rm -f .o victim victim_gfree