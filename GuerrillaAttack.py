
import copy

def calculate_time(spy, camp):
    x1, y1 = spy
    x2, y2 = camp
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def hungarian_algorithm(cost_matrix):
    # Step 1: Subtract the minimum value from each row and each column
   
    n = len(cost_matrix)
    for i in range(n):
        min_val = min(cost_matrix[i])
        for j in range(n):
            cost_matrix[i][j] -= min_val
    # print(cost_matrix)

    for j in range(n):
        min_val = min(cost_matrix[i][j] for i in range(n))
        for i in range(n):
            cost_matrix[i][j] -= min_val
    # print(cost_matrix)

    # Step 2: Find the minimum number of lines to cover all zeros in the matrix
    rows_covered = [False] * n
    cols_covered = [False] * n
    lines = 0

    while lines < n:
        # Find the minimum uncovered value
        min_val = float('inf')
        for i in range(n):
            if not rows_covered[i]:
                for j in range(n):
                    if not cols_covered[j]:
                        min_val = min(min_val, cost_matrix[i][j])
        # print(rows_covered, cols_covered, min_val)

        # Subtract the minimum value from all uncovered values
        for i in range(n):
            if not rows_covered[i]:
                for j in range(n):
                    cost_matrix[i][j] -= min_val
        # print(cost_matrix)

        for j in range(n):
            if not cols_covered[j]:
                for i in range(n):
                    cost_matrix[i][j] -= min_val
        # print(cost_matrix)

        # Cover rows and columns with zeros
        for i in range(n):
            if not rows_covered[i]:
                for j in range(n):
                    if not cols_covered[j] and cost_matrix[i][j] == 0:
                        rows_covered[i] = True
                        cols_covered[j] = True
                        lines += 1
                        break
        # print(rows_covered, cols_covered, lines)

    # Step 3: Find the optimal assignment
    assignment = [-1] * n
    for i in range(n):
        for j in range(n):
            if cost_matrix[i][j] == 0 and assignment[j] == -1:
                assignment[j] = i
        # print(assignment)

    return assignment

def min_total_time(cost_matrix):
    # Apply the Hungarian algorithm to find the optimal assignment
    cost_matrix_old = copy.deepcopy(cost_matrix)
    assignment = hungarian_algorithm(cost_matrix_old)
    # print(assignment)
    # print(cost_matrix)
    # print(cost_matrix_old)

    temp = []
    for i in range(len(assignment)):
        temp.append(cost_matrix[i][assignment[i]])
    # print(temp)
    # Calculate the minimum total time
    total_time = max(temp)

    return total_time

def create_cost_matrix(directory, num_camps):
    # Extract unique soldiers and camps from the directory
    soldiers = list(directory.keys())
    camps = set()

    for camps_dict in directory.values():
        camps.update(camps_dict.keys())

    camps = list(camps)

    # Initialize the cost matrix with infinity values
    num_soldiers = len(soldiers)
    num_camps = len(camps)
    cost_matrix = [[float('inf')] * num_camps for _ in range(num_soldiers)]

    # Fill the cost matrix with the actual costs
    for i, soldier in enumerate(soldiers):
        for j, camp in enumerate(camps):
            if camp in directory[soldier]:
                cost_matrix[i][j] = directory[soldier][camp]

    return cost_matrix



# Main ======================================================
N, M, K = map(int, input().split())

spies = {}
camps = {}


for i in range(N):
    x, y = map(int, input().split())
    spies[f's{i+1}'] = (x, y)


for i in range(M):
    x, y = map(int, input().split())
    camps[f'c{i+1}'] = (x, y)

graph = {}

# Calculate time for each spy to inform each camp
for s_key, s_value in spies.items():
    graph[s_key] = {}
    for c_key, c_value in camps.items():
        graph[s_key][c_key] = calculate_time(s_value, c_value)

# print(graph)

# Create the cost matrix
cost_matrix = create_cost_matrix(graph, K)

# # Print the cost matrix
# for row in cost_matrix:
#     print(row)

# print(cost_matrix)



# Calculate the minimum total time
total_time = min_total_time(cost_matrix)





print(total_time)


