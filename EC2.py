import random

marketing_ec2 = ['Gvjvg1', 'Gvgrav2', 'Gvdh3', 'Gfvja4', 'Rdszg', 'Rfee2', 'Rrrhfyu3', 'RFRgFgf4',
                 'Bhgy1', 'Befe2', 'B3rgtrh', 'Bfefe4', 'Phfdz1', 'Pgrarefv2', 'P3rgadhth', 'Paahtf4']  # Random EC2
ec2 = int(input("How many instance do you want: "))
if ec2 == 0:
    print("Enter a value greater than 0")
elif ec2 == 1:
    print(random.choice(marketing_ec2))
elif ec2 == 2:
    print(random.sample(marketing_ec2, 2))
elif ec2 == 3:
    print(random.sample(marketing_ec2, 3))
elif ec2 == 4:
    print(random.sample(marketing_ec2, 4))
elif ec2 == 5:
    print(random.sample(marketing_ec2, 5))
elif ec2 == 6:
    print(random.sample(marketing_ec2, 6))
elif ec2 == 7:
    print(random.sample(marketing_ec2, 7))
elif ec2 == 8:
    print(random.sample(marketing_ec2, 8))
elif ec2 == 9:
    print(random.sample(marketing_ec2, 9))
elif ec2 == 10:
    print(random.sample(marketing_ec2, 10))
elif ec2 == 11:
    print(random.sample(marketing_ec2, 11))
elif ec2 == 12:
    print(random.sample(marketing_ec2, 12))
elif ec2 == 13:
    print(random.sample(marketing_ec2, 13))
elif ec2 == 14:
    print(random.sample(marketing_ec2, 14))
elif ec2 == 15:
    print(random.sample(marketing_ec2, 15))
elif ec2 == 16:
    print(random.sample(marketing_ec2, 16))
else:
    print("ERROR")
department = str(input("Enter your department name: "))
if department == "Marketing":
    print("EC2 that begins with 'G' is for your department")
elif department == "FinOps":
    print("EC2 that starts with 'R' is for your department")
elif department == "Accounting":
    print("EC2 that starts with 'B' is for your department")
elif department == "Engineering":
    print("EC2 that starts with 'P' is for your department")
else:
    print("INVALID ENTRY")
