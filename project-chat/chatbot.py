import random
import time

# list of agent names that will be randomly generated for each session
agents = ["Zoey Lawrance", "Matt Styles", "Leonardo Owens", "Lana Garner", "Riley Fox", "Allan Ellison"]

# list of responses if keyword is found
responses= {
    "location": "The University of Poppleton is located in PA13 4SR, Scotland, Highland. A detailed campus map is available on our website for your convenience.",
    "located": "The University of Poppleton is located in PA13 4SR, Scotland, Highland. A detailed campus map is available on our website for your convenience.",
    "coffee": "The cafe opens from 7:30 AM to 6 PM on weekdays, serving variety of drinks and bakery items. The cafe provides a pleasant atmosphere for the students to hang out with their friends. ",
    "cafe": "The cafe opens from 7:30 AM to 6 PM on weekdays, serving variety of drinks and bakery items. The cafe provides a pleasant atmosphere for the students to hang out with their friends. ",
    "course": "The University of Poppleton offers a wide range of undergraduate and postgraduate courses. Visit the courses section of the website for more details.", 
    "program": "The University of Poppleton offers a wide range of undergraduate and postgraduate courses. Visit the courses section of the website for more details.",
    "subject": "The University of Poppleton offers a wide range of undergraduate and postgraduate courses. Visit the courses section of the website for more details.",  
    "library": "The library is open from 6 AM to 8 PM on weekdays and from 10 AM to 6 PM in the weekends, offering our students with peaceful space and extensive resources.",
    "sport":  "Our university offers top-notch sports facilities to support our student’s physical well-being, such as a fully equipped gym, swimming pool, table tennis, and outdoor sports field.",
    "admission": "Admissions for the upcoming semester are open! Applications can be submitted through the online admissions portal.",
    "scholarship": "Scholarship opportunities are available for students. For further information, please visit the scholarships section on our website. ",
    "room": "Comfortable on-campus accommodation with a variety of room options are available to make you feel like home. Check out the dorm options on our website.",
    "drom": "Comfortable on-campus accommodation with a variety of room options are available to make you feel like home. Check out the dorm options on our website.",
    "fee": "Tuition fees vary by the course you choose. For a detailed fee structure, please visit the admission section on our website.",  
    "event": "To engage students and foster a sense of community, our university hosts various events. Kindly refer to the events calendar on our website for exact dates and details of our upcoming event.",  
    "exam": "The exam schedule is published on the university portal. Students are advised to log in to view their routine.",
    "examination": "The exam schedule is published on the university portal. Students are advised to log in to view their routine.", 
    "wifi": "Free Wi-Fi is available for all students. Login credentials are available in the IT Department Board.",  
    "internet": "Free Wi-Fi is available for all students. Login credentials are available in the IT Department Board.",
    "club": "There are many student clubs at our university, including drama club, robotics club, debate club, sports club, and photography club.",
    "canteen": "The canteen is open from 9 AM to 8:30 PM and offers a variety of meals, including both vegetarian and non-vegetarian options.",
    "lunch": "The canteen is open from 9 AM to 8:30 PM and offers a variety of meals, including both vegetarian and non-vegetarian options.",
    "medical": "The university infirmary is open 24/7 to provide medical help to students.",
    "health": "The university infirmary is open 24/7 to provide medical help to students.",
    "sick": "The university infirmary is open 24/7 to provide medical help to students.",
    "injury": "The university infirmary is open 24/7 to provide medical help to students.",
    "injured": "The university infirmary is open 24/7 to provide medical help to students.",
    "internship": "Career services help students find internships. Check the career portal for current opportunities.",  
    "intern": "Career services help students find internships. Check the career portal for current opportunities.", 
    "career": "Career services help students find internships. Check the career portal for current opportunities.", 
    "job": "Career services help students find internships. Check the career portal for current opportunities.", 
    "alumni": "The university has an active alumni network that supports current students through mentoring programs and organizing events.",  
    "shift": "The university operates both morning and day shifts. Morning shifts run from 7:00 AM to 10:30 AM, and day shifts run from 11:00 AM to 4:00 PM, accommodating diverse schedules for students and faculty.",
    "time": "The university operates both morning and day shifts. Morning shifts run from 7:00 AM to 10:30 AM, and day shifts run from 11:00 AM to 4:00 PM, accommodating diverse schedules for students and faculty.",
    "timing": "The university operates both morning and day shifts. Morning shifts run from 7:00 AM to 10:30 AM, and day shifts run from 11:00 AM to 4:00 PM, accommodating diverse schedules for students and faculty."
}

# list of responses that displays if a keyword is not found
random_responses= [
    "I am not sure about that {user_name}, Can you provide me with more details?", 
    "That is an interesting question {user_name}. Let me think about it. I will get back to you with more details shortly.",  
    "I am sorry {user_name}, I am not sure I have an answer for that right now.",  
    "Hmm, I am not sure. Could you clarify a bit more?",  
    "I will need to check on that for you. Can I assist you with something else in the meantime?",  
    "I am not quite sure about that, but I will find a way to get you an answer!"
]

# list of fun facts that displays occasionally if a keyword is not found 
fun_facts= [
    "FUN FACT: Did you know? The university library has over 500,000 books!", 
    "FUN FACT: Our campus cafe sold 10,000 cups of coffee last month. Looks like we are fueled by caffeine!",  
    "FUN FACT: The university library has underground levels! It is the quietest spot on campus, perfect for studying.", 
    "FUN FACT: The art department’s walls are painted by students every year. Each one tells a unique story about campus life.",  
    "FUN FACT: The biology department’s collection of butterflies includes rare species from six continents!"
]

