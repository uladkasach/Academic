import numpy as np;
import random;
import sys;


###################
## Display state as a matrix
###################
def display_as_matrix(state, conflicts = None):
    n = len(state);
    
    print("Matrix Display: ");
    
    #print("\nArray Display:");
    string = "";
    string_2 = "";
    for i in range(n):
        number = str(state[i]);
        if(len(number) == 2):
            string += (" " + str(state[i]));
        else:
            string += (" " + str(state[i]) + " ");
        string_2 += (" - ");
    print string; 
    print string_2;
    
    #print("Matrix Display:");
    for i in range(n):
        string = "";
        for j in range(n):
            this_pos = state[j];
            if(i == this_pos):
                string += (" Q ");
            else:
                string += (" x ");
        print string;
    
    if(conflicts is not None):
        #print("Conflicts Display:");
        string = "";
        string_2 = "";
        for i in range(n):
            string += (" " + str(int(conflicts[i])) + " ");
            string_2 += (" - ");
        print string_2;
        print string; 
            
    
def default_display_mode(state, conflicts = None, matrix = False ):
    if(matrix):
        display_as_matrix(state, conflicts);
    else:
        print(state);
        
        
    
#####################
## Conflict Count Sub Funciton
#####################
def count_conflicts_for_position(row, column, state):
    queen_exists_at_position = state[column] == row;
    
    ##############
    ## Count Horizontal Conflicts
    ##############
    horizontal_conflicts = 0;
    for i in range(len(state)):
        this_position = state[i];
        if(this_position == -1):
            continue; # there is no queen set in this column
        if(this_position == row):
            horizontal_conflicts += 1;
    if(queen_exists_at_position):
        horizontal_conflicts = horizontal_conflicts - 1; # due to counting self conflicting with self / not accounting for own position
    
    
    ##############
    ## Vertical Conflicts DNE
    ##############
    
    ##############
    ## Count Diagonal Conflicts
    ##      idea: y=mx+b, m = -1, +1. thus, b_+ = i-j, b_- = i+j 
    ##############
    diagonal_conflicts = 0;
    b_positive = row - column;
    b_negative = row + column;
    #print "for location (" + str(row) + "," + str(column) + ") b+ and b- are : " + str(b_positive) +","+ str(b_negative);
    for i in range(len(state)):
        this_positive_row = b_positive + i;
        this_negative_row = b_negative - i;
        #print "checking (" + str(this_positive_row) + "," + str(n) + ") and (" + str(this_negative_row) + "," + str(n) + ") ";
        this_position = state[i];
        if(this_position == -1):
            continue; # there is no queen set in this column
        if(this_position == this_positive_row or this_position == this_negative_row):
            diagonal_conflicts = diagonal_conflicts + 1;
            #print("found conflict at - " , n, this_position, " -> diag conflicts now = ", diagonal_conflicts)
    if(queen_exists_at_position):
        diagonal_conflicts = diagonal_conflicts - 1; # due to counting self conflicting with self / not accounting for own position
            
    total_conflicts = horizontal_conflicts + diagonal_conflicts;
    return total_conflicts;
    
#####################
## Conflict Count
######################
def CONFLICT_COUNT_constraint_satisfaction_evaluation(state, column_id = -1):
    ## Determine the number of conflicts for each row of any column given, or if col_id == -1, for every queen position
    ## returns an array with the above data
    n = len(state);
    conflicts = np.zeros(n);
    
    if(column_id == -1):
        # count conflicts for every queen position
        for i in range(n):
            conflicts[i] = count_conflicts_for_position(state[i], i, state);
        
    else:
        # count conflicts for every position in column i
        for i in range(n):
            conflicts[i] = count_conflicts_for_position(i, column_id, state);
    return conflicts;

########################
## SEARCH Sub-functions
########################
def transition(queen_id, row_id, state):
    ## Move queen_i to row_i on state
    state[queen_id] = row_id;
    return state;

