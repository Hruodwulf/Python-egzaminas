# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos:

from Uzduotis_5.modules.mathematics.addition import add
from Uzduotis_5.modules.mathematics.division import divide
from Uzduotis_5.modules.mathematics.multiplication import multiply
from Uzduotis_5.modules.mathematics.subtraction import subtract
import Uzduotis_5.modules.num.ints as integers

# Kitų failų ir žemiau esančio kodo nekeiskite

a = add(integers.one, integers.four)
b = divide(integers.four, integers.two)
c = subtract(integers.three, integers.two)
d = multiply(integers.five, integers.two)

print(a);
print(b);
print(c);
print(d);

