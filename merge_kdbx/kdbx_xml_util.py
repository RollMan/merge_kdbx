def find_group(root, group_name):
    for group in root:
        if group.find('Name').text == group_name:
            return group
    return None

def find_entry_by_title(group, title):
    for entry in group.findall('Entry'):
        if get_element_title(entry) == title:
            return entry
    return None

def get_element_title(entry):
    for s in entry.findall('String'):
        if s.find('Key').text == 'Title':
            return s.find('Value').text
    return None