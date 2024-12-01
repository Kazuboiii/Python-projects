#Match-case Statement (Switch) = An alternative to using many 'elif' statements
#                               Execute some code if a value matches a 'case'
#                               Benefits : cleaner and syntax is more readable
#def day_of_weeks(day):
#    match day:
#        case 1:
#            return "IT IS SUNDAY !!!"
#       case 2:
#            return "IT IS MONDAY !!!"
#        case 3:
#            return "IT IS TUESDAY !!!"
#        case 4:
#            return "IT IS WEDNESDAY !!!"
#        case 5:
#            return "IT IS THURSDAY !!!"
#        case 6:
#            return "IT IS FRIDAY !!!"
#        case 7:
#            return "IT IS SATURDAY !!!"
#        case _:
#            return "IT IS NOT A VALID DAY,PLEASE ENTER FROM 1 TO 7"
#
#print(day_of_weeks(2))

#def is_weekends(day):
#    match day:
#        case "Sunday":
#           return True
#        case "Monday":
#            return False
#        case "Tuesday":
#            return False
#        case "Wednesday":
#            return False
#        case "Thursday":
#            return False
#        case "Friday":
#           return False
#        case "Saturday":
#           return True
#        case _:
#           return 'ENTER A VALID DAY'

#print(is_weekends('Saturday'))
def is_weekends(day):
    match day:
        case "Sunday"|"Saturday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case _:
            return 'ENTER A VALID DAY'

print(is_weekends('Tuesday'))