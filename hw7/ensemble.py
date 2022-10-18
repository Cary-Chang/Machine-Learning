import csv

ans = []
with open('result_1.csv', newline='', encoding="utf-8") as f1:
    with open('result_2.csv', newline='', encoding="utf-8") as f2:
        with open('result_3.csv', newline='', encoding="utf-8") as f3:
                row1 = list(csv.reader(f1))
                row2 = list(csv.reader(f2))
                row3 = list(csv.reader(f3))
                
                del row1[0], row2[0], row3[0]
                for i in range(3493):
                    temp = []
                    temp.append(row1[i][1])
                    temp.append(row2[i][1])
                    temp.append(row3[i][1])
                    ans.append(max(temp,key=temp.count))

result_file = "result_ensemble.csv"
with open(result_file, 'w', encoding="utf-8") as f:	
    f.write("ID,Answer\n")
    for i, s in enumerate(ans):
        f.write(f"{i},{s}\n")