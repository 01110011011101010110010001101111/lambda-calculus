from lang import *

def test_ch_3_1():
    # if false then 0 else 1;
    cond_result = evaluate(Conditional(ConstFalse(), ConstZero(), Successor(ConstZero())))
    assert isinstance(cond_result, Successor)
    # assert cond_result.num == 1

    # print(evaluate(ZeroTest(Predecessor(Successor(ConstZero())))))
    # iszero (pred (succ 0));
    assert isinstance(evaluate(ZeroTest(Predecessor(Successor(ConstZero())))), ConstTrue)

def test_major():
    # with a variable
    # x := 5
    # result = evaluate(Variable("a"))
    # assert isinstance(result, Variable)
    # assert result.name == "a"

    # result = evaluate(Evaluation(Lambda("x", (Variable("x"))), ConstZero()))

    # print(result)

    # page 72

    # (λx.t12) v2 -→ [x , v2]t12
    # result = evaluate(
    #             Evaluation(
    #                 Lambda(),
    #             )
    #          )


    # result = evaluate(Evaluation(
    #                    Lambda("l", 
    #                           Lambda("m", 
    #                                  Evaluation(Variable("l"), Variable("m"))
    #                                  ))
    #                   , ConstTrue())
    #                   )
    # print(result)


# TODO: format this better, etc.
test_ch_3_1()
test_major()

