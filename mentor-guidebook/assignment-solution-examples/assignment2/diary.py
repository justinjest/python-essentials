
import traceback

# open the dairy file for appending
try:
    with open('diary.txt', 'a') as dfh:
        input_line = ''
        prompt = "What happened today? "
        while True:
            # get the next input
            input_line = input(prompt)
            # update the prompt
            prompt = "What else? "
            if input_line == 'done for now':
                break
            # write to the dairy
            dfh.write(input_line + '\n')
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