def select_a_conflicting_variable(state, last_var, method = 3):
    ## methods: 1) Select first variable that is found to be conflicting 
    ##          2) Select most conflicting variable out of the conflicting variables
    ##          3) Randomly select a variable out of the conflicting variables
    
    #############
    ## Method 1
    #############
    if(method == 1):
        conflicts = CONFLICT_COUNT_constraint_satisfaction_evaluation(state);
        for i in range(len(conflicts)):
            if(conflicts[i] != 0):
                return i;
            
    #############
    ## Method 2
    #############
    if(method == 2):
        index_max_conflicts = -1;
        max_conflicts_count = 0;
        conflicts = CONFLICT_COUNT_constraint_satisfaction_evaluation(state);
        for i in range(len(conflicts)):
            these_conflicts = conflicts[i];
            if(these_conflicts > max_conflicts_count):
                index_max_conflicts = i;
                max_conflicts_count = these_conflicts;
        return index_max_conflicts;
    
    ###############
    ## Method 3
    ###############
    if(method == 3):
        conflicts = CONFLICT_COUNT_constraint_satisfaction_evaluation(state);
        n = len(conflicts);
        choice = random.randint(0, n-1);
        last_var_accounted = True #(choice != last_var or last_var == -1); #(choice != last_var or last_var == -1); <-- poor performance
        while(conflicts[choice] == 0 and last_var_accounted): ## ensure choice has a conflict
            choice = random.randint(0, n-1);
            last_var_accounted = True #(choice != last_var or last_var == -1); <-- poor performance
        return choice;
        
    
def find_min_conflicting_value_for_variable(state, column):
    conflicts = CONFLICT_COUNT_constraint_satisfaction_evaluation(state, column);
    #print(conflicts);
    #display_as_matrix(state);
    #print("\n");
    current_state = state[column];
    
    min_conflicts_count = len(state) + 1;
    index_min_conflicts = -1;
    for i in range(len(conflicts)):
        these_conflicts = conflicts[i];
        if(current_state == i):
            continue; # ensure queen does not stay in place
        if(these_conflicts < min_conflicts_count):
            index_min_conflicts = i;
            min_conflicts_count = these_conflicts;
    return index_min_conflicts;


#####################
## IsFinalState
######################
def IS_FINAL_STATE_goal_test(state): 
    conflicts = sum(CONFLICT_COUNT_constraint_satisfaction_evaluation(state));
    if(conflicts == 0):
        return True;
    return False;

#####################
## Initialization
######################
def initialization(n = 8):
    ## Initialize the state in a greedy fashion
    state = np.zeros(dtype = 'int', shape = [n]) - 1;
    for i in range(n):
        value = find_min_conflicting_value_for_variable(state, i);
        state[i] = value;
    #print(state);
    return state;


#####################
## SEARCH
######################
def SEARCH_find_n_queens_solution(n = 8, max_steps = 100):
    current_state = initialization(n);
    print "Initial State: ";
    #conflicts = CONFLICT_COUNT_constraint_satisfaction_evaluation(current_state);
    default_display_mode(current_state);

    var = -1;
    for i in range(max_steps):
        print '\n iteration ' + str(i);
        default_display_mode(current_state);
        if(IS_FINAL_STATE_goal_test(current_state)): ## determine if solution was found
            return current_state, i;
        var = select_a_conflicting_variable(current_state, var);
        value = find_min_conflicting_value_for_variable(current_state, var);
        current_state = transition(var, value, current_state);
        
        #print(var);
        #print(value);
        
        #default_display_mode(current_state);
        #exit();
    return False, i;



if len(sys.argv) > 1:
    n_requested = int(sys.argv[1]);
else:
    n_requested = 8

if len(sys.argv) > 2:
    seed_value = int(sys.argv[2]);
else:
    seed_value = 821
    
    
random.seed(seed_value);
###########
## Solve it 
###########
solved = False;
initializations = 0;
total_steps = 0;
while( solved  == False ):
    solution_state, steps = SEARCH_find_n_queens_solution(n_requested);
    if hasattr(solution_state, "__len__"):
        solved = True;
    initializations += 1;
    total_steps += steps;
    #print(result);

###########
## Print Result
###########
print("\n" + str(n_requested) + " Queens: \n");
conflicts = CONFLICT_COUNT_constraint_satisfaction_evaluation(solution_state);
print("Final Solution:");
default_display_mode(solution_state);
print("Total Steps Program Start = " + str(total_steps));
print("Total Initializations = " + str(initializations));
print("Total Steps Since Successful Initialization = " + str(steps));


