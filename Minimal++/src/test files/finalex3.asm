j L110
L100:
sw $ra,($sp)
L101:
li $t1,1
lw $t0,-4($sp)
addi $t0,$t0,-12
sw $t1,($t0)
L102:
li $t1,1
lw $t0,-8($sp)
sw $t1,($t0)
L103:
lw $ra,($sp)
jr $ra
L104:
sw $ra,($sp)
L105:
addi $fp,$sp,12
addi $t0,$sp,-16
sw $t0,-8($fp)
L106:
sw $sp,-4($fp)
addi $sp,$sp,12
jal L100
addi $sp,$sp,-12
L107:
lw $t1,-16($sp)
sw $t1,-12($s0)
L108:
lw $t1,-12($s0)
lw $t0,-8($sp)
sw $t1,($t0)
L109:
lw $ra,($sp)
jr $ra
L110:
addi $sp,$sp,20
move $s0,$sp
L111:
addi $fp,$sp,20
addi $t0,$sp,-16
sw $t0,-8($fp)
L112:
sw $sp,-4($fp)
addi $sp,$sp,20
jal L104
addi $sp,$sp,-20
L113:
lw $t1,-16($s0)
li $v0,1
move $a0,$t1
syscall
L114:
lw $t1,-12($s0)
li $v0,1
move $a0,$t1
syscall
L115:
li $v0,10
syscall
