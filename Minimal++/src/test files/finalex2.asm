j L108
L100:
sw $ra,($sp)
L101:
lw $t1,-16($s0)
sw $t1,-20($s0)
L102:
lw $t0,-4($sp)
addi $t0,$t0,-12
lw $t1,($t0)
lw $t0,-4($sp)
addi $t0,$t0,-16
lw $t0,($t0)
sw $t1,($t0)
L103:
lw $ra,($sp)
jr $ra
L104:
sw $ra,($sp)
L105:
li $t1,2
sw $t1,-16($s0)
L106:
addi $fp,$sp,12
sw $sp,-4($fp)
addi $sp,$sp,12
jal L100
addi $sp,$sp,-12
L107:
lw $ra,($sp)
jr $ra
L108:
addi $sp,$sp,24
move $s0,$sp
L109:
li $t1,3
sw $t1,-12($s0)
L110:
li $t1,4
sw $t1,-16($s0)
L111:
addi $fp,$sp,20
lw $t0,-12($s0)
sw $t0,-12($fp)
L112:
addi $t0,$sp,-16
sw $t0,-16($fp)
L113:
sw $sp,-4($fp)
addi $sp,$sp,20
jal L104
addi $sp,$sp,-20
L114:
lw $t1,-16($s0)
li $v0,1
move $a0,$t1
syscall
L115:
lw $t1,-20($s0)
li $v0,1
move $a0,$t1
syscall
L116:
li $v0,10
syscall
