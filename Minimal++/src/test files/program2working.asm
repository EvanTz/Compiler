j L110
L100:
sw $ra,($sp)
L101:
lw $t1,-12($sp)
li $v0,1
move $a0,$t1
syscall
L102:
lw $t1,-16($s0)
li $t2,1
sub $t1,$t1,$t2
sw $t1,-16($sp)
L103:
lw $t1,-16($sp)
sw $t1,-16($s0)
L104:
lw $t1,-16($s0)
li $t2,0
bgt $t1,$t2,L106
L105:
b L109
L106:
addi $fp,$sp,20
lw $t0,-12($sp)
sw $t0,-12($fp)
L107:
sw $sp,-4($fp)
addi $sp,$sp,20
jal L100
addi $sp,$sp,-20
L108:
b L109
L109:
lw $ra,($sp)
jr $ra
L110:
addi $sp,$sp,44
move $s0,$sp
L111:
li $t1,10
sw $t1,-12($s0)
L112:
lw $t1,-12($s0)
li $t2,0
bgt $t1,$t2,L114
L113:
b L123
L114:
lw $t1,-12($s0)
li $t2,1
sub $t1,$t1,$t2
sw $t1,-20($s0)
L115:
lw $t1,-20($s0)
sw $t1,-12($s0)
L116:
lw $t1,-12($s0)
li $v0,1
move $a0,$t1
syscall
L117:
lw $t1,-12($s0)
li $t2,5
bgt $t1,$t2,L119
L118:
b L121
L119:
li $t1,0
li $v0,1
move $a0,$t1
syscall
L120:
b L122
L121:
li $t1,1
li $v0,1
move $a0,$t1
syscall
L122:
b L112
L123:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L124:
lw $t1,-12($s0)
sw $t1,-16($s0)
L125:
addi $fp,$sp,20
lw $t0,-12($s0)
sw $t0,-12($fp)
L126:
sw $sp,-4($fp)
addi $sp,$sp,20
jal L100
addi $sp,$sp,-20
L127:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L128:
lw $t1,-12($s0)
sw $t1,-16($s0)
L129:
lw $t1,-12($s0)
li $t2,0
bgt $t1,$t2,L131
L130:
b L135
L131:
lw $t1,-12($s0)
li $v0,1
move $a0,$t1
syscall
L132:
lw $t1,-12($s0)
li $t2,1
sub $t1,$t1,$t2
sw $t1,-24($s0)
L133:
lw $t1,-24($s0)
sw $t1,-12($s0)
L134:
b L129
L135:
li $t1,0
lw $t2,-16($s0)
sub $t1,$t1,$t2
sw $t1,-28($s0)
L136:
lw $t1,-12($s0)
lw $t2,-28($s0)
bge $t1,$t2,L138
L137:
b L142
L138:
lw $t1,-12($s0)
li $v0,1
move $a0,$t1
syscall
L139:
lw $t1,-12($s0)
li $t2,1
sub $t1,$t1,$t2
sw $t1,-32($s0)
L140:
lw $t1,-32($s0)
sw $t1,-12($s0)
L141:
b L129
L142:
lw $t1,-12($s0)
li $t2,1
add $t1,$t1,$t2
sw $t1,-36($s0)
L143:
lw $t1,-36($s0)
sw $t1,-12($s0)
L144:
lw $t1,-12($s0)
lw $t2,-16($s0)
blt $t1,$t2,L146
L145:
b L150
L146:
lw $t1,-12($s0)
li $t2,1
add $t1,$t1,$t2
sw $t1,-40($s0)
L147:
lw $t1,-40($s0)
sw $t1,-12($s0)
L148:
lw $t1,-12($s0)
li $v0,1
move $a0,$t1
syscall
L149:
b L144
L150:
li $v0,10
syscall
