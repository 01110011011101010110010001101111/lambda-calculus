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
class ConstZero(Expr):
    pass

@dataclass
class Successor(Expr):
    num: Expr

@dataclass
class Predecessor(Expr):
    num: Expr

@dataclass
class ZeroTest(Expr):
    num: Expr

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

@dataclass
class NumericValue(Expr):
    num: int

# page 72
def evaluate(expr: Expr) -> Expr:
    assert isinstance(expr, Expr)

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
        case ConstTrue() | ConstFalse() | ConstZero():
            return expr
        # page 34
        case Conditional(cond, t_branch, f_branch):
            # reduce the conditional if possible
            eval_cond = evaluate(cond)
            if isinstance(eval_cond, ConstTrue):
                return evaluate(t_branch)
            elif isinstance(eval_cond, ConstFalse):
                return evaluate(f_branch)
            else:
                # NOTE: not 1-to-1 with the book, doing unnecessary evals of the t_branch and f_branch
                # return Conditional(eval_cond, evaluate(t_branch), evaluate(f_branch))
                return Conditional(eval_cond, t_branch, f_branch)
        # page 41
        case Predecessor(num):
            match num:
                # pred 0 -> 0
                case ConstZero():
                    return ConstZero()
                # pred ( succ (nv_1) ) -> nv1
                case Successor(nv1) if isinstance(nv1, NumericValue) or isinstance(nv1, ConstZero):
                    return nv1
            # t1 -> t1' ==> pred t1 -> pred t1'
            eval_num = evaluate(num)
            return (Predecessor(eval_num))
        # page 41
        case Successor(num):
            eval_num = evaluate(num)
            return Successor(eval_num)
        case ZeroTest(num):
            match num:
                case ConstZero():
                    return ConstTrue()
                case Successor(nv1):
                    return ConstFalse()
                case _:
                    nump = evaluate(num)
                    return evaluate(ZeroTest(nump))
        case _:
            raise NotImplementedError

# free variables
def fv(expr: Expr) -> set[str]:
    assert isinstance(expr, Expr)

    match expr:
        # main terms
        case Variable(name):
            return {name}
        case Lambda(arg, body):
            return fv(body) - arg
        case Evaluation(f, a):
            return fv(f) | fv(a)

        # TODO -- makes sense but verify
        case Conditional(cond, t_branch, f_branch):
            return fv(cond) | fv(t_branch) | fv(f_branch)
        case ConstTrue() | ConstFalse() | ConstZero():
            return set()
        case NumericValue() | ZeroTest() | Successor() | Predecessor():
            return set()

        case _:
            raise NotImplementedError

# page 71, section 5.3.5
def substitute(x: str, s: Expr, expr: Expr) -> Expr:
    assert type(x) == str
    assert isinstance(s, Expr)
    assert isinstance(expr, Expr)

    match expr:
        case Variable(name) if x == name:
            return s
        case Variable(name):
            return expr
        case Lambda(arg, body) if arg != x and arg not in fv(s):
            return Lambda(y, substitute(x, s, body))
        case Lambda(arg, body):
            return expr
        case Evaluation(f, a):
            return Evaluation(substitute(x, s, f), substitute(x, s, a))

        # TODO -- makes sense but verify
        case Conditional(cond, t_branch, f_branch):
            return expr
        case ConstTrue() | ConstFalse() | ConstZero():
            return expr
        case NumericValue() | ZeroTest() | Successor() | Predecessor():
            return expr

        case _:
            raise NotImplementedError

