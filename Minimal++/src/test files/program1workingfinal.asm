j L145
L100:
sw $ra,($sp)
L101:
lw $t1,-12($sp)
li $t2,1
add $t1,$t1,$t2
sw $t1,-16($sp)
L102:
lw $t1,-16($sp)
sw $t1,-12($sp)
L103:
lw $t1,-12($sp)
li $t2,10
bgt $t1,$t2,L105
L104:
b L109
L105:
li $t1,0
lw $t2,-12($sp)
sub $t1,$t1,$t2
sw $t1,-20($sp)
L106:
lw $t1,-20($sp)
li $t2,100
add $t1,$t1,$t2
sw $t1,-24($sp)
L107:
lw $t1,-24($sp)
li $v0,1
move $a0,$t1
syscall
L108:
b L111
L109:
lw $t1,-12($sp)
li $t2,100
sub $t1,$t1,$t2
sw $t1,-28($sp)
L110:
lw $t1,-28($sp)
li $v0,1
move $a0,$t1
syscall
L111:
lw $t1,-12($sp)
li $t2,10
add $t1,$t1,$t2
sw $t1,-32($sp)
L112:
lw $t1,-32($sp)
lw $t0,-8($sp)
sw $t1,($t0)
L113:
lw $ra,($sp)
jr $ra
L114:
sw $ra,($sp)
L115:
lw $t1,-16($s0)
sw $t1,-20($s0)
L116:
lw $t1,-20($s0)
li $v0,1
move $a0,$t1
syscall
L117:
lw $t1,-16($s0)
li $v0,1
move $a0,$t1
syscall
L118:
lw $ra,($sp)
jr $ra
L119:
sw $ra,($sp)
L120:
li $t1,10
sw $t1,-12($s0)
L121:
lw $t1,-12($s0)
lw $t0,-8($sp)
sw $t1,($t0)
L122:
lw $ra,($sp)
jr $ra
L123:
sw $ra,($sp)
L124:
li $t1,5
lw $t2,-12($sp)
mul $t1,$t1,$t2
sw $t1,-24($sp)
L125:
lw $t1,-24($sp)
li $t2,20
sub $t1,$t1,$t2
sw $t1,-28($sp)
L126:
lw $t1,-28($sp)
sw $t1,-20($sp)
L127:
lw $t1,-20($sp)
li $t2,0
bgt $t1,$t2,L129
L128:
b L132
L129:
li $t1,2
lw $t0,-16($sp)
lw $t2,($t0)
mul $t1,$t1,$t2
sw $t1,-32($sp)
L130:
lw $t1,-32($sp)
li $v0,1
move $a0,$t1
syscall
L131:
b L134
L132:
li $t1,5
lw $t0,-16($sp)
lw $t2,($t0)
mul $t1,$t1,$t2
sw $t1,-36($sp)
L133:
lw $t1,-36($sp)
lw $t0,-8($sp)
sw $t1,($t0)
L134:
addi $fp,$sp,12
addi $t0,$sp,-40
sw $t0,-8($fp)
L135:
sw $sp,-4($fp)
addi $sp,$sp,12
jal L119
addi $sp,$sp,-12
L136:
lw $t1,-40($sp)
sw $t1,-20($sp)
L137:
lw $t1,-20($sp)
lw $t0,-16($sp)
lw $t2,($t0)
add $t1,$t1,$t2
sw $t1,-44($sp)
L138:
addi $fp,$sp,36
lw $t0,-16($sp)
lw $t0,($t0)
sw $t0,-12($fp)
L139:
addi $t0,$sp,-48
sw $t0,-8($fp)
L140:
sw $sp,-4($fp)
addi $sp,$sp,36
jal L100
addi $sp,$sp,-36
L141:
lw $t1,-44($sp)
lw $t2,-48($sp)
add $t1,$t1,$t2
sw $t1,-52($sp)
L142:
lw $t1,-52($sp)
sw $t1,-20($sp)
L143:
lw $t1,-20($sp)
lw $t0,-8($sp)
sw $t1,($t0)
L144:
lw $ra,($sp)
jr $ra
L145:
addi $sp,$sp,32
move $s0,$sp
L146:
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L147:
addi $fp,$sp,36
lw $t0,-12($s0)
sw $t0,-12($fp)
L148:
addi $t0,$sp,-24
sw $t0,-8($fp)
L149:
sw $sp,-4($fp)
addi $sp,$sp,36
jal L100
addi $sp,$sp,-36
L150:
lw $t1,-24($s0)
sw $t1,-16($s0)
L151:
addi $fp,$sp,12
sw $sp,-4($fp)
addi $sp,$sp,12
jal L114
addi $sp,$sp,-12
L152:
addi $fp,$sp,56
lw $t0,-16($s0)
sw $t0,-12($fp)
L153:
addi $t0,$sp,-20
sw $t0,-16($fp)
L154:
addi $t0,$sp,-28
sw $t0,-8($fp)
L155:
sw $sp,-4($fp)
addi $sp,$sp,56
jal L123
addi $sp,$sp,-56
L156:
lw $t1,-28($s0)
sw $t1,-12($s0)
L157:
lw $t1,-12($s0)
li $v0,1
move $a0,$t1
syscall
L158:
li $v0,10
syscall
