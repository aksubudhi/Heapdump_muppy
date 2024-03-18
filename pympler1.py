


from pympler import muppy, summary
all_objects = muppy.get_objects()
sum1 = summary.summarize(all_objects)

all_list = []
for line in summary.format_(sum1, limit=15, sort='size', order='descending'):
    all_list.append(line)

all_str = "\n".join(all_list)

print(all_str)
