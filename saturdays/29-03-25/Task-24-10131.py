with open("24_10131.txt") as f:
    data = f.readline()


# ids_A = [i for i in range(len(data)) if data[i] == "A"]
# ids_B = [i for i in range(len(data)) if data[i] == "B"]
#
# ans = 0
# for i in range(1, len(ids_A) - 1):
#     for j in range(i, len(ids_A) - 1):
#         line = data[ids_A[i - 1] + 1:ids_A[j + 1]]
#         c_B = line.count("B")
#         c_A = j - i + 1
#         if c_A > c_B:
#             continue
#         while c_A != c_B and (line.find("B") < line.find('A') or line.rfind("A") < line.rfind("B")):
#             left_B = line.find("B")
#             right_B = len(line) - line.rfind("B")
#             if left_B <= right_B:
#                 line = line[left_B+1:]
#             elif left_B > right_B:
#                 line = line[:right_B]
#             else:
#
#             c_B -= 1
#
#         ans = max(ans, len(line))
#         print(ans)
#
#
# print(ans)



