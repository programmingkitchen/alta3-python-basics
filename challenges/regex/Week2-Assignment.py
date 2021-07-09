# LECTURE:  WEEK 2
# TOPIC:  REGULAR EXPRESSIONS
#
# MOOC NAME:  COURSERA
# SERIES TITLE:  Programming for Everbody
# COURSE  NAME:  Course 3 (Using Python to Access Web Data)

# The basic outline of this problem is to read the file, look for integers 
# using the re.findall(), looking for a regular expression of '[0-9]+' and then 
# converting the extracted strings to integers and summing up the integers.
#
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt
# (There are 90 values with a sum=445833)
#
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_42231.txt
# There are 84 values and the sum ends with 212)
import re


print ("\n\nREGULAR EXPRESSIONS:  Week 2 Assignment")


# ====================   Define functions ====================

# Parse out the numbers in a file.   Each line will be read.  Some lines
# will have zero numbers, others will have more than one number resulting in a list
# of numbers for one line.  We need to append these to a master list.
def parseNumbers(fileName, isVerbose):
    print ("\n----------   PARSE AND ADD NUMBERS (file: " + fileName + ")   ----------")

    # Current Regex
    regex = "[0-9]+"

    try:
        fin = open(fileName)
    except:
        print("ERROR:  cannot open fileName")
        quit()

    # Create a list for storage of the numbers
    numberList = list()
    
    for line in fin:
        line = line.rstrip()
        numbersInLine = re.findall(regex, line)
        # If there is something there, then put it in the list
        if len(numbersInLine) > 0:
            for number in numbersInLine:
                numberList.append(int(number))

    print("MIN:", min(numberList))
    print("MAX:", max(numberList))
    print("SUM:", sum(numberList))
    print("COUNT", len(numberList))

    if isVerbose:
        print(numberList)
    
# ====================   Main program flow ====================

isVerbose = False

sampleFile = "regex_sum_42.txt"
assignmentFile = "regex_sum_42231.txt" #rgranier@gmail.com
assignmentFile = "regex_sum_75239.txt" # rg9133@att.com

parseNumbers(sampleFile, isVerbose)
parseNumbers(assignmentFile, isVerbose)
