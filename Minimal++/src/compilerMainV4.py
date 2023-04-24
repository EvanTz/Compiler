# Evangelos Tzortzis
# AM: 3088
# username: cse53088

import sys
import pathlib

in_name = ''


#############################
#          Lexer
#############################
class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens_1 = []
        self.source_index = 0
        self.text_line = 1

    def tokenize(self):
        reserved_words = ['program', 'declare', 'if', 'else', 'while', 'doublewhile', 'loop',
                          'exit', 'forcase', 'incase', 'when', 'default', 'not', 'and',
                          'or', 'function', 'procedure', 'call', 'return', 'in', 'inout', 'input', 'print', 'then']

        reserved_words_tokens = ['program_tk', 'declare_tk', 'if_tk', 'else_tk', 'while_tk', 'doublewhile_tk',
                                 'loop_tk', 'exit_tk', 'forcase_tk', 'incase_tk', 'when_tk', 'default_tk',
                                 'not_tk', 'and_tk', 'or_tk', 'function_tk', 'procedure_tk', 'call_tk',
                                 'return_tk', 'in_tk', 'inout_tk', 'input_tk', 'print_tk', 'then_tk']

        source_code = self.source_code
        source_index = self.source_index
        text_line = self.text_line

        # the 1st time the program runs
        if self.source_index == 0:
            # make array of source code
            srr = []
            srr_index = 0
            for i in source_code:
                srr += i
            srr.append('@')  # add last line as '@'
            # check for '$' now so it can be used for comment checking
            for i in srr:
                if i == '$':
                    print('ERROR: character "$" does not belong in the language')
                    quit()

            # check for and remove comments
            while srr_index < len(srr)-2:
                char = srr[srr_index]
                next_char = srr[srr_index + 1]
                if char == '/' and next_char == "/":
                    srr[srr_index] = '$'
                    srr[srr_index + 1] = '$'
                    srr_index += 2
                    while srr[srr_index] != '\n' and srr_index < len(srr)-2:
                        srr[srr_index] = '$'
                        srr_index += 1

                elif char == '/' and next_char == '*':
                    srr[srr_index] = '$'
                    srr[srr_index + 1] = '$'
                    srr_index += 2
                    while srr[srr_index] != '*' or srr[srr_index + 1] != '/' and srr_index < len(srr)-2:
                        if srr[srr_index] != '\n':
                            srr[srr_index] = '$'
                        if srr[srr_index] != '*' and srr[srr_index + 1] != '/' and srr_index == len(srr)-2:
                            print('ERROR: multi line comments are not closed with "*/"')
                            quit()
                        srr_index += 1
                    srr[srr_index] = '$'
                    srr[srr_index + 1] = '$'
                    srr_index += 1

                elif char == '*' and next_char == '/':
                    print('ERROR: multi line comment end "*/" without beginning')
                    quit()
                srr_index += 1

            srr = [x for x in srr if x != '$']
            self.source_code = ''.join(srr).strip()
            og_sc = ''.join(srr)

            source_code = self.source_code
            # count lines with whitespace in the beginning
            og_sc_index = 0
            while og_sc[og_sc_index].isspace():
                if og_sc[og_sc_index] == '\n':
                    self.text_line += 1
                og_sc_index += 1

        if self.source_index < len(source_code):
            char1 = source_code[source_index]

            # remove whitespaces and remove/mark lines for error info
            if char1.isspace() or char1 == '\n':
                if char1 == '\n':
                    self.text_line += 1
                self.source_index += 1
                while source_code[self.source_index].isspace() or source_code[self.source_index] == '\n' and\
                        self.source_index < len(source_code)-1:
                    if source_code[self.source_index] == '\n':
                        self.text_line += 1
                    self.source_index += 1
                text_line = self.text_line
            source_index = self.source_index

            char = source_code[source_index]

            # first char of ids should be letter ...
            if char.isalpha():
                if source_index < len(source_code)-1:
                    next_index_temp = self.source_index+1
                    temp_id = [char]
                    # ... then letter or digit
                    while source_code[next_index_temp].isdigit() or source_code[next_index_temp].isalpha():
                        temp_id.append(source_code[next_index_temp])
                        next_index_temp += 1
                        self.source_index += 1
                    final_find = ''.join(temp_id[0:30])
                    # check for reserved word
                    if final_find in reserved_words:
                        self.tokens_1.append([reserved_words_tokens[reserved_words.index(final_find)].upper(),
                                              final_find, text_line])
                    else:
                        self.tokens_1.append(['id_tk'.upper(), final_find, text_line])

            # tokenize numbers/digit sequences
            elif char.isdigit():
                if source_index < len(source_code)-1:
                    next_index_temp_digit = self.source_index+1
                    temp_digit = [char]
                    while source_code[next_index_temp_digit].isdigit():
                        temp_digit.append(source_code[next_index_temp_digit])
                        next_index_temp_digit += 1
                        self.source_index += 1
                    final_digit = int(''.join(temp_digit))
                    if source_code[next_index_temp_digit].isalpha():
                        print('ERROR: letter after digit, invalid syntax: ' +
                              ''.join(''.join(temp_digit) + source_code[self.source_index+1]) +
                              ' at line %s' % text_line)
                        quit()
                    self.tokens_1.append(['number'.upper(), str(final_digit), text_line])

            # tokenize operators
            elif char == '+':
                self.tokens_1.append(['plus_tk'.upper(), char, text_line])
            elif char == '-':
                self.tokens_1.append(['minus_tk'.upper(), char, text_line])
            elif char == '*' and source_code[source_index + 1] != '/':
                self.tokens_1.append(['times_tk'.upper(), char, text_line])
            elif char == '/' and source_code[source_index + 1] != '*' and source_code[source_index + 1] != '/':
                self.tokens_1.append(['over_tk'.upper(), char, text_line])

            # tokenize comparison operators
            elif char == '<' and source_code[source_index+1] != '>' and source_code[source_index+1] != '=':
                self.tokens_1.append(['smaller_tk'.upper(), char, text_line])

            elif char == '<' and source_code[source_index+1] == '>':
                self.tokens_1.append(['different_tk'.upper(), ''.join(char + source_code[source_index+1]), text_line])
                self.source_index += 1   # because the next '>' gets tokenized

            elif char == '<'and source_code[source_index+1] == '=':
                self.tokens_1.append(['smallerequal_tk'.upper(), ''.join(char + source_code[source_index+1]),
                                      text_line])
                self.source_index += 1   # because the next '=' gets tokenized

            elif char == '>' and source_code[source_index+1] != '=':
                self.tokens_1.append(['larger_tk'.upper(), char, text_line])

            elif char == '>'and source_code[source_index+1] == '=':
                self.tokens_1.append(['largerequal_tk'.upper(), ''.join(char + source_code[source_index+1]), text_line])
                self.source_index += 1
            elif char == '=':
                self.tokens_1.append(['equal_tk'.upper(), char, text_line])

            # tokenize assign
            elif char == ":"and source_code[source_index + 1] == "=":
                self.tokens_1.append(['assign_tk'.upper(), ''.join(char + source_code[source_index+1]), text_line])
                self.source_index += 1

            # tokenize dividers
            elif char == ';':
                self.tokens_1.append(['semicolon_tk'.upper(), char, text_line])
            elif char == ':'and source_code[source_index + 1] != "=":
                self.tokens_1.append(['colon_tk'.upper(), char, text_line])
            elif char == ',':
                self.tokens_1.append(['comma_tk'.upper(), char, text_line])

            # tokenize grouping symbols
            elif char == '(':
                self.tokens_1.append(['left_paren_tk'.upper(), char, text_line])
            elif char == ')':
                self.tokens_1.append(['right_paren_tk'.upper(), char, text_line])
            elif char == '[':
                self.tokens_1.append(['left_bracket_tk'.upper(), char, text_line])
            elif char == ']':
                self.tokens_1.append(['right_bracket_tk'.upper(), char, text_line])
            elif char == '{':
                self.tokens_1.append(['left_brace_tk'.upper(), char, text_line])
            elif char == '}':
                self.tokens_1.append(['right_brace_tk'.upper(), char, text_line])

            # tokenize comment symbols
            elif char == '/' and source_code[source_index + 1] == "*":
                self.tokens_1.append(['multi_comment_start_tk'.upper(), ''.join(char + source_code[source_index+1]),
                                      text_line])
                self.source_index += 1
            elif char == '/' and source_code[source_index + 1] == "/":
                self.tokens_1.append(['single_comment_tk'.upper(), ''.join(char + source_code[source_index+1]),
                                      text_line])
                self.source_index += 1
            elif char == '*' and source_code[source_index + 1] == "/":
                self.tokens_1.append(['multi_comment_end_tk'.upper(), ''.join(char + source_code[source_index+1]),
                                      text_line])
                self.source_index += 1

            # mark EOF with '@'
            elif char == '@' and source_index == len(source_code) - 1:
                self.tokens_1.append(['EOF_TK', char, text_line])

            # check if char belongs in the language
            elif not char.isspace():
                print('Character: %s does not belong in language ' % char + 'at line: %s' % text_line)
                quit()

            else:
                pass

            self.source_index += 1

        return self.tokens_1


