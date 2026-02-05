#Method-1
# # -------------------------------
# # Message Class
# # -------------------------------
# # This class represents a single chat message
# class Message:
    
#     # Class variable to generate unique message IDs
#     message_counter = 1

#     def __init__(self, sender, content):
#         # sender → User object who sent the message
#         self.sender = sender
        
#         # content → actual message text
#         self.content = content
        
#         # Assign unique ID to each message
#         self.id = Message.message_counter
        
#         # Increment counter for next message
#         Message.message_counter += 1

#     def __str__(self):
#         # Defines how the message will be printed
#         # Example: (1) Alice: Hello!
#         return f"({self.id}) {self.sender.username}: {self.content}"


# # -------------------------------
# # User Class
# # -------------------------------
# # This class represents a user in the chat system
# class User:
#     def __init__(self, username):
#         # Store username of the user
#         self.username = username
        
#         # Initially user is not in any chatroom
#         self.chatroom = None

#     # Method for joining a chatroom
#     def join_chatroom(self, chatroom):
#         # If user is already in a chatroom
#         if self.chatroom:
#             print(f"{self.username} is already in a chatroom.")
#         else:
#             # Add user to the chatroom
#             chatroom.add_user(self)
            
#             # Save reference of joined chatroom
#             self.chatroom = chatroom
            
#             print(f"{self.username} joined {chatroom.name}")

#     # Method for leaving a chatroom
#     def leave_chatroom(self):
#         # If user is not part of any chatroom
#         if not self.chatroom:
#             print(f"{self.username} is not in any chatroom.")
#         else:
#             # Remove user from the chatroom
#             self.chatroom.remove_user(self)
            
#             print(f"{self.username} left {self.chatroom.name}")
            
#             # Reset chatroom to None
#             self.chatroom = None

#     # Method for sending a message
#     def send_message(self, content):
#         # User must be in a chatroom to send messages
#         if not self.chatroom:
#             print(f"{self.username} cannot send a message (not in a chatroom).")
#         else:
#             # Call chatroom's broadcast method
#             self.chatroom.broadcast(self, content)


# # -------------------------------
# # ChatRoom Class
# # -------------------------------
# # This class represents a chatroom
# class ChatRoom:
#     def __init__(self, name):
#         # Name of the chatroom
#         self.name = name
        
#         # List to store active users
#         self.users = []
        
#         # List to store chat history
#         self.messages = []

#     # Add a user to the chatroom
#     def add_user(self, user):
#         self.users.append(user)

#     # Remove a user from the chatroom
#     def remove_user(self, user):
#         self.users.remove(user)

#     # Send message to all users (broadcast)
#     def broadcast(self, sender, content):
#         # Create a new Message object
#         message = Message(sender, content)
        
#         # Save message in chat history
#         self.messages.append(message)
        
#         # Display message on console
#         print(message)

#     # Show complete chat history
#     def show_chat_history(self):
#         print(f"\nChat History of {self.name}:")
#         for msg in self.messages:
#             print(msg)
#         print()


# # ---------------------------------------
# # Main Program (Example Usage)
# # ---------------------------------------
# if __name__ == "__main__":

#     # Create a chatroom
#     room = ChatRoom("Python Lounge")

#     # Create users
#     u1 = User("Alice")
#     u2 = User("Bob")
#     u3 = User("Charlie")

#     # Users join the chatroom
#     u1.join_chatroom(room)
#     u2.join_chatroom(room)

#     # Users send messages
#     u1.send_message("Hello everyone!")
#     u2.send_message("Hi Alice!")

#     # New user joins and sends message
#     u3.join_chatroom(room)
#     u3.send_message("Hey guys, what's up?")

#     # Display chat history
#     room.show_chat_history()

#     # Users leave the chatroom
#     u1.leave_chatroom()
#     u2.leave_chatroom()
#     u3.leave_chatroom()


class Message():
    message_counter=1

    def __init__(self,user_obj,content):
        self.user_obj=user_obj
        self.content=content
        self.id=Message.message_counter
        Message.message_counter+=1

    def __str__(self):
        return f"({self.id}) {self.user_obj.name} : {self.content}"

class User():

    def __init__(self,name):
        self.name=name
        self.chatroom=None  #instance variable to store chatroom object

    def join_chatroom(self,chatroom):
        if self.chatroom is None :
            chatroom.add_user(self) 
            self.chatroom=chatroom     
            print(f"{self.name} joined the {chatroom.name}")
        else:
            print(f"{self.name} is in the {chatroom.name}")

    def leave_chatroom(self,chatroom):
        if self.chatroom is None :
            print(f"{self.name} is already not in chatroom")

        else :
            self.chatroom.remove_user(self)
            self.chatroom=None
            print(f"{self.name} is removed from {chatroom.name}")    

    def send_msg(self,content):
        if self.chatroom is None:
           print(f"{self.name} is not in chatroom")

        else:
            self.chatroom.broadcast(self,content)


class ChatRoom():
    def __init__(self,name):
        self.name=name
        self.users=[]
        self.masg_history=[]

    def add_user(self,user_obj):
        self.users.append(user_obj)

    def remove_user(self,user_obj):
        self.users.remove(user_obj)

    def broadcast(self,user_obj,content):
        msg=Message(user_obj,content)  
        self.masg_history.append(msg)
        print(msg)

    def chat_history(self):
        for i in self.masg_history:
            print(i)    


room=ChatRoom("Python Lounge")
u1=User("Harshit")
u2=User("Hitesh")
u1.join_chatroom(room)
u2.join_chatroom(room)
u1.send_msg("Hello Everyone")
u2.send_msg(f"Hey {u1.name}")

room.chat_history()
u1.leave_chatroom(room)
u1.send_msg("Hey")