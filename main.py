import voidstone_functions

def main():
    user_input = ask_question()
    keywords = get_keywords(user_input)
    problem = determine_problem(keywords)
    solution = find_solution(problem)
    return solution

main()