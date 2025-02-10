# LinkedIn Customized Post Generator For Bill Gates (Llama3.2)
## Made by Tulsi Patel and Mayank Pareek
![Screenshot (9)](https://github.com/user-attachments/assets/f4005b38-9c85-42b5-9d83-f9bcde40d005)
# [DEMO LINK 🔗](https://mayankprojectlinkedin.streamlit.app/)
## Project Aim
The primary aim of this project is to automate the creation of LinkedIn posts based on specified parameters, such as topic, language, and length, enabling streamlined post generation for various themes and styles. The tool reads, processes, and filters pre-existing post data, incorporates a language model for new content generation, and allows users to specify criteria to generate posts effectively.

## Detailed File Explanations

### few_shot.py

Purpose: This file is dedicated to processing post data and filtering it based on specific criteria. It enables quick access to relevant posts that can serve as examples or inspiration.

Imports: Imports essential libraries pandas and json to handle data in JSON format and manipulate it as DataFrames.

FewShotPosts Class:

__init__ Method: Initializes the class and loads the processed post data from a JSON file, creating two instance variables:
self.df: Stores the DataFrame with post data.
self.unique_tags: Stores unique tags for categorizing posts.
load_posts Method: Opens and reads a JSON file, converts it into a pandas DataFrame, and calculates each post's length category ("Short," "Medium," or "Long").
get_filtered_posts Method: Filters posts based on criteria like length, language, and tag, returning posts that match these criteria.
categorize_length Method: Determines the length category for each post based on the line count.
get_tags Method: Returns the unique tags identified in the dataset.
Main Execution Block: Creates an instance of FewShotPosts and calls get_filtered_posts to display posts matching given criteria.

### llm_helper.py

Purpose: This file initializes and manages the connection to a language model service, ChatGroq, which will generate language-based responses.

Imports: Imports necessary libraries for environment handling, ChatGroq for language model interaction, and os for accessing environment variables.
load_dotenv Call: Loads environment variables from a .env file.
Language Model Initialization (llm): Initializes the language model with API credentials.
Main Execution Block: Tests the language model by prompting it with a query about Bill Gates.
main.py

Purpose: This file creates a user interface (UI) in Streamlit for users to select post criteria, submit their request, and view the generated LinkedIn post.

Imports: Imports Streamlit for UI, FewShotPosts for accessing post data, and generate_post for post generation.
UI Setup:
Dropdowns and Button: Allows users to select a topic, post length, and language.
Generate Button: Calls the generate_post function to display a generated LinkedIn post based on selected parameters.
post_generator.py

Purpose: This file constructs the prompt for the language model, feeding it with the criteria and example posts to generate a LinkedIn post.

Imports: Imports the language model instance (llm) and FewShotPosts class.
get_length_str Function: Maps length categories to line count ranges.
generate_post Function: Forms a prompt based on user criteria and invokes the language model to generate a post.
get_prompt Function: Builds a detailed prompt with topic, length, and language details and provides examples if available to guide the language model in generating a similar style.

### preprocess.py

Purpose: This file is responsible for processing raw LinkedIn posts, extracting metadata (e.g., language, tags, line count), and generating unified tags.

Imports: Includes json for file handling, llm for language model interaction, and various LangChain components for prompt and output parsing.
process_posts Function: Loads raw posts, enriches them with metadata, unifies tags, and writes the processed data back to a file.
extract_metadata Function: Uses a language model prompt to extract metadata (e.g., line count, language, tags) for each post.
get_unified_tags Function: Aggregates tags, simplifies them into unified categories, and maps original tags to these categories using the language model.
Main Execution Block: Executes process_posts on specified JSON files for data preparation.

## How Each File Functions Together
Data Preprocessing: preprocess.py processes raw posts and organizes them into a standardized format, creating a JSON file with enriched metadata.
Data Loading and Filtering: few_shot.py loads the processed data, categorizes it by post length, and provides filtered post examples.
User Interface: main.py facilitates user selection of criteria, connects to generate_post for post generation, and displays the result.
Prompt Creation and Generation: post_generator.py formats the user input as a prompt, enriches it with examples, and invokes the language model via llm_helper.py to produce the post content.

## Example Workflow
Data Preparation: Raw LinkedIn posts are loaded and processed into enriched JSON files with metadata, including language and tags.
User Interaction: The user specifies criteria (e.g., "Topic: Climate," "Length: Medium," "Language: English") via the Streamlit interface.
Post Generation: Based on the specified criteria, the system uses filtered posts as examples to guide the language model in generating a post.
Output: The generated post is displayed to the user, ready for posting or further editing.
## This project automates content generation and offers a powerful, efficient way to generate LinkedIn posts, simplifying the process of consistent, topic-driven, and style-specific post creation for a professional audience.