# list of exit keywords to quit the chat session
exit_keywords = ["quit", "exit", "bye", "goodbye", "end"]

# function to greet the user        
def greet_user(user_name,agent_name):
    # gets the current hour of the day to personalize the greeting
    current_hour = time.localtime().tm_hour 
    # displays a cherry greeting message for the user from their agent based on the time of the day
    if 0<=current_hour<12:
        print(f"Welcome to the official website of the University of Poppleton!\nGood morning {user_name}, hope you are having a good day. I am {agent_name} your virtual assistant, here to help you with any inquiries. How may I assist you today?")
    elif 12<=current_hour<16:
        print(f"Welcome to the official website of the University of Poppleton!\nGood afternoon {user_name}, hope you are having a good day. I am {agent_name} your virtual assistant, here to help you with any inquiries. How may I assist you today?")
    else:
        print(f"Welcome to the official website of the University of Poppleton!\nGood evening {user_name}, hope you are having a good day. I am {agent_name} your virtual assistant, here to help you with any inquiries. How may I assist you today?")
        
# function to handle the chat interaction 
def chatbot():
    # pick a random agent name from the list for the session
    agent_name = random.choice(agents)

    # prompt user to input their name
    user_name = input("Please enter your name: ").capitalize()
    
    # calls the function to greet the user
    greet_user(user_name,agent_name)

    # opens and stores conversation history in chat.txt 
    log_file=open("chathistory.txt", "a") 
    log_file.write(f"\nChat session started with {user_name} assisted by agent {agent_name}\n")
     
    # start chat loop
    while True: 
        # prompts the user to input their query
        queries_input = input(f"{user_name}: ").lower() # changes user input into lowercase for comparison
        words_in_input = queries_input.split()  # splits sentence into words and stores it inside a list

        # write the user's question in file chat.txt
        log_file.write(f"Question: {queries_input}\n")

        # checks if the user wants to exit the chat by finding exit keyword in the user input
        exit_detection=False
        for i in range(len(exit_keywords)):
            # check if current exit_keyword is in words_in_input list by comparing each word
            for j in range(len(words_in_input)):
                if exit_keywords[i] == words_in_input[j]: # comparing if the words match
                    exit_detection=True
                    print(f"{agent_name}: It was a pleasure assisting you, {user_name}. Thank you for reaching out. If you have any more questions, feel free to reach out again. Have a wonderful day!")
                    print("Contact info: 228-993-4339")
                    # writes the end of chat session in chat.txt 
                    log_file.write(f"The chat session came to an end.\n")
                    break # breaks inner loop
            j=j+1
            if exit_detection==True:
                break  # break outer loop
        i=i+1
        if exit_detection==True:
            break  # breaks the while loop 

        # simulate random disconnection
        disconnect_choices = ["disconnected", "connected1", "connected2", "connected3", "connected4", "connected5"]
        disconnect = random.choice(disconnect_choices)  # randomly choose if there is a connectivity issue
        if disconnect=="disconnected":
            print(f"{agent_name}:  Oops! It seems we have lost the connection. Trying to reconnect...")
            log_file.write(f"Chat disconnected...\n")
            time.sleep(random.randint(3, 5))  # pause the program for random seconds ranging from 3 to 5 seconds
            print(f"{agent_name}: I am back online! Sorry for the brief interruption, {user_name}. Let’s continue.")
            log_file.write(f"Chat reconnected!\n")
        
        # empty list
        matching_response= []

        # loops through each word in the user's query to find matching responses
        for x in range(len(words_in_input)):
            # Remove the last "s" in case the keyword is plural
            if words_in_input[x][-1]=="s":
                words_in_input[x] = words_in_input[x][:-1]  

            # checks if any word matches the keyword
            for keyword, response in responses.items():
                if keyword == words_in_input[x]:
                    matching_response.append(response) # appends the response to the empty list(matching_response)

        # checks if more than one keyword is found in the user's query and responds accordingly         
        if len(matching_response)>1:
            print(f"{agent_name}: I detected that you have asked questions on multiple topics. Here is what i could gather:")
            log_file.write(f"Answer: Multiple keywords detected:\n")
            for y in range(len(matching_response)):
                print(f"\t{matching_response[y]}")
                log_file.write(f"{matching_response[y]}\n")
        # displays response if only one keyword was found in the user's query
        elif len(matching_response)==1:       
                print(f"{agent_name}: {matching_response[0]}")
                log_file.write(f"Answer: {matching_response[0]}\n") 
        # displays random response if no keyword was found in the user's query
        else: 
            no_keyword= random.choice(random_responses)
            print(f"{no_keyword.replace('{user_name}', user_name)}")
            log_file.write(f"Answer: {no_keyword}\n")

            # randomly displays a fun fact from the list
            choices = ["fun", "continue"]
            fact= random.choice(choices)
            if fact=="fun":  
                fact = random.choice(fun_facts)
                print(f"{agent_name}: {fact}")
                log_file.write(f"Fun fact  was displayed: {fact}\n")

    # close the files after the chat session ends
    log_file.close()

# starts the chatbot
chatbot()
