
# Write a program to fill in a letter template given below with name and date.


def dispay_selection_status(content,name,date):
    print(content.replace('<|Name|>',name).replace('<|Date|>',date))


letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

dispay_selection_status(letter,'Vijay','15th August 2025')