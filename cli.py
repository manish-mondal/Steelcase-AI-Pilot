import argparse

def get_input_arguments():
    parser = argparse.ArgumentParser(
        description="IT Intern Team Matcher, if this is run with no args then you will be prompted for the arguments"
    )
    parser.add_argument(
        "resume",
        nargs="?",
        help="path to the resume pdf file",
        type=str,
    )
    parser.add_argument(
        "teams",
        nargs="?",
        help="path to the available teams csv file",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output file name (OPTIONAL)",
        type=str,
    )

    args = parser.parse_args()

    if args.resume and args.
    return None, None

if __name__ == '__main__':
    resume_pdf, teams_csv = get_input_arguments()