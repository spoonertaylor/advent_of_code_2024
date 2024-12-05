# Advent of Code, Day 1
def match_list_distance(l1, l2):
    l1.sort()
    l2.sort()
    l3 = [abs(e1-e2) for e1,e2 in zip(l1,l2)]
    return sum(l3)

def read_input():
    a = []
    b = []
    with open("input_file.txt", 'r') as f:
        for line in f.readlines():
            x, y = (int(z) for z in line.split())
            a.append(x)
            b.append(y)
    return(a,b)

## Part 2
def multiply_counter(l1, l2):
    l3 = [e1*l2.count(e1) for e1 in l1]
    return(sum(l3))

if __name__ == "__main__":
    l1,l2 = read_input()

    list_dist = match_list_distance(l1,l2)
    print(f"List Distance: {list_dist}")
    mult_dist = multiply_counter(l1,l2)
    print(f"New safe reports {mult_dist}")
