"""
mathsolver, a parser which solves math equations I made to spite my Dad who didn't think I could do it.
Copyright (C) 2020   Nate Choe

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

print("""<program>  Copyright (C) <year>  <name of author>
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; see license.txt for details.""")

equation = "".join(input().split())

parenthesis = 0
operator = 1
number = 2

class Section:
    def __init__(self, t, v):
        self.type = t;
        self.value = v;

def solve(equation):
    parenthesis_count = 0
    sections = []
    for i in range(0, len(equation)):
        if equation[i] == '(':
            parenthesis_count += 1
        if equation[i] == ')':
            parenthesis_count -= 1
        if parenthesis_count != 0:
            if len(sections) == 0 or sections[-1].type != parenthesis:
                sections.append(Section(parenthesis, ""))
            sections[-1].value += equation[i]
        elif equation[i] in ('+', '-', '*', '/', '^'):
            sections.append(Section(operator, equation[i]))
        elif equation[i].isdigit():
            if len(sections) == 0 or sections[-1].type != number:
                sections.append(Section(number, ""))
            sections[-1].value += equation[i]

    #At this point the equation has been parsed and converted into Sections.

    for i in range(0, len(sections)):
        if sections[i].type == parenthesis:
            sections[i] = solve(sections[i].value[1:])
            #If it's a parenthesis, recursively solve the parenthesis. Note, solve returns a Section with a number type.

    operations = (('^'), ('*', '/'), ('+', '-'))
    for operation_group in operations:
        i = 0
        while i < len(sections):
            if sections[i].type == operator and sections[i].value in operation_group:
                operation = sections[i].value
                if operation == '^':
                    sections[i-1].value = str(float(sections[i-1].value)**float(sections[i+1].value))
                if operation == '*':
                    sections[i-1].value = str(float(sections[i-1].value)*float(sections[i+1].value))
                if operation == '/':
                    sections[i-1].value = str(float(sections[i-1].value)/float(sections[i+1].value))
                if operation == '+':
                    sections[i-1].value = str(float(sections[i-1].value)+float(sections[i+1].value))
                if operation == '-':
                    sections[i-1].value = str(float(sections[i-1].value)-float(sections[i+1].value))
                
                sections.remove(sections[i+1])
                sections.remove(sections[i])
                i -= 1
            i += 1
    return sections[0]

print(solve(equation).value)
