import os

folder_path = "/Users/cindyli/imessage_export_last_year"

rank = []


for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as file:
            messages_sent_by_me = 0
            total_texts = 0
            content = file.read()
            lines = content.splitlines()
            for line in lines:
                if (line) == "":
                     total_texts+=1
                if line.strip() == "Me":
                    messages_sent_by_me += 1
            
            rank.append((filename, messages_sent_by_me, total_texts-messages_sent_by_me))

sorted_array = sorted(rank, key=lambda x: x[1])
sorted_array.reverse()

counter = 1
for line in sorted_array:
    print(str(counter) + ":" + str(line))
    counter+=1
        

# file_path = os.path.join(folder_path, '+16073397764.txt')
# with open(file_path, "r") as file:
#             messages_sent_by_me = 0
#             content = file.read()
#             lines = content.splitlines()
#             total_texts = 0
#             messages_sent_by_me = 0
#             for line in lines:
#                 if (line) == "":
#                      total_texts+=1
#                 if line.strip() == "Me":
#                     messages_sent_by_me += 1

# print(total_texts)
# print(messages_sent_by_me)

