# Conflict Solver

This application allows for comparision of two big text files. It was created as Software Engineering course project at Silesian University of Technology in academic year 2021/2022.

It allows user to split text into chunks divided by lines/chars/words/sentences. Then all different chunks are listed and available for direct comparision.

User can create new text file which will be merged version of those two files.

## How to run

To run this application from source:

1. Clone this repository to your local machine.
2. Make sure you have Chrome web browser installed.
3. Install python dependencies listed inside requirements.txt file
4. Run main.py

## Testing

Tests are stored inside "tests" directory.
 * test_compare.py: Checks if comparision alghoritm is working as expected
 * test_merge.py: Checks if valid output file is generated after resolving all differences
 * test_splitter_param.py: Checks if input text is splitted correctly.

All test files for test cases are provided.


## Languages Used

This application was created using Java Script, HTML and CSS for GUI and Python for all backend operations.

## License

This application is licensed under the MIT License. See the LICENSE file for more information.