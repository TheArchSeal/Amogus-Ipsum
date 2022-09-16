# Amogus-Ipsum
A shitty lorem ipsum generator with support for custom word sets.

Disclaimer: This is quite bad code I threw together in ~2h because I though it'd be funny. If you need something decent, maybe don't use this.

The input file specifies what words can be used for the output.\\
A trailing "-" indicates that the word __must__ be followed by another to create a compound word. \\
A trailing "_" indicates that the word __can__ be followed by another. \\
A leading "-" indicates that the word __must__ follow another word as part of a compound. \\
A leading "_" indicates that the word __can__ follow another word. \\
If the compounded word ends with "-" or "_" it is also able to be compounded meaning some compunds of three or more words may be generated

The config file allows for:
	* "input_file" - Default: "data_in.txt" - Name of file containing word set
	* "output_file" - Default: "text_out.txt" - Name of file to override with output
	* "copy_to_clipboard" - Default: false - If true, the output will additionally be copied to your clipboard
	* "output_char_count" - Default: false - If true, print final character count to console
	* "start_string" - Default: "Amogus ipsum " - String that will always appear first, is not followed by space and following word does not care about leading characters
	* "num_chars_to_generate" - Default: 150 - Approximate amount of characters to generate, the error is dependent on avarage sentence length
	* "word_continue_chance" - Default: 0.2 - Chance (not in percent) that a word with trailing character will create a compound
	* "sentence_continue_chance" - Default: 0.8 - Chance (not in percent) that a centence will add another word, this is then repeted
	* "min_sentence_char_count" - Default: 40 - Minimum number of characters allowed in a sentence
	* "max_sentence_char_count" - Default: 100 - Maximum number of characters allowed. If smaller than "min_sentence_char_count" all sentences will be one word larger than it
	* "comma_chance" - Default: 0.03 - Chance to put a comma after a word
	* "exclemation_mark_chance" - Default: 0.05 - Chance a sentence ends with an exclemation mark instead of a period
	* "question_mark_chance" Default: 0.05 - Chance a sentence ends with a question mark instead of a period. An excemation mark takes precedence if their sum is greater than 1