#############################################
# Parser/Intermediate/Symbol Table/Final Code
#############################################
class Parse(object):

    def __init__(self, content):
        self.content = content
        self.tokens = []
        self.token_index = 0
        self.statements_tokens = ['ASSIGN_TK', 'IF_TK', 'WHILE_TK', 'DOUBLEWHILE_TK', 'LOOP_TK', 'EXIT_TK',
                                  'FORCASE_TK', 'INCASE_TK', 'CALL_TK', 'RETURN_TK', 'INPUT_TK', 'PRINT_TK']
        self.token = 0
        self.loop_exit_counter = 0
        self.mark_exit = False
        self.func_c = 0
        self.ret = 0

        self.lex = Lexer(content)

        # for intermediate code generation
        self.counter_temp = 1
        self.quads = []
        self.quad_count = 100

        # for .c file
        self.declared_vars = []
        self.startofmainprogram = 0

        # for symbol table
        self.scopes = []
        self.nesting_level = -1
        self.offset = [0]
        self.symbol_output = open(in_name+'_symbol_table_history.txt', 'w')
        self.symbol_output.write('Symbol table history:\n')

        # for final code
        self.finalcode = ['']

    def get_token(self):
        self.tokens = self.lex.tokenize()
        if self.tokens[self.token_index][0] != 'EOF_TK':
            self.token_index += 1
            return self.tokens[self.token_index-1]
        elif self.tokens[self.token_index][0] == 'EOF_TK':
            return self.tokens[self.token_index]

    def parse(self):
        # Token Legend:
        # token_type = self.tokens[self.token_index][0]
        # token_value = self.tokens[self.token_index][1]
        # token_line = self.tokens[self.token_index][2]
        self.program()
        self.symbol_output.close()

    def program(self):
        self.token = self.get_token()
        if self.token[0] == 'PROGRAM_TK':
            main_program_id = 'PROGRAM_TK'
            self.token = self.get_token()
            if self.token[0] == 'ID_TK':
                name_id = self.token[1]
                self.token = self.get_token()
                if self.token[0] == 'LEFT_BRACE_TK':
                    self.token = self.get_token()

                    self.add_scope()  # scope for main program

                    self.programblock(name_id, main_program_id)

                    self.delete_scope()  # the scope is the final/main one  and it is not deleted

                    if self.token[0] != 'RIGHT_BRACE_TK':
                        print('ERROR: program/subprogram/statements does not end with "}"')
                        quit()
                    self.token = self.get_token()
                    if self.token[0] != 'EOF_TK':
                        print('ERROR: end of file expected after program braces, instead found: ', self.token[1],
                              ' at line:', self.token[2])
                        quit()
                else:
                    print('ERROR: program does not start with "{" at line ' + str(self.token[2]))
                    quit()
            else:
                print('ERROR: program name "' + self.token[1] +
                      '" at line ' + str(self.token[2]) + ' is not valid')
                quit()

        else:
            print("program does not start with the word 'program'")
            quit()

    def programblock(self, name_id, main_program_id=None):
        self.declarations()
        self.subprograms()

        self.startofmainprogram = len(self.quads)+1
        self.genquad('begin_block', name_id, '_', '_')

        self.statements()

        if main_program_id == 'PROGRAM_TK':

            self.genquad('halt', '_', '_', '_')

            # call final code for main
            self.final_code(name_id, is_main=1)

        self.genquad('end_block', name_id, '_', '_')

    def declarations(self):
        while self.token[0] == 'DECLARE_TK':
            self.token = self.get_token()
            self.varlist()
            if self.token[0] != 'SEMICOLON_TK':
                print('ERROR: declarations require ";" ')
                quit()
            else:
                self.token = self.get_token()

    def varlist(self):
        if self.token[0] == 'ID_TK':
            self.add_entity(0, self.token[1])  # symbol table  add variable entities
            self.declared_vars.append(self.token[1])  # for .c file
            self.token = self.get_token()
            while self.token[0] == 'COMMA_TK':
                self.token = self.get_token()
                if self.token[0] == 'ID_TK':
                    self.add_entity(0, self.token[1])  # symbol table  add variable entities
                    self.declared_vars.append(self.token[1])  # for .c file
                    self.token = self.get_token()
                else:
                    print('ERROR: wrong syntax at line: ', self.token[2])
                    quit()
        elif self.token[0] == 'SEMICOLON_TK':
            return
        else:
            print('ERROR: wrong syntax in declaration at line ', self.tokens[self.token_index-2][2])
            quit()

    def subprograms(self):
        while self.token[0] == 'FUNCTION_TK' or self.token[0] == 'PROCEDURE_TK':
            if self.token[0] == 'FUNCTION_TK':
                self.token = self.get_token()
                func_name = self.tokens[self.token_index-1][1]
                self.func_c += 1
                self.subprogram()
                self.func_c -= 1
                if self.ret == 0:
                    print('ERROR: no return statement in function: ', func_name)
                    quit()
                else:
                    self.ret = 0
            else:
                self.token = self.get_token()
                self.subprogram()

    def subprogram(self):
        if self.token[0] == 'ID_TK':
            sub_type = self.tokens[self.token_index-2][0]  # get the type of subprogram
            program_id = self.token[1]  # program_id(name) in symbol table (for function/procedure)
            self.add_entity(3, name=program_id, subprogram_type=sub_type)

            self.token = self.get_token()
            self.funcbody(program_id)

            self.scopes[self.nesting_level - 1][-1][2] = self.find_starting_quad(program_id)  # starting quad

            # final code call
            self.final_code(program_id)

            self.delete_scope()
        else:
            print('ERROR: invalid or no function/procedure name at line: ', self.tokens[self.token_index-1][2])
            quit()

    def funcbody(self, name_id):
        self.formalpars()
        if self.token[0] == 'LEFT_BRACE_TK':
            self.token = self.get_token()
            self.programblock(name_id)
            if self.token[0] != 'RIGHT_BRACE_TK':
                print('ERROR: closing brace expected at line: ', self.tokens[self.token_index-1][2])
                quit()
            else:
                self.token = self.get_token()
        else:
            print('ERROR: opening brace missing at line: ', self.tokens[self.token_index-1][2])
            quit()

    def formalpars(self):
        if self.token[0] == 'LEFT_PAREN_TK':
            self.token = self.get_token()
            self.formalparlist()
            if self.token[0] == 'RIGHT_PAREN_TK':
                self.token = self.get_token()
            else:
                print('ERROR: closing parenthesis missing at line: ', self.tokens[self.token_index-1][2])
                quit()
        else:
            print('ERROR: opening parenthesis missing at line: ', self.tokens[self.token_index-1][2])
            quit()

    def formalparlist(self):
        if self.token[0] == 'RIGHT_PAREN_TK':
            return
        self.formalparitem()
        while self.token[0] == 'COMMA_TK':
            self.token = self.get_token()
            self.formalparitem()

    def formalparitem(self):
        if self.token[0] == 'IN_TK' or self.token[0] == 'INOUT_TK':
            if self.token[0] == 'IN_TK':
                pmode = 1
            else:
                pmode = 2
            self.token = self.get_token()
            if self.token[0] == 'ID_TK':
                parname = self.token[1]
                self.token = self.get_token()

                self.add_entity(2, name=parname, par_mode=pmode)  # get the in/inout to the symbol table
            else:
                print('ERROR: wrong function or procedure initialization at line: ', self.token[2])
                quit()
        else:
            print('ERROR: invalid passing type, in or inout expected at line: ',
                  self.tokens[self.token_index - 1][2])
            quit()

    def statements(self):
        if self.token[0] in self.statements_tokens or self.token[0] == 'ID_TK':
            self.statement()
        elif self.token[0] == 'LEFT_BRACE_TK':
            self.token = self.get_token()
            if self.token[0] in self.statements_tokens or self.token[0] == 'ID_TK':
                self.statement()
                while self.token[0] == 'SEMICOLON_TK':
                    self.token = self.get_token()
                    if self.token[0] in self.statements_tokens or self.token[0] == 'ID_TK':
                        self.statement()
                    else:
                        print('ERROR: invalid statements syntax at line ', self.tokens[self.token_index-1][2])
                        quit()
                if self.token[0] != 'RIGHT_BRACE_TK':
                    print('ERROR: closing brace of expected after statements at line: ',
                          self.tokens[self.token_index-2][2])
                    quit()
                else:
                    self.token = self.get_token()
            else:
                print('ERROR: at least one statement expected/wrong statement after opening brace at line: ',
                      self.token[2])
                quit()
        else:
            print('ERROR: at least one statement required in every program/subprogram, or wrong statement syntax')
            quit()

    def statement(self):
        if self.token[0] == 'ID_TK':
            self.assignment_stat()
        elif self.token[0] == 'IF_TK':
            self.if_stat()
        elif self.token[0] == 'WHILE_TK':
            self.while_stat()
        elif self.token[0] == 'DOUBLEWHILE_TK':
            self.doublewhile_stat()
        elif self.token[0] == 'LOOP_TK':
            self.loop_stat()
        elif self.token[0] == 'EXIT_TK':
            self.exit_stat()
        elif self.token[0] == 'FORCASE_TK':
            self.forcase_stat()
        elif self.token[0] == 'INCASE_TK':
            self.incase_stat()
        elif self.token[0] == 'CALL_TK':
            self.call_stat()
        elif self.token[0] == 'RETURN_TK':
            self.return_stat()
        elif self.token[0] == 'INPUT_TK':
            self.input_stat()
        elif self.token[0] == 'PRINT_TK':
            self.print_stat()
        else:
            print('ERROR: unknown statement')
            quit()

    def assignment_stat(self):
        idplace = self.token[1]
        self.search_entity(0, idplace)
        self.token = self.get_token()
        if self.token[0] == 'ASSIGN_TK':
            self.token = self.get_token()
            eplace = self.expression()
            self.genquad(':=', eplace, '_', idplace)
        else:
            print('ERROR: variable without assignment in statements:', self.tokens[self.token_index-2][1])
            quit()

    def if_stat(self):
        self.token = self.get_token()
        if self.token[0] == 'LEFT_PAREN_TK':
            self.token = self.get_token()
            (btrue, bfalse) = self.condition()
            if self.token[0] == 'RIGHT_PAREN_TK':
                self.token = self.get_token()
                if self.token[0] == 'THEN_TK':
                    self.token = self.get_token()
                    self.backpatch(btrue, self.nextquad())
                    self.statements()
                    iflist = self.makelist(self.nextquad())
                    self.genquad('jump', '_', '_', '_')
                    self.backpatch(bfalse, self.nextquad())
                    self.elsepart()
                    self.backpatch(iflist, self.nextquad())
                else:
                    print('ERROR: if statement without "then"')
                    quit()
            else:
                print('ERROR: closing parenthesis expected after conditions at line: ', self.token[2])
                quit()
        else:
            print('ERROR: opening parenthesis expected after "if" statement at line: ',
                  self.tokens[self.token_index-2][2])
            quit()

    def condition(self):
        (q1true, q1false) = self.boolterm()
        btrue = q1true
        bfalse = q1false
        while self.token[0] == 'OR_TK':
            self.token = self.get_token()
            self.backpatch(bfalse, self.nextquad())
            (q2true, q2false) = self.boolterm()
            btrue = self.mergelist(btrue, q2true)
            bfalse = q2false
        return btrue, bfalse

    def boolterm(self):
        (r1true, r1false) = self.boolfactor()
        qtrue = r1true
        qfalse = r1false
        while self.token[0] == 'AND_TK':
            self.token = self.get_token()
            self.backpatch(qtrue, self.nextquad())
            (r2true, r2false) = self.boolfactor()
            qfalse = self.mergelist(qfalse, r2false)
            qtrue = r2true
        return qtrue, qfalse

    def boolfactor(self):
        rtrue = ''
        rfalse = ''
        if self.token[0] == 'NOT_TK':  # changed (rtrue, rfalse) to (rfalse, rtrue) for 'not'
            self.token = self.get_token()
            if self.token[0] == 'LEFT_BRACKET_TK':
                self.token = self.get_token()
                (rfalse, rtrue) = self.condition()
                if self.token[0] != 'RIGHT_BRACKET_TK':
                    print('ERROR: no closing bracket in a condition')
                    quit()
                else:
                    self.token = self.get_token()
            else:
                print('ERROR: opening bracket expected after "not" at line: ', self.tokens[self.token_index-2][2])
                quit()
        elif self.token[0] == 'LEFT_BRACKET_TK':
            self.token = self.get_token()
            (rtrue, rfalse) = self.condition()
            if self.token[0] != 'RIGHT_BRACKET_TK':
                print('ERROR: no closing bracket in a condition')
                quit()
            else:
                self.token = self.get_token()
        else:
            e1place = self.expression()
            relop = self.relational_operator()
            e2place = self.expression()

            rtrue = self.makelist(self.nextquad())
            self.genquad(relop, e1place, e2place, '_')
            rfalse = self.makelist(self.nextquad())
            self.genquad('jump', '_', '_', '_')
        return rtrue, rfalse

    def relational_operator(self):
        relop = None  # needed for correct syntax
        if self.token[0] == 'EQUAL_TK' or self.token[0] == 'SMALLEREQUAL_TK' or self.token[0] == 'LARGEREQUAL_TK' \
                or self.token[0] == 'LARGER_TK' or self.token[0] == 'SMALLER_TK' or self.token[0] == 'DIFFERENT_TK':
            relop = self.token[1]
            self.token = self.get_token()
        else:
            print('ERROR: relational operator expected at line: ', self.tokens[self.token_index-2][2])
            quit()
        return relop

    def elsepart(self):
        if self.token[0] == 'ELSE_TK':
            self.token = self.get_token()
            self.statements()

    def while_stat(self):
        if self.token[0] == 'WHILE_TK':
            bquad = self.nextquad()
            self.token = self.get_token()
            if self.token[0] == 'LEFT_PAREN_TK':
                self.token = self.get_token()
                (btrue, bfalse) = self.condition()
                if self.token[0] == 'RIGHT_PAREN_TK':
                    self.backpatch(btrue, self.nextquad())
                    self.token = self.get_token()
                    self.statements()
                    self.genquad('jump', '_', '_', str(bquad))
                    self.backpatch(bfalse, self.nextquad())
                else:
                    print('ERROR: closing parenthesis expected after conditions at line: ', self.token[2])
                    quit()
            else:
                print('ERROR: opening parenthesis expected after "while" statement at line: ',
                      self.tokens[self.token_index - 2][2])
                quit()

    def doublewhile_stat(self):  # removed from language
        if self.token[0] == 'DOUBLEWHILE_TK':
            self.token = self.get_token()
            if self.token[0] == 'LEFT_PAREN_TK':
                self.token = self.get_token()
                self.condition()
                if self.token[0] == 'RIGHT_PAREN_TK':
                    self.token = self.get_token()
                    self.statements()
                    if self.token[0] == 'ELSE_TK':
                        self.token = self.get_token()
                        self.statements()
                    else:
                        print('ERROR: "else" expected after statements in doublewhile at line: ',
                              self.tokens[self.token_index - 2][2])
                        quit()
                else:
                    print('ERROR: closing parenthesis expected after conditions at line: ', self.token[2])
                    quit()
            else:
                print('ERROR: opening parenthesis expected after "doublewhile" statement at line: ',
                      self.tokens[self.token_index - 2][2])
                quit()

    def loop_stat(self):  # removed from language
        if self.token[0] == 'LOOP_TK':
            xc = self.token[2]
            self.mark_exit = False
            self.loop_exit_counter += 1
            self.token = self.get_token()
            self.statements()
            self.loop_exit_counter -= 1
            if not self.mark_exit:
                print('WARNING: loop statement at line %s without "exit" will run infinite times!' % xc)

    def exit_stat(self):      # exit should only work inside loop statements (post deadline fix)
        if self.loop_exit_counter > 0:
            self.token = self.get_token()
            self.mark_exit = True
        else:
            print('ERROR: exit statement found outside loop statement'
                  ' at line: ', self.token[2])
            quit()


