import argparse

def __check_overwriting_source(dst, src):
    if dst in src:
        return True
    return False

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--force',
        help='permit overwriting source file by dst.'
    )
    parser.add_argument(
        'dst',
        type=str,
        help='path to destination xml files.'
    )
    parser.add_argument(
        'srcs',
        type=str,
        nargs='+',
        help='paths to source xml file to be merged.'
    )

    args = parser.parse_args()

    if not args.force and __check_overwriting_source(args.dst, args.src):
        raise ValueError("overwriting source file of {} is not permitted. remove the option of `-f`.".format(args.dst))


    return args