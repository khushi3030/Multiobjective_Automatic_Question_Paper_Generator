import ast
import astor
import random
import sys
import pandas as pd
from io import StringIO




df=pd.read_csv('question_final.csv')
import pandas as pd
df.dropna(inplace=True)  
df.drop_duplicates(inplace=True) 
import pandas as pd
#column_data_list = df['column_name'].tolist()
#print(column_data_list)
col_data=df['Question']
print(col_data)

original_code =[ #" sum=0\n for num in range(1, 11, 2): \n sum += num\nprint('Sum of odd numbers:', sum)",
"sentence='jai' \n print(sentence+sentence)"








                #"word = 'Python Programming'\nn = len(word)\nword1 = word.upper()\nword2 = word.lower()\nconverted_word = ''\nfor i in range(n):\n if i % 2 == 0:\n   converted_word += word2[i]\n else:\n   converted_word += word1[i]\nprint(converted_word)" ]
                #"num = 12321\ntemp = num\nreverse = 0\nwhile temp > 0:\n    remainder = temp % 10\n    reverse = (reverse * 10) + remainder\n    temp = temp // 10\nif num == reverse:\n  print('Palindrome')\nelse:\n  print('Not Palindrome')"]
                #"text='goat'\nprint(text)"
             #"d = {1 : 'A', 2 : 'B', 3 : 'C'}\nd.clear()\nprint(d)"]# Pool of meaningful quoted values
             ]

