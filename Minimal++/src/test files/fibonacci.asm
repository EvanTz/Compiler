j L117
L100:
sw $ra,($sp)
L101:
lw $t1,-12($s0)
li $t2,1
sub $t1,$t1,$t2
sw $t1,-28($sp)
L102:
lw $t1,-28($sp)
sw $t1,-12($s0)
L103:
lw $t1,-16($sp)
lw $t2,-20($sp)
add $t1,$t1,$t2
sw $t1,-32($sp)
L104:
lw $t1,-32($sp)
sw $t1,-24($sp)
L105:
lw $t1,-24($sp)
li $v0,1
move $a0,$t1
syscall
L106:
lw $t1,-12($s0)
li $t2,0
bgt $t1,$t2,L108
L107:
b L115
L108:
addi $fp,$sp,40
lw $t0,-12($s0)
sw $t0,-12($fp)
L109:
lw $t0,-20($sp)
sw $t0,-16($fp)
L110:
lw $t0,-24($sp)
sw $t0,-20($fp)
L111:
addi $t0,$sp,-36
sw $t0,-8($fp)
L112:
sw $sp,-4($fp)
addi $sp,$sp,40
jal L100
addi $sp,$sp,-40
L113:
lw $t1,-36($sp)
sw $t1,-24($sp)
L114:
b L116
L115:
li $t1,0
lw $t0,-8($sp)
sw $t1,($t0)
L116:
lw $ra,($sp)
jr $ra
L117:
addi $sp,$sp,28
move $s0,$sp
L118:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L119:
li $t1,1
sw $t1,-16($s0)
L120:
li $t1,1
sw $t1,-20($s0)
L121:
lw $t1,-16($s0)
li $v0,1
move $a0,$t1
syscall
L122:
lw $t1,-20($s0)
li $v0,1
move $a0,$t1
syscall
L123:
addi $fp,$sp,40
lw $t0,-12($s0)
sw $t0,-12($fp)
L124:
lw $t0,-16($s0)
sw $t0,-16($fp)
L125:
lw $t0,-20($s0)
sw $t0,-20($fp)
L126:
addi $t0,$sp,-24
sw $t0,-8($fp)
L127:
sw $sp,-4($fp)
addi $sp,$sp,40
jal L100
addi $sp,$sp,-40
L128:
lw $t1,-24($s0)
sw $t1,-12($s0)
L129:
li $v0,10
syscall
