j L100
L100:
addi $sp,$sp,68
move $s0,$sp
L101:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L102:
li $v0,5
syscall
move $t1,$v0
sw $t1,-16($s0)
L103:
lw $t1,-12($s0)
lw $t2,-16($s0)
blt $t1,$t2,L105
L104:
b L119
L105:
lw $t1,-12($s0)
li $t2,2
blt $t1,$t2,L107
L106:
b L112
L107:
lw $t1,-16($s0)
li $t2,4
bgt $t1,$t2,L109
L108:
b L112
L109:
li $t1,0
li $t2,32767
sub $t1,$t1,$t2
sw $t1,-28($s0)
L110:
lw $t1,-28($s0)
li $v0,1
move $a0,$t1
syscall
L111:
b L113
L112:
li $t1,32767
li $v0,1
move $a0,$t1
syscall
L113:
lw $t1,-12($s0)
lw $t2,-16($s0)
add $t1,$t1,$t2
sw $t1,-32($s0)
L114:
lw $t1,-32($s0)
sw $t1,-20($s0)
L115:
lw $t1,-20($s0)
li $v0,1
move $a0,$t1
syscall
L116:
li $t1,1
lw $t2,-16($s0)
add $t1,$t1,$t2
sw $t1,-36($s0)
L117:
lw $t1,-36($s0)
sw $t1,-12($s0)
L118:
b L103
L119:
lw $t1,-20($s0)
li $v0,1
move $a0,$t1
syscall
L120:
lw $t1,-20($s0)
li $t2,1
bgt $t1,$t2,L122
L121:
b L126
L122:
lw $t1,-20($s0)
li $v0,1
move $a0,$t1
syscall
L123:
lw $t1,-20($s0)
li $t2,1
sub $t1,$t1,$t2
sw $t1,-40($s0)
L124:
lw $t1,-40($s0)
sw $t1,-20($s0)
L125:
b L120
L126:
lw $t1,-20($s0)
li $t2,1
beq $t1,$t2,L128
L127:
b L134
L128:
lw $t1,-20($s0)
lw $t2,-12($s0)
add $t1,$t1,$t2
sw $t1,-44($s0)
L129:
lw $t1,-44($s0)
lw $t2,-16($s0)
add $t1,$t1,$t2
sw $t1,-48($s0)
L130:
lw $t1,-48($s0)
li $v0,1
move $a0,$t1
syscall
L131:
lw $t1,-20($s0)
li $t2,1
sub $t1,$t1,$t2
sw $t1,-52($s0)
L132:
lw $t1,-52($s0)
sw $t1,-20($s0)
L133:
b L120
L134:
lw $t1,-20($s0)
li $t2,10
sub $t1,$t1,$t2
sw $t1,-56($s0)
L135:
lw $t1,-56($s0)
sw $t1,-20($s0)
L136:
lw $t1,-20($s0)
li $v0,1
move $a0,$t1
syscall
L137:
li $v0,5
syscall
move $t1,$v0
sw $t1,-24($s0)
L138:
lw $t1,-24($s0)
lw $t2,-20($s0)
ble $t1,$t2,L142
L139:
b L140
L140:
lw $t1,-24($s0)
li $t2,6
bgt $t1,$t2,L142
L141:
b L147
L142:
li $t1,0
lw $t2,-24($s0)
sub $t1,$t1,$t2
sw $t1,-60($s0)
L143:
lw $t1,-60($s0)
li $v0,1
move $a0,$t1
syscall
L144:
li $t1,0
lw $t2,-24($s0)
sub $t1,$t1,$t2
sw $t1,-64($s0)
L145:
lw $t1,-64($s0)
sw $t1,-24($s0)
L146:
b L148
L147:
lw $t1,-24($s0)
li $v0,1
move $a0,$t1
syscall
L148:
li $v0,10
syscall
