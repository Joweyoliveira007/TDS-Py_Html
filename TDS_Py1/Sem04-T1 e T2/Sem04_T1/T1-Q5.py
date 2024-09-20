def num_inverso(num_escrito):
    d1oo = num_escrito // 1000
    d2oo = (num_escrito % 1000) // 100
    d3oo = (num_escrito % 10) //10
    d4oo = (num_escrito % 10) // 1
    return(d4oo * 1000) + (d3oo * 100) + (d2oo * 10) + (d1oo * 1)

num = int(input())
total_inverso = num_inverso(num)
print(f"{total_inverso}")