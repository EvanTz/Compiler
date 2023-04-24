j L106
L100:
sw $ra,($sp)
L101:
lw $t1,-12($sp)
li $t2,1
add $t1,$t1,$t2
sw $t1,-20($sp)
L102:
lw $t1,-20($sp)
lw $t0,-16($sp)
sw $t1,($t0)
L103:
li $t1,4
sw $t1,-20($s0)
L104:
lw $t0,-16($sp)
lw $t1,($t0)
lw $t0,-8($sp)
sw $t1,($t0)
L105:
lw $ra,($sp)
jr $ra
L106:
addi $sp,$sp,28
move $s0,$sp
L107:
li $t1,1
sw $t1,-12($s0)
L108:
addi $fp,$sp,24
lw $t0,-12($s0)
sw $t0,-12($fp)
L109:
addi $t0,$sp,-16
sw $t0,-16($fp)
L110:
addi $t0,$sp,-24
sw $t0,-8($fp)
L111:
sw $sp,-4($fp)
addi $sp,$sp,24
jal L100
addi $sp,$sp,-24
L112:
lw $t1,-24($s0)
sw $t1,-20($s0)
L113:
lw $t1,-20($s0)
li $v0,1
move $a0,$t1
syscall
L114:
lw $t1,-16($s0)
li $v0,1
move $a0,$t1
syscall
L115:
li $v0,10
syscall
