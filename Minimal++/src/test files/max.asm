j L107
L100:
sw $ra,($sp)
L101:
lw $t1,-12($sp)
lw $t2,-16($sp)
bgt $t1,$t2,L103
L102:
b L105
L103:
lw $t1,-12($sp)
lw $t0,-8($sp)
sw $t1,($t0)
L104:
b L106
L105:
lw $t1,-16($sp)
lw $t0,-8($sp)
sw $t1,($t0)
L106:
lw $ra,($sp)
jr $ra
L107:
addi $sp,$sp,52
move $s0,$sp
L108:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L109:
li $v0,5
syscall
move $t1,$v0
sw $t1,-16($s0)
L110:
addi $fp,$sp,20
lw $t0,-12($s0)
sw $t0,-12($fp)
L111:
lw $t0,-16($s0)
sw $t0,-16($fp)
L112:
addi $t0,$sp,-40
sw $t0,-8($fp)
L113:
sw $sp,-4($fp)
addi $sp,$sp,20
jal L100
addi $sp,$sp,-20
L114:
lw $t1,-40($s0)
sw $t1,-32($s0)
L115:
li $v0,5
syscall
move $t1,$v0
sw $t1,-20($s0)
L116:
li $v0,5
syscall
move $t1,$v0
sw $t1,-24($s0)
L117:
addi $fp,$sp,20
lw $t0,-20($s0)
sw $t0,-12($fp)
L118:
lw $t0,-24($s0)
sw $t0,-16($fp)
L119:
addi $t0,$sp,-44
sw $t0,-8($fp)
L120:
sw $sp,-4($fp)
addi $sp,$sp,20
jal L100
addi $sp,$sp,-20
L121:
lw $t1,-44($s0)
sw $t1,-36($s0)
L122:
addi $fp,$sp,20
lw $t0,-32($s0)
sw $t0,-12($fp)
L123:
lw $t0,-36($s0)
sw $t0,-16($fp)
L124:
addi $t0,$sp,-48
sw $t0,-8($fp)
L125:
sw $sp,-4($fp)
addi $sp,$sp,20
jal L100
addi $sp,$sp,-20
L126:
lw $t1,-48($s0)
sw $t1,-28($s0)
L127:
lw $t1,-28($s0)
li $v0,1
move $a0,$t1
syscall
L128:
li $v0,10
syscall