#########################################
# FORCASE INTERMEDIATE CODE EXPLANATION
# forcase {P1} (when:(condition): {P2} S1 {P3} )*
# default: S2  <-- runs in the end when all "when" conditions are false
#
# {P1}: fQuad = nextQuad()
# {P2}: backpatch(btrue, nextquad())
# {P3}: genquad('jump', '_', '_', fQuad)
#       backpatch(bfalse, nextquad())
#########################################
    def forcase_stat(self):
        self.token = self.get_token()
        fquad = self.nextquad()
        while self.token[0] == 'WHEN_TK':
            self.token = self.get_token()
            if self.token[0] == 'LEFT_PAREN_TK':
                self.token = self.get_token()
                (btrue, bfalse) = self.condition()
                if self.token[0] == 'RIGHT_PAREN_TK':
                    self.token = self.get_token()
                    if self.token[0] == 'COLON_TK':
                        self.backpatch(btrue, self.nextquad())
                        self.token = self.get_token()
                        self.statements()
                        self.genquad('jump', '_', '_', fquad)
                        self.backpatch(bfalse, self.nextquad())
                    else:
                        print('ERROR: colon expected in forcase statement at line: ',
                              self.tokens[self.token_index - 2][2])
                        quit()
                else:
                    print('ERROR: closing parenthesis expected after condition in forcase statement at line: ',
                          self.tokens[self.token_index - 2][2])
                    quit()
            else:
                print('ERROR: opening parenthesis expected after "when" in forcase statement at line: ',
                      self.tokens[self.token_index - 2][2])
                quit()
        if self.token[0] == 'DEFAULT_TK':
            self.token = self.get_token()
            if self.token[0] == 'COLON_TK':
                self.token = self.get_token()
                self.statements()
            else:
                print('ERROR: colon expected in forcase default statement at line: ',
                      self.tokens[self.token_index - 2][2])
                quit()
        else:
            print('ERROR: default statement expected in forcase statement at line: ',
                  self.tokens[self.token_index - 2][2])
            quit()

    def incase_stat(self):  # removed from language
        self.token = self.get_token()
        while self.token[0] == 'WHEN_TK':
            self.token = self.get_token()
            if self.token[0] == 'LEFT_PAREN_TK':
                self.token = self.get_token()
                self.condition()
                if self.token[0] == 'RIGHT_PAREN_TK':
                    self.token = self.get_token()
                    if self.token[0] == 'COLON_TK':
                        self.token = self.get_token()
                        self.statements()
                    else:
                        print('ERROR: colon expected in incase statement at line: ',
                              self.tokens[self.token_index - 2][2])
                        quit()
                else:
                    print('ERROR: closing parenthesis expected after condition in incase statement at line: ',
                          self.tokens[self.token_index - 2][2])
                    quit()
            else:
                print('ERROR: opening parenthesis expected after "when" in incase statement at line: ',
                      self.tokens[self.token_index - 2][2])
                quit()

    def call_stat(self):
        self.token = self.get_token()
        if self.token[0] == 'ID_TK':
            assign_v = self.token[1]
            self.search_entity(3, assign_v, subtype=2)
            self.token = self.get_token()
            self.actualpars(assign_v, is_call_statement=True)
            self.genquad('call', assign_v, '_', '_')
        else:
            print('ERROR: no name or wrong syntax in call statement at line: ',
                  self.tokens[self.token_index - 2][2])
            quit()

    def return_stat(self):
        if self.token[0] == 'RETURN_TK':
            if self.func_c == 0:
                print('ERROR: return found out of function at line: ', self.token[2])
                quit()
            elif self.func_c > 0:
                self.ret = 1
            self.token = self.get_token()
            eplace = self.expression()
            self.genquad('retv', eplace, '_', '_')

    def input_stat(self):
        self.token = self.get_token()
        if self.token[0] == 'LEFT_PAREN_TK':
            self.token = self.get_token()
            if self.token[0] == 'ID_TK':
                idplace = self.token[1]
                self.search_entity(0, idplace)
                self.token = self.get_token()
                if self.token[0] == 'RIGHT_PAREN_TK':
                    self.token = self.get_token()
                    self.genquad('inp', idplace, '_', '_', )
                else:
                    print('ERROR: closing parenthesis expected after "input" statement at line: ', self.token[2])
                    quit()
            else:
                print('ERROR: wrong/no input field at line: ', self.tokens[self.token_index - 2][2])
                quit()
        else:
            print('ERROR: opening parenthesis expected after "input" statement at line: ',
                  self.tokens[self.token_index - 2][2])
            quit()

    def print_stat(self):
        self.token = self.get_token()
        if self.token[0] == 'LEFT_PAREN_TK':
            self.token = self.get_token()
            eplace = self.expression()
            if self.token[0] == 'RIGHT_PAREN_TK':
                self.token = self.get_token()
                self.genquad('out', eplace, '_', '_',)
            else:
                print('ERROR: closing parenthesis expected after "print" statement at line: ', self.token[2])
                quit()
        else:
            print('ERROR: opening parenthesis expected after "print" statement at line: ',
                  self.tokens[self.token_index - 2][2])
            quit()

    def expression(self):
        os = self.optional_sign()
        if os:
            t1os = self.new_temp()
            t1temp = self.term()
            self.genquad('-', '0', t1temp, t1os)
            t1place = t1os
        else:
            t1place = self.term()
        while self.token[0] == 'PLUS_TK' or self.token[0] == 'MINUS_TK':
            oper = self.token[1]
            self.add_oper()
            t2place = self.term()
            w = self.new_temp()
            self.genquad(oper, t1place, t2place, w)
            t1place = w
        eplace = t1place
        return eplace

    def optional_sign(self):
        os = False
        if self.token[0] == 'PLUS_TK' or self.token[0] == 'MINUS_TK':
            if self.token[0] == 'MINUS_TK':
                os = True
            self.add_oper()
            return os

    def term(self):
        f1place = self.factor()
        while self.token[0] == 'TIMES_TK' or self.token[0] == 'OVER_TK':
            oper = self.token[1]
            self.mul_oper()
            f2place = self.factor()
            w = self.new_temp()
            self.genquad(oper, f1place, f2place, w)
            f1place = w
        tplace = f1place
        return tplace

    def factor(self):
        if self.token[0] == 'NUMBER':
            if int(self.token[1]) > 32767 or int(self.token[1]) < -32767:
                print('ERROR: numbers must be between -32767 and 32767 ,found: ',
                      self.token[1], ' at line: ', self.token[2])
                quit()
            number = self.token[1]
            self.token = self.get_token()
            fplace = number
        elif self.token[0] == 'LEFT_PAREN_TK':
            self.token = self.get_token()
            fplace = self.expression()
            if self.token[0] == 'RIGHT_PAREN_TK':
                self.token = self.get_token()
            else:
                print('ERROR: closing parenthesis missing in factor expression')
                quit()
        elif self.token[0] == 'ID_TK':
            idplace = self.token[1]
            self.token = self.get_token()
            x = self.idtail()
            if x != 'variable':
                fplace = x
            else:
                fplace = idplace
        else:
            fplace = None  # needed for python syntax
            print('ERROR: invalid or no factor in expression')
            quit()
        return fplace

    def idtail(self):
        if self.token[0] == 'LEFT_PAREN_TK':
            assign_v = self.tokens[self.token_index-2][1]
            self.search_entity(3, assign_v, subtype=1)
            self.actualpars(assign_v)
            w = self.new_temp()
            self.genquad('par', w, 'RET', '_')
            self.genquad('call', assign_v, '_', '_')
            return w
        else:  # it is a variable, not a function
            varname = self.tokens[self.token_index - 2][1]
            self.search_entity(0, varname)
            return 'variable'

    def mul_oper(self):
        if self.token[0] == 'TIMES_TK' or self.token[0] == 'OVER_TK':
            self.token = self.get_token()
        else:
            print('ERROR: no * or / operator')
            quit()

    def add_oper(self):
        if self.token[0] == 'PLUS_TK' or self.token[0] == 'MINUS_TK':
            self.token = self.get_token()
        else:
            print('ERROR: no + or - operator')
            quit()

    def actualpars(self, sub_name, is_call_statement=False):
        if self.token[0] == 'LEFT_PAREN_TK':
            self.token = self.get_token()
            self.actualparlist(sub_name, is_call_statement)
            if self.token[0] == 'RIGHT_PAREN_TK':
                self.token = self.get_token()
            else:
                print('ERROR: closing parenthesis missing after parameters at line: ',
                      self.tokens[self.token_index-2][2])
                quit()
        else:
            print('ERROR: opening parenthesis expected at line: ',
                  self.tokens[self.token_index - 2][2])
            quit()

    def actualparlist(self, sub_name, is_call_s):
        counter = 0
        if self.token[0] == 'RIGHT_PAREN_TK':  # actualparlist is empty: ()
            # check if actual arguments' size match typical arguments' size in call of function
            if is_call_s is False:
                fun1, fun2 = self.search_entity(3, sub_name, 1)
            else:
                fun1, fun2 = self.search_entity(3, sub_name, 2)
            if len(self.scopes[fun1][fun2][-2]) != 0:
                print('ERROR: Actual arguments size(0) does not match formal arguments size in call of function',
                      sub_name)
                quit()
            return
        self.actualparitem(counter, sub_name)
        counter += 1
        while self.token[0] == 'COMMA_TK':
            self.token = self.get_token()
            self.actualparitem(counter, sub_name)
            counter += 1

        # check if actual arguments' size match typical arguments' size in call of function
        if is_call_s is False:
            fun1, fun2 = self.search_entity(3, sub_name, 1)
        else:
            fun1, fun2 = self.search_entity(3, sub_name, 2)
        if len(self.scopes[fun1][fun2][-2]) != counter:
            print('ERROR: Actual arguments size does not match formal arguments size in call of function', sub_name)
            quit()

    def actualparitem(self, counter, s_name):
        if self.token[0] == 'IN_TK':
            self.token = self.get_token()
            explace = self.expression()
            self.search_entity(2, explace, parameter_type=1, sub_name=s_name, counter=counter)
            self.genquad('par', explace, 'CV', '_')
        elif self.token[0] == 'INOUT_TK':
            self.token = self.get_token()
            if self.token[0] == 'ID_TK':
                idplace = self.token[1]
                self.search_entity(2, idplace, parameter_type=2, sub_name=s_name, counter=counter)
                self.token = self.get_token()
                self.genquad('par', idplace, 'REF', '_')
            else:
                print('ERROR: wrong or no variable name after "in" or "inout" at line: ',
                      self.tokens[self.token_index-2][2])
                quit()
        else:
            print('ERROR: invalid passing type, in or inout expected at line: ', self.tokens[self.token_index - 1][2])
            quit()

    #############################
    # Intermediate code generator
    #############################
    def nextquad(self):
        return self.quad_count

    def genquad(self, op, x, y, z):
        self.quads.append([self.quad_count, op, x, y, z])
        self.quad_count += 1

    def new_temp(self):
        temp_var = 'T_' + str(self.counter_temp)
        self.counter_temp += 1
        self.declared_vars.append(temp_var)
        self.add_entity(1, temp_var)  # add temporary variable
        return temp_var

    # noinspection PyMethodMayBeStatic
    def emptylist(self):
        return []

    # noinspection PyMethodMayBeStatic
    def makelist(self, x):
        return [x]

    # noinspection PyMethodMayBeStatic
    def mergelist(self, l1, l2):
        return l1 + l2

    def backpatch(self, list_input, z):
        for i in list_input:
            for x in self.quads:
                if i == x[0] and x[4] == '_':
                    x[4] = str(z)

    #############################
    #       Symbol Table
    #############################
    def add_scope(self):
        self.nesting_level += 1
        self.offset.append(0)
        self.offset[self.nesting_level] = 12
        self.scopes.append([])

    def delete_scope(self):
        self.symbol_output.write('\n\nCurrent nesting level: %d' % self.nesting_level + '\n')
        if self.nesting_level >= 1:
            self.symbol_output.write('Current symbol table before scope delete:\n')
            for i in reversed(self.scopes):
                self.symbol_output.write('Scope #%d: %s' % (self.scopes.index(i), str(i)) + '\n\n')
            final_offset = self.offset[self.nesting_level]
            self.nesting_level -= 1
            self.scopes.pop()
            self.offset.pop()
            self.scopes[self.nesting_level][-1][-1] = final_offset  # framelength stored to function in previous
            # scope level

            self.recursion_fix()  # put framelength in recursive function call
        elif self.nesting_level == 0:
            final_offset = self.offset[self.nesting_level]
            self.symbol_output.write('Final/main symbol table: %s' % str(self.scopes) + '\n\n')
            self.nesting_level -= 1
            self.offset.pop()
            self.symbol_output.write('Final offset of program: %s' % str(final_offset) + '\n')

    def add_entity(self, entity_type, name='', subprogram_type='', start_quad=-1, par_mode=-1):

        if entity_type == 0:  # variable
            for i in self.scopes[self.nesting_level]:
                if i[0] == name:
                    print('ERROR: variable name: %s already exists!' % name)
                    quit()
            self.scopes[self.nesting_level].append([name, self.offset[self.nesting_level]])
            self.offset[self.nesting_level] += 4

        elif entity_type == 1:  # temporary variable (the same as variable)
            self.scopes[self.nesting_level].append([name, self.offset[self.nesting_level]])
            self.offset[self.nesting_level] += 4

        elif entity_type == 2:  # parameter   |  par_mode: in = 1    inout = 2
            self.scopes[self.nesting_level].append([name, par_mode, self.offset[self.nesting_level]])
            self.offset[self.nesting_level] += 4
            self.add_argument(par_mode)

        elif entity_type == 3:  # function or procedure
            arguments = []
            if name == self.tokens[1][1]:
                print('ERROR: same function/procedure name as main program!')
                quit()
            if subprogram_type == 'FUNCTION_TK':
                self.scopes[self.nesting_level].append([name, 1, start_quad, arguments, -1])
            else:
                self.scopes[self.nesting_level].append([name, 2, start_quad, arguments, -1])

            self.add_scope()

    def add_argument(self, parmode):
        self.scopes[self.nesting_level - 1][-1][-2].append(parmode)

    def find_starting_quad(self, funcname):
        for i in self.quads:
            if i[1] == 'begin_block' and i[2] == funcname:
                return i[0]+1

    def search_entity(self, entity_type, name, subtype=-1, parameter_type=-1, sub_name='', counter=-1):
        if entity_type == 0:  # variable search
            for i in reversed(range(self.nesting_level+1)):
                for j in range(len(self.scopes[i])):
                    if self.scopes[i][j][0] == name:
                        return i, j
            print('variable: %s not found (not declared/not visible)!' % name, 'at line',
                  self.tokens[self.token_index-1][2])
            quit()

        elif entity_type == 2:  # parameter search |  parameter_type: in = 1    inout = 2
            for j in self.scopes[self.nesting_level]:
                if j[0] == sub_name:
                    if j[-2][counter] != parameter_type:
                        print('ERROR: actual parameter type "%s" does not match formal parameter type '
                              '"%s" in call of function %s'
                              % (self.num_to_par(parameter_type), self.num_to_par(j[-2][counter]), sub_name))
                        quit()
            if counter < len(self.scopes[self.nesting_level - 1][-1][-2]):
                if self.nesting_level > 0 \
                        and self.scopes[self.nesting_level - 1][-1][-2][counter] != parameter_type\
                        and self.scopes[self.nesting_level - 1][-1][0] == sub_name:  # for recursion
                    print('ERROR: actual parameter type "%s" does not match formal parameter type "%s" in call of '
                          'function %s' % (self.num_to_par(parameter_type),
                                           (self.num_to_par(self.scopes[self.nesting_level - 1][-1][-2][counter])),
                                           sub_name))
                    quit()

            if parameter_type == 2:
                for i in reversed(range(self.nesting_level+1)):
                    for j in range(len(self.scopes[i])):
                        if self.scopes[i][j][0] == name:
                            return i, j
                print('ERROR: parameter: %s not found/not declared!' % name, 'at line',
                      self.tokens[self.token_index-1][2])
                quit()
            elif parameter_type == 1:  # expression stored in a temporary variable, no error checking needed
                for i in reversed(range(self.nesting_level+1)):
                    for j in range(len(self.scopes[i])):
                        if self.scopes[i][j][0] == name:
                            return i, j

        elif entity_type == 3:  # function/procedure search  | subtype: function = 1 , procedure = 2 , dontcare = 3
            if subtype == 1:
                for i in reversed(range(self.nesting_level+1)):
                    for j in range(len(self.scopes[i])):
                        if self.scopes[i][j][0] == name:
                            if self.scopes[i][j][1] == 1:
                                return i, j
                            else:
                                print('ERROR: %s is not a function! Only functions should be used in expressions.'
                                      % name)
                                quit()

                print('function: %s not found!' % name)
                quit()
            elif subtype == 2:
                for i in reversed(range(self.nesting_level+1)):
                    for j in range(len(self.scopes[i])):
                        if self.scopes[i][j][0] == name:
                            if self.scopes[i][j][1] == 2:
                                return i, j
                            else:
                                print('ERROR: %s is not a procedure! Only procedures '
                                      'should be used in "call" statements.' % name)
                                quit()

                print('function: %s not found!' % name)
                quit()
            elif subtype == 3:
                for i in reversed(range(self.nesting_level+1)):
                    for j in range(len(self.scopes[i])):
                        if self.scopes[i][j][0] == name:
                                return i, j
                print('function: %s not found!' % name)
                quit()

    # noinspection PyMethodMayBeStatic
    def num_to_par(self, param):
        if param == 1:
            return 'in'
        else:
            return 'inout'

    #############################
    #       Final Code
    #############################
    def gnvlcode(self, var):
        for it in self.scopes[self.nesting_level]:
            if it[0] == var:  # variable is local on the current nesting level
                return

        self.finalcode.append('lw $t0,-4($sp)')
        i, j = self.search_entity(0, var)
        for _ in reversed(range(i, self.nesting_level-1)):
            self.finalcode.append('lw $t0,-4($t0)')
        offset = self.scopes[i][j][-1]
        self.finalcode.append('addi $t0,$t0,-'+str(offset))

    def loadvr(self, v, r):
        x = None
        y = None
        for it in reversed(range(self.nesting_level + 1)):  # done here and not with search_entity to check constant
            for jt in range(len(self.scopes[it])):
                if self.scopes[it][jt][0] == v:
                    x, y = it, jt
        if x is None and y is None:  # constant doesnt exist in symbol table
            self.finalcode.append(("li $t" + str(r) + "," + str(v)))
            return

        i, j = self.search_entity(0, v)  # i = scope, j = entity index in the scope | 0=variable but works for par too
        offset = self.scopes[i][j][-1]
        if i == 0:  # main scope therefore global variable
            self.finalcode.append('lw $t' + str(r) + ',-' + str(offset) + '($s0)')

        elif i == self.nesting_level:
            if len(self.scopes[i][j]) == 3:  # parameter
                if self.scopes[i][j][1] == 1:  # in  (value)
                    self.finalcode.append('lw $t' + str(r) + ',-' + str(offset) + '($sp)')
                elif self.scopes[i][j][1] == 2:  # inout  (reference)
                    self.finalcode.append('lw $t0,-' + str(offset) + '($sp)')
                    self.finalcode.append('lw $t' + str(r) + ',($t0)')
                else:
                    print('loadvr flag error not valid parameter type check')
                    quit()
            elif len(self.scopes[i][j]) == 2:  # local variable
                self.finalcode.append('lw $t' + str(r) + ',-' + str(offset) + '($sp)')
            else:
                print('loadvr flag error function or procedure instead of variable')
                quit()
        elif i < self.nesting_level:  # this should always be true if the program gets here
            if len(self.scopes[i][j]) == 2:  # local variable
                self.gnvlcode(v)
                self.finalcode.append('lw $t' + str(r) + ',($t0)')
            elif len(self.scopes[i][j]) == 3:  # parameter
                if self.scopes[i][j][1] == 1:  # in  (value)
                    self.gnvlcode(v)
                    self.finalcode.append('lw $t' + str(r) + ',($t0)')
                elif self.scopes[i][j][1] == 2:  # inout  (reference)
                    self.gnvlcode(v)
                    self.finalcode.append('lw $t0,($t0)')
                    self.finalcode.append('lw $t' + str(r) + ',($t0)')
                else:
                    print('loadvr flag error not valid parameter type check')
                    quit()
            else:
                print('loadvr flag error function or procedure instead of variable')
                quit()

    def storerv(self, r, v):
        i, j = self.search_entity(0, v)  # i = scope, j = entity index in the scope
        offset = self.scopes[i][j][-1]
        if i == 0:  # main scope therefore global variable
            self.finalcode.append('sw $t' + str(r) + ',-' + str(offset) + '($s0)')

        elif i == self.nesting_level:
            if len(self.scopes[i][j]) == 3:  # parameter
                if self.scopes[i][j][1] == 1:  # in  (value)
                    self.finalcode.append('sw $t' + str(r) + ',-' + str(offset) + '($sp)')
                elif self.scopes[i][j][1] == 2:  # inout  (reference)
                    self.finalcode.append('lw $t0,-' + str(offset) + '($sp)')
                    self.finalcode.append('sw $t' + str(r) + ',($t0)')
                else:
                    print('storevr flag error not valid parameter type check')
                    quit()
            elif len(self.scopes[i][j]) == 2:  # local variable
                self.finalcode.append('sw $t' + str(r) + ',-' + str(offset) + '($sp)')
            else:
                print('loadvr flag error function or procedure instead of variable')
                quit()
        elif i < self.nesting_level:  # this should always be true if the program gets here
            if len(self.scopes[i][j]) == 2:  # local variable
                self.gnvlcode(v)
                self.finalcode.append('sw $t' + str(r) + ',($t0)')
            elif len(self.scopes[i][j]) == 3:  # parameter
                if self.scopes[i][j][1] == 1:  # in  (value)
                    self.gnvlcode(v)
                    self.finalcode.append('sw $t' + str(r) + ',($t0)')
                elif self.scopes[i][j][1] == 2:  # inout  (reference)
                    self.gnvlcode(v)
                    self.finalcode.append('lw $t0,($t0)')
                    self.finalcode.append('sw $t' + str(r) + ',($t0)')
                else:
                    print('storevr flag error not valid parameter type check')
                    quit()
            else:
                print('storevr flag error function or procedure instead of variable')
                quit()

    def final_code(self, program_name, is_main=0):  # is_main needed for j Lmain, program_name for starting quad
        sq = 0
        templist = []
        init_par_flag = 0
        starting_quad = self.find_starting_quad(program_name)  # find quad label
        for it in range(len(self.quads)):
            if self.quads[it][0] == starting_quad:
                sq = it  # starting quad index
                break

        if is_main == 1:
            self.finalcode[0] = 'j L' + str(starting_quad-1)

        for i in range(sq-1, len(self.quads)):
            # self.quads[i][1] is the keyword

            self.finalcode.append('L' + str(self.quads[i][0]) + ':')

            if is_main == 0 and self.quads[i][0] == starting_quad-1:
                self.finalcode.append('sw $ra,($sp)')

            if self.quads[i][0] == starting_quad-1 and is_main == 1 and self.quads[i][1] == 'begin_block':
                self.finalcode.append('addi $sp,$sp,' + str(self.offset[self.nesting_level]))
                self.finalcode.append('move $s0,$sp')

            elif self.quads[i][1] == 'jump':
                self.finalcode.append('b ' + 'L' + str(self.quads[i][4]))

            elif self.quads[i][1] in ['>', '<', '>=', '<=', '=', '<>']:
                self.loadvr(self.quads[i][2], 1)
                self.loadvr(self.quads[i][3], 2)
                self.finalcode.append(self.matchoper(self.quads[i][1]) + ' $t1,$t2,L' + str(self.quads[i][4]))

            elif self.quads[i][1] == ':=':
                self.loadvr(self.quads[i][2], 1)
                self.storerv(1, self.quads[i][4])

            elif self.quads[i][1] in ['-', '+', '/', '*']:
                self.loadvr(self.quads[i][2], 1)
                self.loadvr(self.quads[i][3], 2)
                self.finalcode.append(self.matchoper(self.quads[i][1]) + ' $t1,$t1,$t2')
                self.storerv(1, self.quads[i][4])

            elif self.quads[i][1] == 'out':
                self.loadvr(self.quads[i][2], 1)
                self.finalcode.append('li $v0,1')
                self.finalcode.append('move $a0,$t1')
                self.finalcode.append('syscall')

            elif self.quads[i][1] == 'inp':
                self.finalcode.append('li $v0,5')
                self.finalcode.append('syscall')
                self.finalcode.append('move $t1,$v0')
                self.storerv(1, self.quads[i][2])

            elif self.quads[i][1] == 'retv':
                self.loadvr(self.quads[i][2], 1)
                self.finalcode.append('lw $t0,-8($sp)')
                self.finalcode.append('sw $t1,($t0)')

            elif is_main == 0 and self.quads[i][1] == 'end_block':
                self.finalcode.append('lw $ra,($sp)')
                self.finalcode.append('jr $ra')

            elif self.quads[i][1] == 'par':
                if init_par_flag == 0:
                    templist.insert(0, ['addi $fp,$sp,', 'placeholder'])
                    init_par_flag = 1

                if self.quads[i][3] in ['CV', 'REF', 'RET']:
                    templist.append([self.quads[i], i])

            elif self.quads[i][1] == 'call':
                fi, fj = self.search_entity(3, self.quads[i][2], 3)
                framelength = self.scopes[fi][fj][-1]
                par_list = self.scopes[fi][fj][-2]
                par_list_len = len(par_list)
                squad = self.scopes[fi][fj][2]
                tm = 0

                if templist:
                    tm = 1
                    templist[0][1] = framelength

                    index = len(self.finalcode)-(len(templist)-1)
                    self.finalcode.insert(index, templist[0][0] + str(templist[0][1]))

                    for p in range(par_list_len):
                        beforelen = len(self.finalcode)
                        index = len(self.finalcode) - (len(templist)-p-1)
                        if templist[p+1][0][3] == 'CV':
                            self.loadvr(templist[p+1][0][2], 0)

                            afterlen = len(self.finalcode)
                            totallen = afterlen - beforelen
                            for _ in reversed(range(totallen)):
                                self.finalcode.insert(index, self.finalcode.pop())
                            index += totallen

                            self.finalcode.insert(index, 'sw $t0,-'+str(12+4*p)+'($fp)')

                        elif templist[p+1][0][3] == 'REF':
                            refi, refj = self.search_entity(0, templist[p+1][0][2])
                            offset1 = self.scopes[refi][refj][1]
                            if refi == self.nesting_level:  # same nesting level
                                if len(self.scopes[refi][refj]) == 3:  # parameter
                                    if self.scopes[refi][refj][1] == 1:  # value parameter
                                        self.finalcode.insert(index, 'addi $t0,$sp,-' + str(offset1))
                                        index += 1
                                        self.finalcode.insert(index, 'sw $t0,-'+str(12+4*p)+'($fp)')
                                    elif self.scopes[refi][refj][1] == 2:  # reference parameter
                                        self.finalcode.insert(index, 'lw $t0,-'+str(offset1)+'($sp)')
                                        index += 1
                                        self.finalcode.insert(index, 'sw $t0,-' + str(12 + 4 * p) + '($fp)')
                                elif len(self.scopes[refi][refj]) == 2:  # variable
                                    self.finalcode.insert(index, 'addi $t0,$sp,-' + str(offset1))
                                    index += 1
                                    self.finalcode.insert(index, 'sw $t0,-' + str(12 + 4 * p) + '($fp)')

                            elif refi < self.nesting_level:  # different nesting level
                                if len(self.scopes[refi][refj]) == 3:  # parameter
                                    if self.scopes[refi][refj][1] == 1:  # value parameter
                                        self.gnvlcode(self.scopes[refi][refj][0])

                                        afterlen = len(self.finalcode)
                                        totallen = afterlen - beforelen
                                        for _ in reversed(range(totallen)):
                                            self.finalcode.insert(index, self.finalcode.pop())
                                        index += totallen

                                        self.finalcode.insert(index, 'sw $t0,-'+str(12+4*p)+'($fp)')
                                    elif self.scopes[refi][refj][1] == 2:  # reference parameter
                                        self.gnvlcode(self.scopes[refi][refj][0])

                                        afterlen = len(self.finalcode)
                                        totallen = afterlen - beforelen
                                        for _ in reversed(range(totallen)):
                                            self.finalcode.insert(index, self.finalcode.pop())
                                        index += totallen

                                        self.finalcode.insert(index, 'lw $t0,($t0)')
                                        index += 1
                                        self.finalcode.insert(index, 'sw $t0,-' + str(12 + 4 * p) + '($fp)')
                                else:  # variable
                                    self.gnvlcode(self.scopes[refi][refj][0])

                                    afterlen = len(self.finalcode)
                                    totallen = afterlen - beforelen
                                    for _ in reversed(range(totallen)):
                                        self.finalcode.insert(index, self.finalcode.pop())
                                    index += totallen

                                    self.finalcode.insert(index, 'sw $t0,-' + str(12 + 4 * p) + '($fp)')

                    for t in range(1, len(templist)):
                        if templist[t][0][3] == 'RET':
                            ri, rj = self.search_entity(0, templist[t][0][2])
                            index = len(self.finalcode)-(len(templist)-t)
                            self.finalcode.insert(index, 'addi $t0,$sp,-' + str(self.scopes[ri][rj][1]))
                            index += 1
                            self.finalcode.insert(index, 'sw $t0,-8($fp)')

                templist[:] = []
                init_par_flag = 0

                # call function
                if tm == 0:
                    self.finalcode.append('addi $fp,$sp,' + str(framelength))

                if fi-1 == self.nesting_level:
                    self.finalcode.append('lw $t0,-4($sp)')
                    self.finalcode.append('sw $t0,-4($fp)')
                else:
                    self.finalcode.append('sw $sp,-4($fp)')

                self.finalcode.append('addi $sp,$sp,' + str(framelength))
                self.finalcode.append('jal L' + str(squad-1))
                self.finalcode.append('addi $sp,$sp,-' + str(framelength))

            elif self.quads[i][1] != 'begin_block':  # end of program
                self.finalcode.append('li $v0,10')  # needed at program end
                self.finalcode.append('syscall')  # needed at program end
                if self.quads[i][1] != 'halt':
                    print('This should not be printed when final code is completed: ',
                          self.quads[i])

    # noinspection PyMethodMayBeStatic
    def matchoper(self, op):
        oplist = ['>', '<', '>=', '<=', '=', '<>', '-', '+', '/', '*']
        if op == oplist[0]:
            return 'bgt'
        elif op == oplist[1]:
            return 'blt'
        elif op == oplist[2]:
            return 'bge'
        elif op == oplist[3]:
            return 'ble'
        elif op == oplist[4]:
            return 'beq'
        elif op == oplist[5]:
            return 'bne'

        elif op == oplist[6]:
            return 'sub'
        elif op == oplist[7]:
            return 'add'
        elif op == oplist[8]:
            return 'div'
        elif op == oplist[9]:
            return 'mul'

    def recursion_fix(self):
        framelen = self.scopes[self.nesting_level][-1][-1]
        start_quad = self.scopes[self.nesting_level][-1][2]
        for f in range(len(self.finalcode)):
            if self.finalcode[f][0:1] == 'L':
                if self.finalcode[f][1:-1] == str(start_quad):
                    for y in range(f, len(self.finalcode)):
                        if self.finalcode[y][-2:] == '-1':
                            self.finalcode[y] = self.finalcode[y][0:-2] + str(framelen)


