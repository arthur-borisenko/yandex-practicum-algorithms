A = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л",
     "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш",
     "щ", "ъ", "ы", "ь", "э", "ю", "я", 'А', 'Б', 'В', 'Г', 'Д', 'Е',
     'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
     'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю',
     'Я'}


def list_find(l, v):
    for i, e in enumerate(l):
        if e == v:
            return i
    return -1


class G:
    def __init__(self, v):
        self.v = v
        self._i = 0

    def __next__(self):
        if self._i >= len(self.v):
            raise StopIteration
        r = self.v[self._i]
        self._i += 1
        return r


def preprocess_text(text, allowed_symbols,
                    enable_auto_lowercase=True):
    result = []
    for char in text:
        if char in allowed_symbols:
            result.append(char)
        elif char.lower() in allowed_symbols and enable_auto_lowercase:
            result.append(char.lower())
    return result


def encrypt(key: list, data: str, allowed_symbols=None,
            enable_auto_lowercase=True):
    if allowed_symbols is None:
        allowed_symbols = A
    block_length = len(key)
    processed_text = preprocess_text(data, allowed_symbols,
                                     enable_auto_lowercase)
    temp_result: list[list] = []
    processed_text.extend(
        [""] * (block_length - len(processed_text) % block_length))
    for i in range(len(processed_text) // block_length):
        temp_result.append([""] * block_length)
        output_block = temp_result[i]
        block = processed_text[
                i * block_length:i * block_length + block_length]
        for j, el in enumerate(block):
            output_block[int(key[j]) - 1] = el
    result = []
    for i in range(len(temp_result[0])):
        for j in range(len(temp_result)):
            result.append(temp_result[j][i])
    return result


def decrypt(key: list, data: str, allowed_symbols=None,
            enable_auto_lowercase=True):
    if allowed_symbols is None:
        allowed_symbols = A
    block_length = len(key)
    processed_data = preprocess_text(data, allowed_symbols,
                                     enable_auto_lowercase)
    large_columns_count = len(processed_data) % block_length
    processed_input = G(processed_data)
    temp_result = [[]] * block_length
    for i in range(block_length):
        orig_column_pos = list_find(key, i + 1)
        if orig_column_pos < large_columns_count:
            temp_result[orig_column_pos] = []
            for _ in range(len(processed_data) // block_length + 1):
                temp_result[orig_column_pos].append(
                    next(processed_input))
        else:
            temp_result[orig_column_pos] = []
            for _ in range(len(processed_data) // block_length):
                temp_result[orig_column_pos].append(
                    next(processed_input))
    result = []
    for i in range(len(temp_result[0])):
        for j in range(len(temp_result)):
            if len(temp_result[j]) > i:
                result.append(temp_result[j][i])
    return result


if __name__ == "__main__":
    mode = input("[E]ncrypt or [D]ecrypt? ")
    key = input(
        "Enter key. split numbers using spaces (example: 1 2 3 4 5 6 7 8 9 10): ")
    text = input("Enter text: ")
    encrypt_inputs = {"E", "e", "encrypt", "Encrypt"}
    decrypt_inputs = {"D", "d", "decrypt", "Decrypt"}
    if mode in encrypt_inputs:
        print("encrypted text: ",
              *encrypt(list(map(int, key.split())), text), sep="")
    elif mode in decrypt_inputs:
        print("decrypted text: ",
              *decrypt(list(map(int, key.split())), text), sep="")
    else:
        raise ValueError(
            "Invalid mode. Please enter either 'E' or 'D' to encrypt or decrypt.")
