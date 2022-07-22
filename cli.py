import argparse
from main import main

DEFAULT_OUTPUT_FILE_NAME = "team_selection"
RESUME_HELP = "path to the resume pdf file"
TEAMS_HELP = "path to the available teams csv file"
OUTPUT_HELP = f"output file name (Default: {DEFAULT_OUTPUT_FILE_NAME})"

def get_input_arguments():
    parser = argparse.ArgumentParser(
        description="IT Intern Team Matcher, if this is run with no args then you will be prompted for the arguments"
    )
    parser.add_argument(
        "resume",
        nargs="?",
        help=RESUME_HELP,
        type=str,
    )
    parser.add_argument(
        "teams",
        nargs="?",
        help=TEAMS_HELP,
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        help=OUTPUT_HELP,
        default=DEFAULT_OUTPUT_FILE_NAME,
        type=str,
    )

    args = parser.parse_args()
    
    # If the user tried to enter CLI args we want to make sure we have both
    if args.resume and not args.teams:
        raise ValueError("Missing Teams positional argument")
    # If the user enters both required positional arguments correctly we want to use them
    elif args.resume and args.teams:
        return args.resume, args.teams, args.output
    # If the user doesn't enter any args we want to prompt for them
    else:
        print("IT Intern Team Matcher")
        print("This can be run without the prompt by providing positional arguments")
        print("when running this program from the command line")
        print()
        resume = input(f"Enter the {RESUME_HELP}: ")
        teams = input(f"Enter the {TEAMS_HELP}: ")
        output = input(f"Enter the {OUTPUT_HELP}: ") or DEFAULT_OUTPUT_FILE_NAME
        return resume, teams, output
        
        
def write_output_file(filename, intern_name, team_name):
    with open(f"{filename}.txt", "a") as output_file:
        output_file.write(f"{intern_name}\t\t{team_name}")

if __name__ == '__main__':
    # This will get us the 3 input parameters
    resume_pdf, teams_csv, output_file_name = get_input_arguments()
    
    # Here is where we can use the 3 input args to do any processing we need to
    main('resources/{}'.format(resume_pdf), 'resources/{}'.format(teams_csv))
    # Now we can append to the output   ile
    test_intern_name = "Bobby Intern"
    test_team_name = "Hedberg H2 Team"
    write_output_file(output_file_name, test_intern_name, test_team_name)
    
    