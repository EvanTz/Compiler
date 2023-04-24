j L155
L100:
sw $ra,($sp)
L101:
lw $t1,-12($sp)
li $t2,22
add $t1,$t1,$t2
sw $t1,-32($sp)
L102:
lw $t1,-32($sp)
sw $t1,-12($sp)
L103:
lw $t1,-12($sp)
li $t2,23
bgt $t1,$t2,L105
L104:
b L107
L105:
lw $t0,-16($sp)
lw $t1,($t0)
li $t2,23
bge $t1,$t2,L109
L106:
b L107
L107:
lw $t1,-20($sp)
li $t2,2
blt $t1,$t2,L111
L108:
b L109
L109:
li $t1,232
lw $t0,-28($sp)
sw $t1,($t0)
L110:
b L113
L111:
li $t1,0
li $t2,1
sub $t1,$t1,$t2
sw $t1,-36($sp)
L112:
lw $t1,-36($sp)
lw $t0,-28($sp)
sw $t1,($t0)
L113:
lw $t0,-28($sp)
lw $t1,($t0)
lw $t2,-12($s0)
add $t1,$t1,$t2
sw $t1,-40($sp)
L114:
lw $t1,-40($sp)
lw $t0,-8($sp)
sw $t1,($t0)
L115:
lw $ra,($sp)
jr $ra
L116:
sw $ra,($sp)
L117:
li $t1,0
lw $t0,-12($sp)
lw $t2,($t0)
sub $t1,$t1,$t2
sw $t1,-20($sp)
L118:
lw $t1,-20($sp)
li $t2,4
div $t1,$t1,$t2
sw $t1,-24($sp)
L119:
lw $t1,-24($sp)
li $t2,2
sub $t1,$t1,$t2
sw $t1,-28($sp)
L120:
li $t1,0
lw $t2,-16($s0)
sub $t1,$t1,$t2
sw $t1,-32($sp)
L121:
li $t1,34
lw $t2,-32($sp)
mul $t1,$t1,$t2
sw $t1,-36($sp)
L122:
lw $t1,-28($sp)
lw $t2,-36($sp)
add $t1,$t1,$t2
sw $t1,-40($sp)
L123:
lw $t1,-40($sp)
lw $t2,-16($sp)
add $t1,$t1,$t2
sw $t1,-44($sp)
L124:
lw $t1,-44($sp)
li $v0,1
move $a0,$t1
syscall
L125:
lw $ra,($sp)
jr $ra
L126:
sw $ra,($sp)
L127:
lw $t1,-12($sp)
lw $t0,-16($sp)
lw $t2,($t0)
mul $t1,$t1,$t2
sw $t1,-28($sp)
L128:
lw $t1,-28($sp)
lw $t2,-24($s0)
mul $t1,$t1,$t2
sw $t1,-32($sp)
L129:
lw $t1,-32($sp)
lw $t0,-8($sp)
sw $t1,($t0)
L130:
lw $ra,($sp)
jr $ra
L131:
sw $ra,($sp)
L132:
li $t1,9
lw $t2,-12($sp)
mul $t1,$t1,$t2
sw $t1,-32($sp)
L133:
lw $t1,-32($sp)
li $t2,3
beq $t1,$t2,L135
L134:
b L138
L135:
lw $t1,-16($sp)
li $v0,1
move $a0,$t1
syscall
L136:
li $t1,2
sw $t1,-12($sp)
L137:
b L132
L138:
addi $fp,$sp,48
lw $t0,-20($sp)
sw $t0,-12($fp)
L139:
lw $t0,-28($sp)
sw $t0,-16($fp)
L140:
addi $t0,$sp,-36
sw $t0,-8($fp)
L141:
sw $sp,-4($fp)
addi $sp,$sp,48
jal L131
addi $sp,$sp,-48
L142:
lw $t1,-36($sp)
lw $t2,-12($sp)
add $t1,$t1,$t2
sw $t1,-40($sp)
L143:
lw $t1,-40($sp)
sw $t1,-20($s0)
L144:
addi $fp,$sp,48
addi $t0,$sp,-20
sw $t0,-12($fp)
L145:
lw $t0,-16($sp)
sw $t0,-16($fp)
L146:
sw $sp,-4($fp)
addi $sp,$sp,48
jal L116
addi $sp,$sp,-48
L147:
addi $fp,$sp,36
lw $t0,-12($sp)
sw $t0,-12($fp)
L148:
lw $t0,-4($sp)
addi $t0,$t0,-20
sw $t0,-16($fp)
L149:
lw $t0,-16($sp)
sw $t0,-20($fp)
L150:
lw $t0,-32($s0)
sw $t0,-24($fp)
L151:
addi $t0,$sp,-44
sw $t0,-8($fp)
L152:
sw $sp,-4($fp)
addi $sp,$sp,36
jal L126
addi $sp,$sp,-36
L153:
lw $t1,-44($sp)
lw $t0,-8($sp)
sw $t1,($t0)
L154:
lw $ra,($sp)
jr $ra
L155:
addi $sp,$sp,136
move $s0,$sp
L156:
li $t1,45
sw $t1,-24($s0)
L157:
lw $t1,-24($s0)
li $t2,23
bgt $t1,$t2,L159
L158:
b L169
L159:
addi $fp,$sp,44
lw $t0,-12($s0)
sw $t0,-12($fp)
L160:
addi $t0,$sp,-16
sw $t0,-16($fp)
L161:
lw $t0,-20($s0)
sw $t0,-20($fp)
L162:
lw $t0,-24($s0)
sw $t0,-24($fp)
L163:
addi $t0,$sp,-28
sw $t0,-28($fp)
L164:
addi $t0,$sp,-80
sw $t0,-8($fp)
L165:
sw $sp,-4($fp)
addi $sp,$sp,44
jal L100
addi $sp,$sp,-44
L166:
li $t1,232
lw $t2,-80($s0)
add $t1,$t1,$t2
sw $t1,-84($s0)
L167:
lw $t1,-84($s0)
sw $t1,-28($s0)
L168:
b L170
L169:
lw $t1,-32($s0)
li $v0,1
move $a0,$t1
syscall
L170:
addi $fp,$sp,48
lw $t0,-12($s0)
sw $t0,-12($fp)
L171:
lw $t0,-16($s0)
sw $t0,-16($fp)
L172:
addi $t0,$sp,-88
sw $t0,-8($fp)
L173:
sw $sp,-4($fp)
addi $sp,$sp,48
jal L131
addi $sp,$sp,-48
L174:
li $t1,0
lw $t2,-32($s0)
sub $t1,$t1,$t2
sw $t1,-92($s0)
L175:
lw $t1,-92($s0)
li $t2,2
mul $t1,$t1,$t2
sw $t1,-96($s0)
L176:
lw $t1,-88($s0)
lw $t2,-96($s0)
bgt $t1,$t2,L182
L177:
b L178
L178:
lw $t1,-36($s0)
lw $t2,-40($s0)
blt $t1,$t2,L180
L179:
b L184
L180:
lw $t1,-44($s0)
lw $t2,-48($s0)
beq $t1,$t2,L184
L181:
b L182
L182:
lw $t1,-24($s0)
li $v0,1
move $a0,$t1
syscall
L183:
b L170
L184:
li $t1,0
lw $t2,-52($s0)
sub $t1,$t1,$t2
sw $t1,-100($s0)
L185:
li $t1,9
lw $t2,-100($s0)
mul $t1,$t1,$t2
sw $t1,-104($s0)
L186:
lw $t1,-104($s0)
li $t2,3
beq $t1,$t2,L188
L187:
b L190
L188:
lw $t1,-56($s0)
li $v0,1
move $a0,$t1
syscall
L189:
b L184
L190:
li $t1,0
lw $t2,-12($s0)
sub $t1,$t1,$t2
sw $t1,-108($s0)
L191:
li $t1,0
lw $t2,-52($s0)
sub $t1,$t1,$t2
sw $t1,-112($s0)
L192:
lw $t1,-108($s0)
lw $t2,-112($s0)
mul $t1,$t1,$t2
sw $t1,-116($s0)
L193:
lw $t1,-116($s0)
li $t2,8467
beq $t1,$t2,L195
L194:
b L197
L195:
lw $t1,-60($s0)
li $v0,1
move $a0,$t1
syscall
L196:
b L184
L197:
lw $t1,-64($s0)
li $v0,1
move $a0,$t1
syscall
L198:
li $t1,0
li $v0,1
move $a0,$t1
syscall
L199:
addi $fp,$sp,48
addi $t0,$sp,-52
sw $t0,-12($fp)
L200:
lw $t0,-48($s0)
sw $t0,-16($fp)
L201:
sw $sp,-4($fp)
addi $sp,$sp,48
jal L116
addi $sp,$sp,-48
L202:
lw $t1,-68($s0)
li $t2,4
sub $t1,$t1,$t2
sw $t1,-120($s0)
L203:
addi $fp,$sp,44
lw $t0,-12($s0)
sw $t0,-12($fp)
L204:
addi $t0,$sp,-16
sw $t0,-16($fp)
L205:
lw $t0,-20($s0)
sw $t0,-20($fp)
L206:
lw $t0,-24($s0)
sw $t0,-24($fp)
L207:
addi $t0,$sp,-28
sw $t0,-28($fp)
L208:
addi $t0,$sp,-124
sw $t0,-8($fp)
L209:
sw $sp,-4($fp)
addi $sp,$sp,44
jal L100
addi $sp,$sp,-44
L210:
lw $t1,-120($s0)
lw $t2,-124($s0)
add $t1,$t1,$t2
sw $t1,-128($s0)
L211:
lw $t1,-128($s0)
li $v0,1
move $a0,$t1
syscall
L212:
lw $t1,-72($s0)
li $t2,2
add $t1,$t1,$t2
sw $t1,-132($s0)
L213:
lw $t1,-132($s0)
li $v0,1
move $a0,$t1
syscall
L214:
li $v0,5
syscall
move $t1,$v0
sw $t1,-76($s0)
L215:
li $v0,10
syscall