#######################################
# Output final code to .asm file
#######################################
def out_to_asm_file(finalcode, infile_name):
    f = open(infile_name[0:-4]+'.asm', 'w+')
    for i in finalcode:
        f.write(str(i) + '\n')
    f.close()


#######################################
# Output intermediate code to .int file
#######################################
def out_to_int_file(quads, infile_name):
    f = open(infile_name[0:-4]+'.int', 'w+')
    for i in quads:
        f.write(str(i[0]) + ': ' + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(i[4]) + '\n')
    f.close()


#####################################
# Output intermediate code to .c file
#####################################
def out_to_c_file(quads, infile_name, startofmainprogram, declared_vars):
    f = open(infile_name[0:-4]+'.c', 'w+')

    f.write('#include <stdio.h>' + '\n')
    f.write('int main()'+'\n'+'{'+'\n')
    f.write(' int ')
    for i in range(0, (len(declared_vars)-1)):
        f.write(str(declared_vars[i])+',')
    f.write(str(declared_vars[-1])+';'+'\n')
    f.write(' ' + var_maker(quads[startofmainprogram-1][0]) + ':' + '\n')

    for i in quads[startofmainprogram:-1]:
        if i[1] == 'call':
            print('Warning: This file could not be converted to .c file properly because of function/procedure calls.')
            f.seek(0)
            f.truncate(0)
            f.write('THE PROGRAM COULD NOT BE CONVERTED TO C FILE PROPERLY BECAUSE OF FUNCTION/PROCEDURE CALLS. ')
            f.close()
            return
        counter = i[0]
        if i[1] == ':=':
            f.write(' '+var_maker(counter)+': '+str(i[4])+'='+str(i[2])+';' +
                    '    //' + str(i[0])+': '+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+'\n')

        elif i[1] == 'jump':
            f.write(' '+var_maker(counter)+': '+'goto '+str(var_maker(i[4]))+';' +
                    '    //'+str(i[0])+': '+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+'\n')

        elif i[1] in ['=', '<', '>', '<>', '<=', '>=']:
            if i[1] == '=':
                f.write(
                    ' ' + var_maker(counter) + ': ' + 'if (' + str(i[2]) + '==' + str(i[3]) + ') ' + 'goto ' + str(
                        var_maker(i[4])) +
                    ';' + '    //' + str(i[0]) + ': ' + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(
                        i[4]) + '\n')

            elif i[1] == '<>':
                f.write(
                    ' ' + var_maker(counter) + ': ' + 'if (' + str(i[2]) + '!=' + str(i[3]) + ') ' + 'goto ' + str(
                        var_maker(i[4])) +
                    ';' + '    //' + str(i[0]) + ': ' + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(
                        i[4]) + '\n')
            else:
                f.write(
                    ' ' + var_maker(counter) + ': ' + 'if (' + str(i[2]) + str(i[1]) + str(i[3]) + ') ' + 'goto ' + str(
                        var_maker(i[4])) +
                    ';' + '    //' + str(i[0]) + ': ' + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(
                        i[4]) + '\n')

        elif i[1] in ['+', '-', '*', '/']:
            f.write(' ' + var_maker(counter) + ': ' + str(i[4]) + '=' + str(i[2]) + str(i[1]) + str(i[3]) + ';' +
                    '    //' + str(i[0]) + ': ' + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(
                i[4]) + '\n')

        elif i[1] == 'out':
            f.write(' ' + var_maker(counter) + ': ' + 'printf("output ' + str(i[2]) + ': %d'+"\\"+'n",'
                    + str(i[2]) + ');' +
                    '    //' + str(i[0]) + ': ' + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(
                i[4]) + '\n')

        elif i[1] == 'inp':
            f.write(' ' + var_maker(counter) + ': ' + 'printf("' + str(i[2]) + ' input: ");\n '
                    + 'scanf("%d",&' + str(i[2])
                    + ');' + '    //' + str(i[0]) + ': ' + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(
                i[4]) + '\n')

        else:
            f.write(' '+var_maker(counter)+': ' + '{}' + '\n')

    f.write('}'+'\n')
    f.close()


