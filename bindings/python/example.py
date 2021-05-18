from unicorn import *
from unicorn.arm_const import *
from udbserver import udbserver

ADDRESS = 0x1000
ARM_CODE = b"\x17\x00\x40\xe2" # sub r0, #23

mu = Uc(UC_ARCH_ARM, UC_MODE_ARM)
mu.mem_map(ADDRESS, 0x400)
mu.mem_write(ADDRESS, ARM_CODE)
mu.reg_write(UC_ARM_REG_PC, ADDRESS)
udbserver(mu)