# Define a function for the fuzzy logic code transformation
def modify_code(original_code):
    # Pool of meaningful quoted values
    quoted_values = {
        1: ['Abstraction','Array','Binary','Variable' 'Bug','Database','Recursion','functions','Framework','Loop','Syntax','Algorithm','Git','Variable','Function','Debugging', 'reusability','programming', 'efficiency','python', 'java', 'code', 'Encapsulation', 'Inheritance','Class','Object','Hybrid ','Multilevel','Private','Public','Protected','Code'],

        2: ['Hello World','Database query','Bug fixing','Git collaboration','Class inheritance','error free','Function abstraction','Code efficiently','Debug systematically','Algorithm optimization','Variable assignment','Loop iteration','Array manipulation','Class inheritance','Database query','Compile successfully','Framework development','Recursion implementation',

'Binary representation', 'Good programming','code changes','Pair programming', 'problem-solving','Refactoring code','Print page', 'Save file', 'Neural Network','Machine Learning','R Langugae','Data Science','SQL Query','Delete Tab','Computer Science','VsCode Editor','Artifcial Intelligence','Numpy Library','Library Pandas','Scikit learn'],

        3: ['Object Oriented Programming','Application Programming Interface','Integrated Development Environment','Analyze algorithm complexity ','Git aids collaboration','Solve LeetCode challenges','OOP improves code ','Fixed a  error', 'Python powers web', 'Python programming language','Debugging is tricky', 'Cybersecurity protects networks', 'Coding requires practice','Machine Learning funny','ChatGpt fired Sam','ChaGpt wants Sam back',' Implemented  binary search '],

        4: ['I love programming', 'coding questions are to be practised for Interviews ', 'I love doing programms in python ', 'I love doing programs in c', 'I love doing programs in java', 'There is funda learnt in c called Encapsulation', 'Inheritance is a very important concept in c','Hello World is the first program', 'I know really good programming', 'Print page', 'Save file', 'Neural Network is a part of deep learning','Object Oriented Programming is very crucial part in c', 'Python powers web', 'Python programming language is the base of AI ', 'Cybersecurity protects networks', 'Coding requires a lot of practice.']
    }

    # Define fuzzy logic rules for variable name changes with randomness
   

    def generate_new_variable_name():
        max_attempts = 10  # Set a reasonable maximum number of attempts
        for _ in range(max_attempts):
            new_name = f'var_{random.randint(1, 10)}'
            if new_name not in variable_names:
                variable_names.append(new_name)
                return new_name

    # If no unique name is found after max_attempts, raise an exception or return a default value
        raise ValueError("Unable to generate a unique variable name.")

    
    # Define fuzzy logic rules for numeric value changes with randomness
    def change_numeric_value(value, is_slice=False):
        new_value = value

        while new_value == value:
            if isinstance(value, int):
                new_value = random.randint(1, 10)
            elif isinstance(value, float):
                new_value = random.uniform(1.0, 10.0)

        if is_slice:
            # Ensure that the first number is smaller than the second number for slice indices
            second_value = random.randint(1, 10)
            new_value = min(new_value, second_value)

        return new_value

    # Define fuzzy logic rules for string value changes with randomness
    def generate_random_quoted_value(l, is_slice=False):
        if is_slice:
            # If generating a value for slice index, ensure the first number is smaller than the second
            first_number = random.randint(1, 10)
            second_number = random.randint(first_number, 10)  # Ensure second number is greater than or equal to the first
            return f'{first_number}:{second_number}'
        elif l <= 3:
            return random.choice(quoted_values[l])
        else:
            return random.choice(quoted_values[4])
    # Define fuzzy logic rules for operation changes with randomness
    def change_operation(node, string_or_char_variables):
        if string_or_char_variables:
            return ast.Add()  # Use addition when string or character variables are present
        else:
            possible_operations = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div()]  # List of possible operations
            new_operation = random.choice(possible_operations)  # Choose a random operation from the list
            return new_operation

    # Helper function to update variable references
    def update_variable_references(node, old_name, new_name):
        if isinstance(node, ast.Name) and node.id == old_name:
            node.id = new_name
        for child in ast.iter_child_nodes(node):
            update_variable_references(child, old_name, new_name)

    # Parse the code snippet
    #for i in range(len(original_code)):
    variable_names = []
    for i in range(len(original_code)):
        # Reset variable_names list at the beginning of each iteration
        variable_names.clear()
        
        random_quest = original_code[i]
        #print("Original code:", random_quest)
        parsed_code = ast.parse(random_quest)
           
    #random_quest=random.choice(original_code)
    #print("Original code: ",random_quest)
    #parsed_code = ast.parse(random_quest)
   

    string_or_char_variables = False  # Initialize the flag

    # Detect if string or character variables are present in the code
    for node in ast.walk(parsed_code):
        if isinstance(node, ast.Str):
            string_or_char_variables = True
            break

    # Apply fuzzy logic rules with randomness to modify variable names, numeric values, string values, and operations
    for node in ast.walk(parsed_code):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    old_name = target.id
                    new_name = generate_new_variable_name()
                    update_variable_references(parsed_code, old_name, new_name)
                    target.id = new_name
        if isinstance(node, ast.Num):
            node.n = change_numeric_value(node.n)
        if isinstance(node, ast.Str):
            c = node.s.count(' ') + 1
            node.s = generate_random_quoted_value(c)
        if isinstance(node, ast.BinOp):
            node.op = change_operation(node.op, string_or_char_variables)

    # Recompile the modified code
    
    modified_code = astor.to_source(parsed_code)
    return modified_code




def is_numeric(value):
    return isinstance(value, (int, float))


modified_code = modify_code(original_code)

# To execute the modified code and capture the variable values
#print(f"Original code:\n{original_code}")
#print(f"\nModified code:\n{modified_code}")


#modified_code = modify_code(original_code)

# Create a StringIO object to capture the output of the modified code
output_stream = StringIO()

# Redirect sys.stdout to the StringIO object
original_stdout = sys.stdout
sys.stdout = output_stream

# Execute the modified code
exec(modified_code, globals())

# Get the output of the modified code
final_output = output_stream.getvalue()

# Restore the original sys.stdout object
sys.stdout = original_stdout

# Attempt to parse and check if the final_output is numeric
try:
    correct_value = ast.literal_eval(final_output)
except (SyntaxError, ValueError):
    correct_value = final_output

# Generate distractors based on the type of the correct_value

