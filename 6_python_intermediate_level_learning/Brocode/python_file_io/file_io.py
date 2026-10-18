lion_king_info = ['The Lion King is a 1994 American animated musical coming-of-age drama film',
'produced by Walt Disney Feature Animation and released by Walt Disney Pictures.',
'The film was directed by Roger Allers and Rob Minkoff, produced by Don Hahn, and written by Irene Mecchi, Jonathan Roberts, and Linda Woolverton.',
'The film features an ensemble voice cast consisting of Matthew Broderick, James Earl Jones, Jeremy Irons, Jonathan Taylor Thomas, Moira Kelly, Niketa Calame, Nathan Lane, Ernie Sabella, Whoopi Goldberg, Cheech Marin, Rowan Atkinson, and Robert Guillaume.',
'The story follows a young lion named Simba, who is exiled from his kingdom after his father Mufasa is murdered by his uncle, Scar. As he grows up, Simba must decide whether to return home to confront Scar and reclaim his place as king.'
]

def write_to_file_generator():
   with open(".\\Lion_King.txt",'x') as file:
      content = (info for info in lion_king_info)
      count = 0 
      while count < len(lion_king_info):
         file.write(next(content))
         file.write("\n")
         count+=1
         if count == 3:
            break


def read_from_file_generator():
   with open(".\\Lion_King.txt",'r') as file:
      content = (line for line in file.readlines())
      count = 0 
      while count < len(lion_king_info):
         print(next(content))
         count+=1
         if count == 3:
            break

write_to_file_generator()
read_from_file_generator()