# GLOBAL SCOPE VARIBLES

IGWORDS = [] #ignored words
USQUESTION = input("Describe your problem: ")

# FUNCTIONS

def ask_question():
    USQUESTION

def ai(user_input: str):
    """
    This function take the question of a user literally represented as
    a string and returns the list of key words based on which our program can define
    what kind of problem we should solve.
    """
    pass

def get_keywords(user_input):
    key_words = ai(user_input)
    return key_words


insurance_keywords = {"insurance", "insurances", "insured", "insure"}
insurance_problems = {"I want to insure"}
dic_insurance = {words_ins_1: problems_ins_1}

loan_keywords = {"loan", "loans", "lease"}
loan_problems = {"I want to loan"}
dic_loan = {words_loan_1: problems_loan_1}

dic_problems = {insurance_keywords: dic_insurance, loan_keywords: dic_loans}

def determine_problem(key_words):
    for word in key_words:    
        for key in dic_problems:
            if word in key:
                keywords_type_problem = key
    return key


def find_solution(problem):
    solution = None
    file = "DB_PROBLEMS_SOLUTIONS.txt"
    open(file, "r")
    for row in file:
        known_problem = row[0]
        if problem == known_problem  in row:
            solution = row[1]
            break
    return solution


foundData = None
lostData = None

BigBoyData = {{"k1_1", "k1_2", "k1_3"}: foundData, "other": lostData}

problemKeys = [{"k1_2", "k1_3"}, {"k2_3"}, {"k3_2"}]

def algorithm():

    while type(BigBoyData) == dict:
        something = list(BigBoyData.keys())
        something = something.remove("other")

        if something[0] & problemKeys[0] != set():
            BigBoyData = BigBoyData[something[0]]
        else:
            BigBoyData = BigBoyData["other"]

    if len(problemKeys) == 0:
        return BigBoyData
    else: 
        BigBoyData = extend_tree(BigBoyData, problemKeys)

def extend_tree():
    None