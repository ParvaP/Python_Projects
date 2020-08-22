def count_pos(raw_input):
    count = 0
    for i in range(len(raw_input)):
        raw_input[i] = float(raw_input[i])
    for i in raw_input:
        if i > 0:
            count = count + 1
    return count


raw_input = input ("Please input a list of numbers separated by space: ").strip().split()
print ("There are",count_pos(raw_input),"positive numbers in your list.")
