"""
STEP1: read + make sure i understand!
STEP2: write test cases!
STEP3: add remaining T/F/etc, with tests!
STEP4: TYPECHECK! (try to get an exhaustiveness test to work)
(STRETCH) STEP5: TRY TO COMPILE DOWN TO PYTHON

 STEP6: copy dataclass
"""

from abc import ABC
from dataclasses import dataclass

class Expr(ABC):
    pass

@dataclass
class ConstTrue(Expr):
    pass

@dataclass
class ConstFalse(Expr):
    pass

@dataclass
class Conditional(Expr):
    cond: Expr
    t_branch: Expr
    f_branch: Expr

@dataclass 
class Lambda(Expr):
    arg: str
    body: Expr

@dataclass
class Variable(Expr):
    name: str

@dataclass
class Evaluation(Expr):
    f: Expr
    a: Expr

# free variables
def fv(expr: Expr) -> set[str]:
    match expr:
        case Variable(name):
            return {name}
        case Lambda(arg, body):
            return fv(body) - arg
        case Evaluation(f, a):
            return fv(f) | fv(a)

# page 72
def evaluate(expr: Expr) -> Expr:
    match expr:
        case Variable(name):
            return expr
        case Lambda(arg, body):
            return Lambda(arg, evaluate(body))
        case Evaluation(f, a):
            fp = evaluate(f)
            if isinstance(fp, Lambda):
                t2p = evaluate(a)

                # both function and arg are lambda
                if isinstance(t2p, Lambda):
                    return evaluate(substitute(fp.arg, t2p, fp.body))
                else:
                    return Evaluation(fp, t2p)
            else:
                return Evaluation(fp, a)

# page 71, section 5.3.5
def substitute(x: str, s: Expr, expr: Expr) -> Expr:
    match expr:
        case Variable(name) if x == name:
            return s
        case Variable(name):
            return expr
        case Lambda(arg, body) if arg != x and arg not in fv(s):
            return Lambda(y, substitute(x, s, body))
        case Evaluation(f, a):
            return Evaluation(substitute(x, s, f), substitute(x, s, a))
        case _:
            return expr
