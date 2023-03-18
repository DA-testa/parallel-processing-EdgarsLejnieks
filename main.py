# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    # col1 = thread number; col2 = time of starting a new task

    # I create a dictionary (hashmap) which will store data about cores
    processor = {}
    for thread in range(n):
        processor[thread] = 0

    timer = 0
    while(len(data) != 0):
        for thread in range(n):
            if processor[thread] == 0:
                processor.update({thread:data.pop(0)})
                output.append([thread, timer])
                
        timer += 1
        for thread in range(n):
            processor[thread] = int(processor[thread]) - 1

    return output

def main():
    # first line - n and m
    # n - thread count 
    # m - job count
    firstline = input()
    secondline = input()
    twonums = firstline.split(" ")
    n = int(twonums[0])
    m = int(twonums[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = secondline.split()
    # print (n, m,"\n", data)

    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

    for i in result:
        print(i)



if __name__ == "__main__":
    main()
