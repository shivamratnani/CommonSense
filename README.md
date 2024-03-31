# CommonSense
### **Backend - Python**

1. Create a Quizlet search that gets the top results for “Computer Science Internship Key Terms”
2. Get first 12 Quizlets
3. Web scrape them with 1st column question, second answer
4. Feed each column into gpt and get 4 wrong answers for each question
    1. These will be next 4 columns with total columns being 6
5. Send this to **Frontend - React or Django**

### Frontend - React or Django

1. Create home page then have mobile and desktop view
    1. Variable view size
    2. Question
    Answer x5
    3. Wrap question
    4. Randomize question order
    5. Show question
    6. Select question then submit
    7. if right say Correct! \n [Question] \n [Answer]
    if Wrong say Wrong! \n [Question] \n [Answer]
    Next Question button
    8. Top right profile w/ percentage - xcorrect/xquestions
