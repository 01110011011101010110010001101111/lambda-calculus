from lang import *

def test_ch_3_1():
    # if false then 0 else 1;
    cond_result = evaluate(Conditional(ConstFalse(), ConstZero(), Successor(ConstZero())))
    assert isinstance(cond_result, NumericValue)
    assert cond_result.num == 1

    # iszero (pred (succ 0));
    assert isinstance(evaluate(ZeroTest(Predecessor(Successor(ConstZero())))), ConstTrue)

def test_major():
    # with a variable
    # x := 5
    result = evaluate(Variable("a"))
    assert isinstance(result, Variable)
    assert result.name == "a"

    result = evaluate(Evaluation(Lambda("x", (Variable("x"))), ConstZero()))

    print(result)

test_major()

# TODO: format this better, etc.
# test_ch_3_1()

