import pygame, sys
import pickle

Questions = {
    'Who is the mother of programming?': {{'Ada Lovelace','Grace Hopper','Kim Gordon','Wendy Carlos'},1},
    'Who created the Analytical Engine?': {{'Alan Turing','Charles Babbage','Steve Jobs','Ada Lovelace'},2},
    'What was the name of the first digital computer?': {{'ABC','ENIVAC','UNIVAC','Indigo'},1},
    'Who came up with the idea of a machine that could compute anything which is computable?': {{'Charles Babbage','Ada Lovelace','Alan Turing','Albert Einstein'},1},
    'What is the lowest level programming language?': {{'Assembly','C','Java','FORTRAN'},1},
    'What was the first commercial computer?': {{'ABC','ENIVAC','Xerox Alto', 'UNIVAC'}, 4},
    'Who developed the concept of Machine Independent Programming?': {{'Grace Hopper','Ada Lovelace','Dennis Ritiche','Alan Turing'},1},
    'When was the internet created?': {{'1960s','1970s','1980s','1990s'}, 1},
    'Who created the computer chip and was awarded with a Nobel Prize in Physics?': {{'Alan Turing','Bill Gates','Jack Kilby','Ken Thompson'},3},
    'Where was UNIX developed?': {{'Bell Laboratories','Xerox Laboratories','BBC Laboratories','Microsoft'},1},
    'What was the first portable computer?': {{'IBM 5100','Osborne 1','IBN 5100','Macintosh'},1},
    'Who created the C programming language?': {{'Ken Thompson','Grace Hopper','Dennis Ritchie','Steve Jobs'}, 3},
    'What company created the first Object Oriented Programming language?': {{'Apple,','Bell','Sun Microsystems', 'Xerox'}, 4},
    'First personal computer with a graphical user interface?': {{'Xerox Alto','Macintosh','IBN 5100','Indigo'}, 1},
    'When was the first dot com domain registered?': {{'1993','1995','1988', '1985'}, 4},
    'What was the name of the AI who beat Grandmasters in chess?': {{'ChessMind','Open King','Deep Blue','Master AI'},3}
}

pickle.dump(Questions, open('q.p','w.b'))