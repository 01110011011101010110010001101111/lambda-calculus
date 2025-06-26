from lang import *

def test_boolean():
    # if false then 0 else 1;
    cond_result = evaluate(Conditional(ConstFalse(), ConstZero(), Successor(ConstZero())))
    assert isinstance(cond_result, Successor)

    # iszero (pred (succ 0));
    assert isinstance(evaluate(ZeroTest(Predecessor(Successor(ConstZero())))), ConstTrue)

    assert isinstance(evaluate(Conditional(ConstTrue(), ConstTrue(), ConstFalse())), ConstTrue)

    assert isinstance(evaluate(Conditional(ZeroTest(ConstZero()), ConstTrue(), ConstFalse())), ConstTrue)

    assert isinstance(evaluate(Predecessor(ConstZero())), ConstZero)

    result = Predecessor(Variable("x"))
    assert isinstance(result, Predecessor)
    assert isinstance(result.num, Variable)
    assert result.num.name == "x"

def test_major():
    result = evaluate(Evaluation(Lambda("x", Variable("x")), Lambda("y", Variable("y"))))
    assert isinstance(result, Lambda)
    assert result.arg == "y"
    assert isinstance(result.body, Variable)
    assert result.body.name == "y"


    result = evaluate(Evaluation(Evaluation(Lambda("x", Variable("x")), Lambda("y", Variable("y"))), Lambda("z", Variable("z"))))
    assert isinstance(result, Lambda)
    assert result.arg == "z"
    assert isinstance(result.body, Variable)
    assert result.body.name == "z"

    result = evaluate(
            Evaluation(
                Evaluation(
                    Lambda("w", Variable("w")), 
                    Lambda("x", Variable("x"))), 
                Evaluation(
                    Lambda("y", Variable("y")), 
                    Lambda("z", Variable("z")))))
    assert isinstance(result, Lambda)
    assert result.arg == "z"
    assert isinstance(result.body, Variable)
    assert result.body.name == "z"

    result = evaluate(Evaluation(Variable("x"), Variable("y")))
    assert isinstance(result, Evaluation)
    assert isinstance(result.f, Variable)
    assert isinstance(result.a, Variable)
    assert result.f.name == "x"
    assert result.a.name == "y"

    result = evaluate(Evaluation(Lambda("x", Variable("x")), Variable("y")))
    assert isinstance(result, Evaluation)
    assert isinstance(result.f, Lambda)
    assert isinstance(result.a, Variable)
    assert isinstance(result.f.body, Variable)
    assert result.f.arg == "x"
    assert result.f.body.name == "x"
    assert result.a.name == "y"


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


# # TODO: format this better, etc.
test_boolean()
test_major()

