# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "No"
    answers["(b)"] = "No"
    answers["(c)"] = "Yes"
    answers["(d)"] = "Yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = " There are instances where a person can satisfy the conditions of more than one rule. For example, a person who is a single, low-income homeowner would satisfy both rules 1 and 2, leading to a conflict in the predicted outcome."
    answers["(b) explain"] = "There are possible combinations of attribute values that are not covered by the given rules. For instance, the rule set does not include a rule for a person who is a high-income, employed non-homeowner and also non-home owner divorced with medium income and not employed"
    answers["(c) explain"] = "ordering is needed for this set of rules because they are not mutually exclusive. When multiple rules could apply to a single case, the order in which the rules are evaluated can affect the outcome. "
    answers["(d) explain"] = "For this rule set, a default class is required. There will be situations that are not covered by any of the rules since the set is not all-inclusive (as section b explains). To categorize these instances, a default class must be supplied in certain situations.For instance, depending on the domain expertise or the intended classifier behavior, No or Yes might be the default class if none of the conditions are met for a particular instance."

    return answers



# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():# recheck the question
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "Yes"# recheck

    # explain-string: explanation in english prose
    answers["(a) example"] = "It is impossible for a vertebrate to have both warm and cold blood.A vertebrate is not able to live in the water or the air.A vertebrate that gives birth does not meet any of the requirements in R1, R2, or R4.Therefore, no vertebrate can simultaneously meet the requirements of more than one rule. It is true that the rules are mutually exclusive."
    answers["(b) example"] = "The rule set is not comprehensive in light of these inadequacies. In order for it to be considered comprehensive, further rules would have to be included to cover these situations and guarantee that every vertebrate could be categorized using the set of principles. Amphibian regulations and any other unique situations that don't meet the established guidelines are covered by this."
    answers["(c) example"] = "The ordering may become significant if the present rules were altered such that they are no longer mutually exclusive, or if new rules were introduced to fill in the gaps and make the set exhaustive. To ensure proper categorization in such circumstances, rules would have to be arranged according to the conditions' precedence or in some other logical order."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = "True"
    answers["(b)"] = "True"
    answers["(c)"] = "False"
    answers["(d)"] = "True"#recheck

    # explain_string: explanation in english prose
    answers["(a) explain"] = "Using the calculus chain rule, the gradients of weights at the kth layer are used to calculate the gradients of weights at the (k+1)th layer in the back-propagation method."
    answers["(b) explain"] = "Applying an ANN model to a test instance and computing the activations at nodes in the (k+1)th layer using the activations at nodes in the kth layer and the related weights is known as the forward propagation phase."
    answers["(c) explain"] = "Even if the training mistakes might not always disappear to zero, the vanishing gradient problem describes the state in which the gradients of the loss function with respect to the weights become extremely tiny, making it challenging for the model to learn during training."
    answers["(d) explain"] = "The gradients of the loss with respect to the weights at all layers will be zero if the ANN model correctly classifies every training instance at a certain backpropagation algorithm iteration. This is because the gradients, which show how the loss changes in relation to the weights, will be 0 and the loss function will be reduced."
    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = "0.65"
    answers["(a) P(X_2=1)"] = "0.41"
    answers["(a) P(X_1=1,X_2=1)"] = "0.28"

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+"
    answers["(d) Row 2"] = "-"
    answers["(d) Row 3"] = "-"
    answers["(d) Row 4"] = "-"

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25# recheck

    return answers
# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = "1"
    answers["(b) K"] = "5"#recheck

    # explain_string
    answers["(a) explain"] = "a smaller K like 1 should work well due to the clear separation between classes."
    answers["(b) explain"] = "K=5 provides a balance that reduces variance without noticeably raising bias, making it appropriate for datasets with some degree of overlap or noise."

 
    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = None
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.857
    answers["(b) P(R|+)"] = 0.192#recheck
    answers["(b) P(R|-)"] = 0.032#recheck

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "because the class label + maximises postirior probability with -."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "For class = +, 0.24(product of the probabilities) not equal to 0.2(joint probability) , proving that A and B are not conditionally independent. The equivalence must exist for variables to be conditionally independent given the class."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
