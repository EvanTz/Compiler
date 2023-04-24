j L128
L100:
sw $ra,($sp)
L101:
lw $t1,-16($s0)
li $t2,0
beq $t1,$t2,L103
L102:
b L105
L103:
li $t1,1
sw $t1,-16($s0)
L104:
b L105
L105:
lw $t1,-12($sp)
li $t2,2
div $t1,$t1,$t2
sw $t1,-28($sp)
L106:
lw $t1,-28($sp)
sw $t1,-16($sp)
L107:
li $t1,2
lw $t2,-16($sp)
mul $t1,$t1,$t2
sw $t1,-32($sp)
L108:
lw $t1,-12($sp)
lw $t2,-32($sp)
sub $t1,$t1,$t2
sw $t1,-36($sp)
L109:
lw $t1,-36($sp)
sw $t1,-20($sp)
L110:
lw $t1,-16($s0)
lw $t2,-20($sp)
mul $t1,$t1,$t2
sw $t1,-40($sp)
L111:
lw $t1,-20($s0)
lw $t2,-40($sp)
add $t1,$t1,$t2
sw $t1,-44($sp)
L112:
lw $t1,-44($sp)
sw $t1,-20($s0)
L113:
lw $t1,-16($s0)
sw $t1,-24($sp)
L114:
lw $t1,-16($s0)
li $t2,10
mul $t1,$t1,$t2
sw $t1,-48($sp)
L115:
lw $t1,-48($sp)
sw $t1,-16($s0)
L116:
lw $t1,-16($sp)
li $t2,0
bgt $t1,$t2,L118
L117:
b L121
L118:
addi $fp,$sp,52
lw $t0,-16($sp)
sw $t0,-12($fp)
L119:
sw $sp,-4($fp)
addi $sp,$sp,52
jal L100
addi $sp,$sp,-52
L120:
b L121
L121:
lw $t1,-24($sp)
li $t2,1
beq $t1,$t2,L123
L122:
b L126
L123:
lw $t1,-20($s0)
li $v0,1
move $a0,$t1
syscall
L124:
li $t1,0
sw $t1,-20($s0)
L125:
b L126
L126:
li $t1,1
sw $t1,-16($s0)
L127:
lw $ra,($sp)
jr $ra
L128:
addi $sp,$sp,28
move $s0,$sp
L129:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L130:
addi $fp,$sp,52
lw $t0,-12($s0)
sw $t0,-12($fp)
L131:
sw $sp,-4($fp)
addi $sp,$sp,52
jal L100
addi $sp,$sp,-52
L132:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L133:
lw $t1,-12($s0)
li $t2,0
bgt $t1,$t2,L135
L134:
b L141
L135:
lw $t1,-12($s0)
li $v0,1
move $a0,$t1
syscall
L136:
addi $fp,$sp,52
lw $t0,-12($s0)
sw $t0,-12($fp)
L137:
sw $sp,-4($fp)
addi $sp,$sp,52
jal L100
addi $sp,$sp,-52
L138:
lw $t1,-12($s0)
li $t2,1
sub $t1,$t1,$t2
sw $t1,-24($s0)
L139:
lw $t1,-24($s0)
sw $t1,-12($s0)
L140:
b L133
L141:
li $v0,10
syscall
