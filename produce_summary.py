# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()

# Final output should look like this:
# Delivered 18 Scaly Bark Watermelons for total of $72.00

def produce_summary(day_number, data_file):

    print('Day', day_number)

    the_file = open(data_file)

    for data in the_file:

        data = data.rstrip().split("|")

        name = data[0]
        count = data[1]
        price = data[2]

        print (f"Delivered {count} {name} for a total of {price}.")


print(produce_summary(1, 'um-deliveries-20140519.txt'))
print(produce_summary(2, 'um-deliveries-20140520.txt'))
print(produce_summary(3, 'um-deliveries-20140521.txt'))





























