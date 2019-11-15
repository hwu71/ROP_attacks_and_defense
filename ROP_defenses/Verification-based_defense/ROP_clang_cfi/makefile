CC = clang-3.9
CFLAGS = -O0 -g -fvisibility=hidden -flto -fno-sanitize-trap=all


all: cfi_victim no_cfi_victim


cfi_victim: victim.c
	@echo Compiling $< to $@
	@$(CC) $(CFLAGS) -fsanitize=cfi -o $@ $<

no_cfi_victim: victim.c
	@echo Compiling $< to $@
	@$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f *.o no_cfi_victim cfi_victim

.PHONY: clean all
