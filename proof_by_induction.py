from sympy import *
x, y, z, k, n = symbols('x y z k n')
init_printing(use_unicode=True)

## este metodo verifica si el caso base es valido
# formula: string con la formula a probar
# valid_from_n: entero que va a ser utilizado para evaluar la formula
# base_case: entero que se espera sea el resultado de la formula
def verify_base_case(formula, valid_from_n, base_case):
    computed_base_case = (sympify(formula)).subs(n, valid_from_n)
    base_case_satisfied = computed_base_case == base_case
    return base_case_satisfied

## este metodo expande la formula S(k) + siguiente termino
# formula: string con la formula a probar
# next_expression: string con el siguiente numero en la sucesion (k+1) a probar
def expand_induction_hypothesis_k_plus_1(formula, next_expression):
    # inductive hypothesis
    inductive_step = formula.replace('n', 'k') + '+' + next_expression.replace('n', 'k')
    return expand(inductive_step)

## este metodo expande la formula S(k+1)
# formula: string con la formula a probar
def expand_formula_k_plus_1(formula):
    return expand(formula.replace('n', '(k+1)'))

## este metodo prueba la formula de la serie aritmetica
# formula: string con la formula a probar
# valid_from_n: entero que va a ser utilizado para evaluar la formula
# base_case: entero que se espera sea el resultado de la formula
# next_expression: string con el siguiente numero en la sucesion
def prove_arithmetic_series_formula(formula, valid_from_n, base_case, next_expression):
    # verify base case
    base_case_satisfied = verify_base_case(formula, valid_from_n, base_case)

    # Next term S(k+1) from the inductive hypothesis
    inductive_hypothesis = expand_induction_hypothesis_k_plus_1(formula, next_expression)

    # Next term S(k+1) directly from the formula
    formula_next_term = expand_formula_k_plus_1(formula)

    # If the inductive hypothesis matches the formula for the next term
    # then we have proved the formula
    return {
        'base_case_satisfied': base_case_satisfied,
        'inductive_hypothesis': inductive_hypothesis,
        'formula_next_term': formula_next_term,
        'proved': base_case_satisfied and inductive_hypothesis == formula_next_term
    }

# Sum of all even numbers
INPUT_FORMULA = '2**n'
INPUT_VALID_FROM_N = 0
INPUT_BASE_CASE = 1
INPUT_NEXT_STEP = '2**n'

print (prove_arithmetic_series_formula(
    INPUT_FORMULA,
    INPUT_VALID_FROM_N,
    INPUT_BASE_CASE,
    INPUT_NEXT_STEP
    ))
