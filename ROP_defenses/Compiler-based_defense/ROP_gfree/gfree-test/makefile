all: gfree gcc
gfree: test.c
	clang-gfree -fno-stack-protector -O0 -o test_gfree test.c
gcc: test.c
	gcc -fno-stack-protector -O0 -o test_gcc test.c
disa: test_gfree test_gcc
	objdump -d test_gfree > test_gfree.disa
	objdump -d test_gcc > test_gcc.disa
clean:
	rm -f .o test_gcc test_gfree