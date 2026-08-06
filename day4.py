# condition statement
# age = 20
# if age > 18:
#     print("you can vote")
# else:
#     print("You cannot vote")

# password = "nepal123"

# if password =="nepal123":
#     print("login successful")
# else:
#     print("login failed")

# logged_in = False
# if not logged_in:
#     print("Please logged in")



# looping
# for i in range(2,11,2):
#     print(i)

# countries = ["nepal","japan","india"]
# for country in countries:
#     print(country)


# prediction_score = [77,99,23,67]
# for score in prediction_score:
#     if score > 80:
#         print(score,"good score")
#     else:
#         print(score,"bad score")


emails_list = [
    "Bhatbhateeni ma discount",
    "Yeti airlines free ticket congrats jitiyo",
    "What is the project update guys",
    "Congratulations, you won rolex watch"
]

for email in emails_list:
    if "congrats" in email or "Congratulations" in email or "discount" in email:
        print("spam",email)
    else:
        print("Not spam",email)