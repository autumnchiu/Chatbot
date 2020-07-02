
## This is a simple retrieval bot that matches intent (picks the closest response) and also identifies the identity (replaces blank spot
# in response with the object in question. 

# Important to notice that the functions of user_functions are defined in seperate gist that needs to be imported


from collections import Counter
# from responses import responses, blank_spot
from utility import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
import spacy
from dialogue_act import is_wh_question, is_yn_question
from process_info import my_to_your, find_keyword
word2vec = spacy.load('en')

exit_commands = ("quit", "goodbye", "exit", "no","stop","bye")
responses = []
class ChatBot:
  
  #define .make_exit() below:
  def make_exit(self,user_message):
    for com in exit_commands:
       if com in user_message:
         print("Goodbye!")
         return True
    return False
     
  #define .chat() below:
  def chat(self):
    user_message = input("Hi, how can I help you?\n")
    while not self.make_exit(user_message):
        if not (is_yn_question(user_message) and is_wh_question(user_message)):
            self.store_as_response(user_message)
            user_message = input("I've taken note of that, is there anything else I can help you with?\n")
            continue
        else:
            user_message = self.respond(user_message)


  #define .find_intent_match() below:
  def find_intent_match(self,responses,user_message):
    if len(responses) == 0:
        return self.idk_response(user_message)
    processed_message = Counter(preprocess(user_message))

    processed_responses = [Counter(preprocess(response)) for response in responses]

    similarity_list = [compare_overlap(processed_message,rep) for rep in processed_responses]
    # If none of the responses really fit what the user is asking:
    if(max(similarity_list)<0.5 or len(responses)==0):
        return self.idk_response(user_message)

    response_index = similarity_list.index(max(similarity_list))
    return responses[response_index]

#   #define .find_entities() below:
#   def find_entities(self,user_message):
#     um = preprocess(user_message)
#     tagged = pos_tag(um)
#     message_nouns = extract_nouns(tagged)
#     string = " ".join(message_nouns)
#     tokens= word2vec(string)
#     category = word2vec(blank_spot)
#     word2vec_result = compute_similarity(tokens,category)
#     word2vec_result.sort(key=lambda x: x[2])
#     if len(word2vec_result)>0:
#       return word2vec_result[-1][0]
#     else:
#       return blank_spot

  #define .respond() below:
  def respond(self,user_message):
    
    best_response = self.find_intent_match(responses,user_message)
    # entity = self.find_entities(user_message)
    # print(best_response.format(entity))
    print(best_response)
    input_message = input("\nWhat else can I help you with?\n")
    return input_message

  def idk_response(self,user_message):
      kw = ""
      if find_keyword(user_message) == None:
          kw = "that"
      else:
          kw = find_keyword(user_message)
    
      kw1 = my_to_your(kw)
      print(kw1)
      response = "I'm sorry, I don't have any information about {}."
      formatted = response.format(kw1)
      return formatted
    
  def store_as_response(self,user_message):
      response = my_to_your(user_message)
    #   key = find_keyword(user_message)
      responses.append(response)
      return True

#initialize ChatBot instance below:
bot = ChatBot()
bot.chat()
#call .chat() method below:

