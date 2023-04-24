j L113
L100:
sw $ra,($sp)
L101:
lw $t1,-12($sp)
li $t2,2
div $t1,$t1,$t2
sw $t1,-24($sp)
L102:
lw $t1,-24($sp)
sw $t1,-16($sp)
L103:
li $t1,2
lw $t2,-16($sp)
mul $t1,$t1,$t2
sw $t1,-28($sp)
L104:
lw $t1,-12($sp)
lw $t2,-28($sp)
sub $t1,$t1,$t2
sw $t1,-32($sp)
L105:
lw $t1,-32($sp)
sw $t1,-20($sp)
L106:
lw $t1,-16($sp)
li $t2,0
bgt $t1,$t2,L108
L107:
b L111
L108:
addi $fp,$sp,36
lw $t0,-16($sp)
sw $t0,-12($fp)
L109:
sw $sp,-4($fp)
addi $sp,$sp,36
jal L100
addi $sp,$sp,-36
L110:
b L111
L111:
lw $t1,-20($sp)
li $v0,1
move $a0,$t1
syscall
L112:
lw $ra,($sp)
jr $ra
L113:
addi $sp,$sp,20
move $s0,$sp
L114:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L115:
addi $fp,$sp,36
lw $t0,-12($s0)
sw $t0,-12($fp)
L116:
sw $sp,-4($fp)
addi $sp,$sp,36
jal L100
addi $sp,$sp,-36
L117:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L118:
lw $t1,-12($s0)
li $t2,0
bgt $t1,$t2,L120
L119:
b L126
L120:
lw $t1,-12($s0)
li $v0,1
move $a0,$t1
syscall
L121:
addi $fp,$sp,36
lw $t0,-12($s0)
sw $t0,-12($fp)
L122:
sw $sp,-4($fp)
addi $sp,$sp,36
jal L100
addi $sp,$sp,-36
L123:
lw $t1,-12($s0)
li $t2,1
sub $t1,$t1,$t2
sw $t1,-16($s0)
L124:
lw $t1,-16($s0)
sw $t1,-12($s0)
L125:
b L118
L126:
li $v0,10
syscall