def var_maker(counter):  # -99 to match with slides examples
    return 'L_'+str(int(counter)-99)


#############################
#           Main
#############################
def main():

    #########
    # RUN INSTRUCTIONS: python compilerMainV4.py <somefile.min>
    #########

    run_instructions = 'RUN INSTRUCTIONS:  python compilerMainV4.py <somefile.min>'

    infile = None
    content = None
    file = ''
    global in_name

    # noinspection PyBroadException
    try:
        infile = sys.argv[1]
    except Exception:
        print('ERROR: no file input!\n', run_instructions)
        quit()

    # noinspection PyBroadException
    try:
        if not sys.argv[2] == '':
            print('ERROR: more than one file input, please input only one file!\n', run_instructions)
            quit()
    except Exception:
        pass

    filepath = pathlib.Path(infile)
    if not filepath.exists():
        print('ERROR: file does not exist!\n', run_instructions)
        quit()

    if infile.endswith('.min'):
        with open(infile, 'r') as file:
            content = file.read()
    else:
        print('ERROR: file extension is not .min\n', run_instructions)
        quit()

    file.close()

    in_name = infile[0:-4]

    # Parser
    parse_syntax = Parse(content)
    parse_syntax.parse()

    out_to_int_file(parse_syntax.quads, infile)

    out_to_c_file(parse_syntax.quads, infile, parse_syntax.startofmainprogram, parse_syntax.declared_vars)

    out_to_asm_file(parse_syntax.finalcode, infile)


main()