# Print the correct value and distractors
#print("Correct Value:", correct_value)
#print("Distractors:", distractors)
# Genetic Algorithm parameters
population_size = 10
num_generations = 10

def generate_numeric_distractors(correct_value, num_distractors=3):
    distractors = []

    # Generate distractors by applying heuristics based on the correct value
    for i in range(num_distractors):
        heuristic = random.choice(["addition", "subtraction", "change_sign", "rounding"])

        if heuristic == "addition":
            distractor = correct_value + random.randint(1, 10)
        elif heuristic == "subtraction":
            distractor = correct_value - random.randint(1, 10)
        elif heuristic == "change_sign":
            distractor = -correct_value
        elif heuristic == "rounding":
            if correct_value is not None:
                distractor = round(correct_value, random.randint(1, 2))

        distractors.append(distractor)

    return distractors




def generate_string_distractors(correct_string, num_distractors=3):
    distractors = []

    for _ in range(num_distractors):
        heuristic = random.choice(["substring", "concatenation", "capitalization", "reverse"])

        if heuristic == "substring":
            if len(correct_string) > 2:
                start = random.randint(0, len(correct_string) - 2)
                end = random.randint(start + 1, len(correct_string))
                distractor = correct_string[:start] + correct_string[end:]
        elif heuristic == "concatenation":
            distractor = correct_string + random.choice(['abc', 'xyz'])
        elif heuristic == "capitalization":
            distractor = correct_string.upper()
        elif heuristic == "reverse":
            distractor = correct_string[::-1]

        distractor = distractor.replace('\n', '')  # Remove newline characters

        distractors.append(distractor)

    return distractors



'''if is_numeric(correct_value):
    distractors = generate_numeric_distractors(correct_value, num_distractors=3)
else:
    distractors = generate_string_distractors(correct_value, num_distractors=3)
'''

def evaluate_fitness(code):
    try:
        # Create a StringIO object to capture the output of the modified code
        output_stream = StringIO()

        # Redirect sys.stdout to the StringIO object
        original_stdout = sys.stdout
        sys.stdout = output_stream

        # Execute the modified code
        exec(code, globals())

        # Get the output of the modified code
        final_output = output_stream.getvalue()

        if is_numeric(final_output):
            distractors = generate_numeric_distractors(final_output, num_distractors=3)
        else:
            distractors = generate_string_distractors(final_output, num_distractors=3)

        # Restore the original sys.stdout object
        sys.stdout = original_stdout

        # Attempt to parse and check if the final_output is numeric
        try:
            correct_value = ast.literal_eval(final_output)
        except (SyntaxError, ValueError):
            correct_value = final_output

        # Penalize based on syntax errors or incorrect outputs
        if correct_value is None:
            print("Syntax Error or None value during execution.")
            return 0, final_output, distractors  # Penalize for syntax errors
        elif is_numeric(correct_value):
            return 1, final_output, distractors  # Fitness increases for numeric results
        else:
            return 0.5, final_output, distractors  # Penalize for non-numeric results

    except Exception as e:
        # Print the error message
        print(f"Error during execution: {e}")

        # Penalize for any unexpected errors during execution
        return 0, f"Error during execution: {e}", []

def is_numeric(value):
    return isinstance(value, (int, float))

# Genetic Algorithm functions
def roulette_wheel_selection(fitness_scores):
    total_fitness = sum(fitness_scores)
    rand_value = random.randint(0, int(total_fitness))  # Convert total_fitness to an integer
    #print("rand_value: ", rand_value)
    cumulative_fitness = 0
    for i, fitness in enumerate(fitness_scores):
        cumulative_fitness += fitness
        if cumulative_fitness >= rand_value:
            return i


'''def crossover(parent1, parent2):
    # Implement crossover logic
    # For simplicity, we'll use a one-point crossover
    print("length of parent1: ",len(parent1))
    print("length of parent2: ",len(parent2))
    crossover_point = random.randint(1, len(parent1) - 1)
    print("crossover_point: ",crossover_point)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2'''
