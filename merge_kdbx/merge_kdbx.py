import sys
print(sys.path)
import xml.etree.ElementTree as ET
import merge_kdbx.clparser
import merge_kdbx.kdbx_xml_util
import datetime
from copy import deepcopy

DATETIME_FORMAT = "%Y-%m-%dT%H-%M-%SZ"

def main():
    try:
        args = merge_kdbx.clparser.parse()
    except ValueError as e:
        print(str(e))
        sys.exit(1)
    
    src_xml_trees = [ET.parse(x) for x in args.srcs]
    src_xml_roots = [x.getroot() for x in src_xml_trees]
    dst_tree = ET.parse(args.src[0])
    dst = dst_tree.getroot()

    # root.Root.Group.Entry.{Times.LastModificationTime, String.Password, String.Title}
    for target_xml_root in src_xml_roots[1:].find('Root'):
        for group in target_xml_root.findall('Group'):
            for entry in group.findall('Entry'):
                    group_name = group.find('Name').text
                    entry_last_mod = datetime.datetime.strptime(entry.find('Times').find('LastModificationTime').text, DATETIME_FORMAT)
                    attr = {'Password': '', 'Title': ''}
                    for s in entry.findall('String'):
                        for k in attr.keys():
                            if s.find('Key').text == k:
                                attr[k] = s.find('Value').text

                    # Check `dst` if it has the group of `group_name` and same entry including attr['Title'].
                    dst_group = merge_kdbx.kdbx_xml_util.find_group(dst.find('Root'), group_name)
                    if dst_group == None:
                        dst.find('Root').append(group)

                    dst_entry = merge_kdbx.kdbx_xml_util.find_entry_by_title(dst_group, attr['Title'])
                    if dst_entry == None:
                        dst.find('Root').find(group_name).append(entry)
                    else:
                        src_last_mod = entry_last_mod
                        dst_last_mod = datetime.datetime.strptime(dst_entry.find('Times').find('LastModificationTime').text, DATETIME_FORMAT)
                        if src_last_mod > dst_last_mod:
                            # I believe `dst_entry` is a reference and modification here affects to the entry in `dst_tree` :X.
                            dst_entry = deepcopy(entry)
    
    dst_tree.write(args.dst)

if __name__ == '__main__':
    main()