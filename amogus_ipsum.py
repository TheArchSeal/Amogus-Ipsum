import random
import json
import pyperclip


def get_config(filename: str) -> dict:
    data = json.load(open(filename))

    config = {
        "input_file": "data_in.txt",
        "output_file": "text_out.txt",
        "copy_to_clipboard": False,
        "output_char_count": False,

        "start_string": "Amogus ipsum ",
        "num_chars_to_generate": 150,
        "word_continue_chance": 0.2,
        "sentence_continue_chance": 0.8,
        "min_sentence_char_count": 40,
        "max_sentence_char_count": 100,
        "comma_chance": 0.03,
        "exclamation_mark_chance": 0.05,
        "question_mark_chance": 0.05
    }

    for i in data:
        config[i] = data[i]

    return config


def filter_beginings(word_set: list[str]) -> list[str]:
    return list(filter(lambda word: word[0] not in "-", word_set))


def filter_follow_ups(word_set: list[str]) -> list[str]:
    return list(filter(lambda word: word[0] in "-_", word_set))


def rand_word(beginings: list[str], follow_ups: list[str], config: dict) -> str:
    word = random.choice(beginings)

    last = word[-1]
    if word in follow_ups:
        word = word[1:]
    if last in "-_":
        word = word[:-1]

    while last == "-" or (last == "_" and random.random() < config["word_continue_chance"]):
        word += random.choice(follow_ups)[1:]

        last = word[-1]
        if last in "-_":
            word = word[:-1]

    return word


def rand_sentence(beginings: list[str], follow_ups: list[str], config: dict) -> str:
    sentence = ""

    while len(sentence) < config["min_sentence_char_count"] or (
            len(sentence) < config["max_sentence_char_count"] and
            random.random() < config["sentence_continue_chance"]):

        sentence += rand_word(beginings, follow_ups, config)

        if random.random() < config["comma_chance"]:
            sentence += ","
        sentence += " "

    sentence = sentence[:-1]
    if sentence[-1] == ",":
        sentence = sentence[:-1]

    punctuation = random.random()
    if punctuation < config["exclamation_mark_chance"]:
        sentence += "!"
    elif punctuation < config["exclamation_mark_chance"] + config["question_mark_chance"]:
        sentence += "?"
    else:
        sentence += "."

    return sentence


def read_from_file(filename: str) -> str:
    file = open(filename, "r")
    string = file.read()
    file.close()
    return string


def write_to_file(filename: str, string: str) -> None:
    file = open(filename, "w")
    file.write(string)
    file.close()


def main():
    config = get_config("config.json")
    unfiltered_word_set = read_from_file(config["input_file"]).split()

    beginings = filter_beginings(unfiltered_word_set)
    follow_ups = filter_follow_ups(unfiltered_word_set)

    ouput_string = (config["start_string"] + rand_sentence(beginings, follow_ups, config) + " ").capitalize()
    while True:
        sentence = rand_sentence(beginings, follow_ups, config).capitalize()
        if abs(len(ouput_string) - config["num_chars_to_generate"]) < abs(len(ouput_string) + len(sentence) - config["num_chars_to_generate"]):
            break
        ouput_string += sentence + " "
    ouput_string = ouput_string[:-1]

    write_to_file(config["output_file"], ouput_string)
    if config["copy_to_clipboard"]:
        pyperclip.copy(ouput_string)
    if config["output_char_count"]:
        print(len(ouput_string))


if __name__ == "__main__":
    main()
