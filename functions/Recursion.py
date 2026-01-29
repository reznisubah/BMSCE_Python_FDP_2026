def function(count):
    count+=1
    print("hii")
    if count<15: #base case
        function(count) # recursive case
    else:
        return


function(10)