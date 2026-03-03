# Name: MUHAMMAD AHSAN
# ID: SP25-BBD-093

# This function moves messages from first_list to sent_messages
def send_messages(first_list, sent_messages):
    while first_list:
        current_msg = first_list.pop()
        sent_messages.append(current_msg)
