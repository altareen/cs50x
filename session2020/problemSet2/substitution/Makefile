###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jul 03, 2020
# Compilation:  make substitution
#
# This Makefile compiles the substitution.c program.
#
##

substitution: substitution.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o substitution substitution.c

clean:
	rm -f *.o a.out core substitution log.txt

