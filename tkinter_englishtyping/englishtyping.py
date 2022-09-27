import time
##### Time

test_string = "student teacher dictionary instead type fast average ten words per minute adults should aim once you know speed test check time practice track progress explicitly require certain shorter distances across pointer fingers cozy food activities mental health strategies spend quality time  newfound commitment action plan helps success classrooms stands under leadership decisions graduate automated rostering transform secure metrics administrative permissions internet connection evidence technology latest keyboarding pathway essential documentation support detailed education tests certificates growth robust unified approach correct"
def cal_wpm(input_string):
    start_tm = time.time()
    ##### Count words
    test_string = "student teacher dictionary instead type fast average ten words per minute adults should aim once you know speed test check time practice track progress explicitly require certain shorter distances across pointer fingers cozy food activities mental health strategies spend quality time  newfound commitment action plan helps success classrooms stands under leadership decisions graduate automated rostering transform secure metrics administrative permissions internet connection evidence technology latest keyboarding pathway essential documentation support detailed education tests certificates growth robust unified approach correct"
    # input_string = input('Testing : ')

    test_list = test_string.split(' ')
    input_list = input_string.split(' ')
    ## print(f'test_list : {test_list}')
    ## print(f'input_list : {input_list}' )

    # cnt_totalword = len(test_list)
    cnt_inputword = len(input_list)
    ##### Check the last word
    cnt_correctword = 0
    for test_word, input_word in zip(test_list, input_list):
        if test_word == input_word:
            cnt_correctword += 1
    print(f'Total typed words : {cnt_inputword}, Correct typed words : {cnt_correctword}, Wrong typed words : {cnt_inputword - cnt_correctword} ')
    end_tm =  time.time() - start_tm 
    print(f'Time : {end_tm:.2f} s')
    ##### Calculate words per minute
    wpm = round(cnt_inputword/end_tm*60, 0)
    print(f'Your Words Per Minute : {wpm}')
    return wpm

