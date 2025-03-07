
# Program Name: CollegeAdmission.py
# Function: This program determines if a student will be admitted or rejected.
# Input: Interactive
# Output: Accept or Reject

testScore = 0
classRank = 0

# Get input and convert to correct data type for testscore and classrank
testScore = float(input("Please enter your test score:  "))
classRank = float(input("Please enter your class rank:  "))

# Test using admission requirements and print Accept or Reject
if testScore >= 90:
      if classRank >= 25:
         print("Accept")
      else:
         print("Reject")
      
else:
      if testScore >= 80:
         if classRank >= 50:
            print("Accept")
         else:
            print("Reject")
      else:
         if testScore >= 70:
            if classRank >= 75:
               print("Accept")
            else:
              print("Reject")
         else:
            print("Reject")