def find_assignments(tree):
    return [node for node in ast.walk(tree) if isinstance(node, ast.Assign)]

import astunparse

def crossover(parent1, parent2):
    # Parse the parents' code into ASTs
    try:
        ast_parent1 = ast.parse(parent1)
        ast_parent2 = ast.parse(parent2)
    except SyntaxError as e:
        # Handle the syntax error
        print(f"Syntax Error: {e}")
        return None, None

    # Find the first assignment node in each parent
    assign_node_parent1 = next((node for node in ast.walk(ast_parent1) if isinstance(node, ast.Assign)), None)
    assign_node_parent2 = next((node for node in ast.walk(ast_parent2) if isinstance(node, ast.Assign)), None)

    # Swap the values of the first variables
    if assign_node_parent1 and assign_node_parent2:
        assign_node_parent1.value, assign_node_parent2.value = assign_node_parent2.value, assign_node_parent1.value

        # Convert ASTs back to code
        child1 = astor.to_source(ast_parent1)
        child2 = astor.to_source(ast_parent2)

        return child1, child2
    else:
        raise ValueError("Both parents must have at least one assignment statement.")


def is_literal(node):
    return isinstance(node, (ast.Str, ast.Num))

def mutate_node(node):
    # Check if the node is an assignment with a literal value
    if isinstance(node, ast.Assign) and is_literal(node.value):
        return True
    # Add additional checks for other types of nodes to mutate
    # For example, you can add checks for variable values in expressions or function calls
    return False

def mutate(code):
    # Parse the code into an AST
    ast_code = ast.parse(code)

    # Find all nodes in the code
    all_nodes = list(ast.walk(ast_code))

    # Find nodes that can be mutated based on custom conditions
    nodes_to_mutate = [node for node in all_nodes if mutate_node(node)]

    if len(nodes_to_mutate) < 2:
        # If there are fewer than two mutation points, return the original value without mutation
        return code

    # Choose two random nodes for mutation
    node1, node2 = random.sample(nodes_to_mutate, 2)

    # Swap the values of the chosen nodes
    node1.value, node2.value = node2.value, node1.value

    # Convert AST back to code
    mutated_code = astunparse.unparse(ast_code)

    return mutated_code


def new_mcq_func(num_ques: int, num_papers: int):
    mcqs_array = {}

    for j in range(0, num_ques):
        mcqs = {}
        best_index = []
        best_mcq = []
        ans = []
        a = []
        b = []
        c = []

        # Move these lists outside the loop to accumulate values across all papers
        for num in range(0, num_papers):
            # Initialize population
            population = [modify_code(original_code) for _ in range(population_size)]

            # Evaluate fitness of each individual in the population
            fitness_and_outputs = [evaluate_fitness(code) for code in population]
            fitness_scores, outputs, dist = zip(*fitness_and_outputs)

            # Select the best individual
            best_index.append(fitness_scores.index(max(fitness_scores)))
            best_mcq.append(population[best_index[num]])

            # Print the best MCQ
            print(f"Best MCQ {num+1}:\n{best_mcq[num]}")
            ans.append(outputs[best_index[num]])
            print(f"Output of the Best MCQ {num+1}:\n{outputs[best_index[num]]}")
            print("Distractors:")
            final_dist = dist[best_index[num]]

            # Print the contents of final_dist
            print("final_dist:", final_dist)

            for element in final_dist:
                values = element.split(',')

                # Check if there are three values separated by commas
                if len(values) == 3:
                    a.append(values[0])
                    b.append(values[1])
                    c.append(values[2])
                else:
                    # Print a message for unexpected values
                    print("Unexpected values:", values)

        mcqs["dist1"] = a
        mcqs["dist2"] = b
        mcqs["dist3"] = c
        mcqs["dist4"] = ans
        mcqs["ans"] = ans

        mcqs_array[f"mcq{j+1}"] = mcqs

    return mcqs_array

soln = new_mcq_func(5, 5)
