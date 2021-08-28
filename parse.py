import datetime

file = open('names.txt', 'r')
output = open('index.md', "w")
output.write("")
output.close()
output = open('index.md', 'a')

# months = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
#           '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}

dates = []

for line in file:
    date = line[5:-5]
    try:
        ind = date.index("_")
    except ValueError:
        ind = -1
    
    if ind == -1:
        # date_txt = months[date[:2]] + " " + date[2:4] + ", 20" + date[4:]
        dates.append((line[:-1], datetime.datetime(int("20" + date[4:]), int(date[:2]), int(date[2:4])), ""))
    else:
        # date_txt = months[date[:2]] + " " + date[2:4] + ", 20" + date[4:6] + " : " + date[ind+1:]
        dates.append((line[:-1], datetime.datetime(int("20" + date[4:6]), int(date[:2]), int(date[2:4])), date[ind+1:]))

dates.sort(key=(lambda x: x[1]))
for l, d, ex in dates:
    if ex == "":
        res = "<p><a href=\"./" + l + "\">" + d.strftime("%B %d, %Y") + "</a></p>\n"
    else:
        res = "<p><a href=\"./" + l + "\">" + d.strftime("%B %d, %Y") + " -- " + ex + "</a></p>\n"
    output.write(res)

output.close()
file.close()